#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import KFold, train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

# parameters
random_state = 42
max_depth = 20
min_samples_leaf = 5
output_file = f"./models/model_md={max_depth}_msl={min_samples_leaf}.bin"

# load data
df = pd.read_csv("./data/secondary_data_generated_with_names.csv", sep=";")
df = df.sample(frac=1).reset_index(drop=True)

# drop columns with missing values
df_no_missing = df.dropna(axis=1, inplace=False)
df_no_missing = df_no_missing.drop(columns=["family"], inplace=False)
df_no_missing = df_no_missing.drop(columns=["class"], inplace=False)

cat_features = [
    #    "family",
    #    "class",
    "cap-shape",
    "cap-color",
    "does-bruise-or-bleed",
    "gill-color",
    "stem-color",
    "has-ring",
    "habitat",
    "season",
]

num_features = [
    "cap-diameter",
    "stem-height",
    "stem-width",
]

df_full_train, df_test = train_test_split(df_no_missing, test_size=0.2, random_state=42)

def train(df_train, y_train, random_state=42, max_depth=20, min_samples_leaf=5):
    dicts = df_train[cat_features + num_features].to_dict(orient="records")

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    dt_classifier = DecisionTreeClassifier(
        random_state=42, max_depth=max_depth, min_samples_leaf=min_samples_leaf
    )
    dt_classifier.fit(X_train, y_train)

    return dv, dt_classifier

def predict(df, dv, model):
    dicts = df[cat_features + num_features].to_dict(orient="records")

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)

    return y_pred

print(f"Training model with max_depth={max_depth} and min_samples_leaf={min_samples_leaf}")

kfold = KFold(n_splits=5, shuffle=True, random_state=1)
scores = []
fold = 0

for train_idx, val_idx in kfold.split(df_full_train):
    fold += 1
    print(f"Fold: {fold}")

    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train["name"].values
    y_val = df_val["name"].values

    dv, model = train(df_train, y_train, max_depth=max_depth, min_samples_leaf=min_samples_leaf)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred, multi_class="ovr")
    scores.append(auc)

    print(f'auc on fold: {fold} is {auc}')

print(f"Mean AUC: {np.mean(scores)}")
print(f"Standard deviation: {np.std(scores)}")

# train final model
dv, model = train(df_full_train, df_full_train["name"].values, max_depth)
y_pred = predict(df_test, dv, model)

y_test = df_test["name"].values
auc = roc_auc_score(y_test, y_pred, multi_class="ovr")

print(f"Final AUC: {auc}")

# save the model
with open(output_file, "wb") as f_out:
    pickle.dump((dv, model), f_out)

print(f"Model saved to {output_file} ")