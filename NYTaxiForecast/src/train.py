#!/usr/bin/env python
# coding: utf-8


# ## Import libraries and load data
import pandas as pd
import numpy as np
# import plotly.express as px
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statsmodels.tsa.deterministic import CalendarFourier, DeterministicProcess
from neuralprophet import NeuralProphet

# plt.style.available

from warnings import simplefilter

simplefilter("ignore")

base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2023-"

# Initialize an empty DataFrame
df = pd.DataFrame()

for item in range(1, 13):
    url = base_url + str(item).zfill(2) + ".parquet"

    # read the data
    print(f"Ingesting {url.split('/')[-1]}")
    df_single_month = pd.read_parquet(url)

    # concatenate the data
    df = pd.concat([df, df_single_month], axis=0)

df_lookup = pd.read_csv(
    "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
)

# Merge the data
df = df.merge(df_lookup, left_on="PULocationID", right_on="LocationID", how="left")
df = df.merge(
    df_lookup,
    left_on="DOLocationID",
    right_on="LocationID",
    how="left",
    suffixes=("_PU", "_DO"),
)

# drop 'LocationID_PU' and 'LocationID_DO' columns
df.drop(columns=["LocationID_PU", "LocationID_DO"], inplace=True)


df2 = df.copy()


# drop rows with missing values
df.dropna(inplace=True, axis=1)
missing_values2 = df.isnull().sum()


## Data Cleaning
df["date"] = df["lpep_pickup_datetime"].dt.date

# remove outliers before 2023
df = df[df["lpep_pickup_datetime"].dt.year == 2023]

################################################################################
# # EDA
# ## Is there a trend in the daily number of trips?
################################################################################

trips_per_day = df["date"].value_counts().sort_index()
# set index frequency to daily
trips_per_day.index = pd.to_datetime(trips_per_day.index)
trips_per_day.index.freq = "D"

moving_average = trips_per_day.rolling(
    window=365,  # 365-day window
    center=True,  # puts the average at the center of the window
    min_periods=183,  # choose about half the window size
).mean()  # compute the mean (could also do median, std, min, max, ...)

dp = DeterministicProcess(
    index=trips_per_day.index,  # dates from the training data
    constant=True,  # dummy feature for the bias (y_intercept)
    order=1,  # the time dummy (trend)
    drop=True,  # drop terms if necessary to avoid collinearity
)
# `in_sample` creates features for the dates given in the `index` argument
X = dp.in_sample()
y = trips_per_day  # the target

# The intercept is the same as the `const` feature from
# DeterministicProcess. LinearRegression behaves badly with duplicated
# features, so we need to be sure to exclude it here.
model = LinearRegression(fit_intercept=False)
model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=X.index)

# ### Forecast the trend
X = dp.out_of_sample(steps=30)
y_lin_fore = pd.Series(model.predict(X), index=X.index)


# Get the last date from trips_per_day
last_date = pd.to_datetime("2023-12-31").date()
# Create new dates for forecast starting from January 1, 2024
forecast_dates = pd.date_range(start="2024-01-01", periods=30, freq="D")

# Convert forecast to a Series with proper dates
y_lin_fore = pd.Series(y_lin_fore.values, index=forecast_dates)

# Plot with adjusted dates
start_date = pd.to_datetime("2023-11-01").date()
# Convert start_date to datetime64
start_date = pd.to_datetime(start_date)

# ## Seasonality

# Let's look for regular, periodic change in the mean of the series - seasonality.
trips_per_day.index = pd.to_datetime(trips_per_day.index)


# Convert trips_per_day to a DataFrame with datetime index
X = trips_per_day.to_frame(name="Trips per day")
X.index = pd.to_datetime(X.index, unit="D")


## Feature engineering
# days within a week
X["day"] = X.index.dayofweek  # the x-axis (freq)
X["week"] = X.index.isocalendar().week  # the seasonal period (period)
X["month"] = X.index.month  # the seasonal period (period)

# days within a year
X["dayofyear"] = X.index.dayofyear
X["dayofmonth"] = X.index.day
X["year"] = X.index.year


y = X["Trips per day"]
y.index = pd.to_datetime(y.index, unit="D")



fourier = CalendarFourier(
    freq="YE", order=10
)  # 10 sin/cos pairs for "A"nnual seasonality

dp = DeterministicProcess(
    index=pd.to_datetime(X.index, unit="D"),
    constant=True,  # dummy feature for bias (y-intercept)
    order=1,  # trend (order 1 means linear)
    seasonal=True,  # weekly seasonality (indicators)
    additional_terms=[fourier],  # annual seasonality (fourier)
    drop=True,  # drop terms to avoid collinearity
)

X = dp.in_sample()  # create features for dates in X.index

# With our feature set created, we're ready to fit the model and make
# predictions. We'll add a 90-day forecast to see how our model extrapolates
# beyond the training data.


# Get the last date from your training data
last_date = dp.index[-1]
# Create future dates index
future_dates = pd.date_range(
    start=dp.index[-1],  # Start from last date in training data
    periods=91,  # steps + 1 to account for the last date
    freq="D",  # Use 'D' for daily, adjust if needed
)[1:]  # Remove first date to avoid overlap

model = LinearRegression(fit_intercept=False)
_ = model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=y.index)
X_fore = dp.out_of_sample(steps=90, forecast_index=future_dates)
y_fore = pd.Series(model.predict(X_fore), index=X_fore.index)

# So this forecast doesn`t look so bright for the taxi drivers 😢

# There's still more we can do with time series to improve our forecasts.
# Next we'll look how to use time series themselves as a features.
# Using time series as inputs to a forecast lets us model the another component
# often found in series: *cycles*.

# ## Serial Dependence

# ### Lagged Series and Lag Plots

# To investigate possible serial dependence (like cycles) in a time series, we
# need to create "lagged" copies of the series. **Lagging** a time series means
# to shift its values forward one or more time steps, or equivalently, to shift
# the times in its index backward one or more steps. In either case, the effect
# is that the observations in the lagged series will appear to have
# happened later in time.

def make_lags(ts, lags):
    return pd.concat({f"y_lag_{i}": ts.shift(i) for i in range(1, lags + 1)}, axis=1)

X = make_lags(y, lags=7)
X = X.fillna(0.0)


# ### split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=60, shuffle=False)


# ### fit and predict
model = LinearRegression(fit_intercept=True)  # since we didn't use DeterministicProcess
model.fit(X_train, y_train)
y_pred = pd.Series(model.predict(X_train), index=y_train.index)
y_fore = pd.Series(model.predict(X_test), index=y_test.index)


# Now this model looks already much better!
# But it is not fully capturing the dropped numbers around x-Mas and New Year.
#
# We can see how our model needs a time step to react to sudden changes in the
# target series. This is a common limitation of models using only lags of the
# target series as features.

# ## Forcasting with NeuralProphet
# ### preprocessing of the data
df_sth = pd.DataFrame({"ds": y.index, "y": y.values})

# ### Create dataframe for NeuralProphet

data = df_sth.copy()
#data.dropna(inplace=True)
data.columns = ["ds", "y"]
data.head()


# ### Train
m = NeuralProphet()
m.fit(data, freq="D", epochs=1000)
# m.set_plotting_backend("matplotlib")

# ### forecast
future = m.make_future_dataframe(data, periods=30)
forecast = m.predict(future)
forecast.head()


# ### save the model
with open("../models/prophet.pkl", "wb") as f:
    pickle.dump(m, f)
