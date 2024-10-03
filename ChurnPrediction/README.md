# 3. Machine Learning for Classification: Churn Prediction

## Binary Classification

### 3.1 Churn prediction project

- Telco Customer Churn Prediction
- Who will leave the company?
- Score between 0 and 1
- eMail 25% discount, to prevent churn

### 3.2 Data preparation

- Load the data
- make column names and values look uniform
- `totalcharges` is an object, convert to number, `seniorcitizen` is an integer, convert to categorical variable, `churn` is an object, convert to int (0, 1)

### 3.3 Validation Framework

- train/val/test split (60/20/20) with sklearn, seed=1
- use `churn` as target

### 3.4 EDA

- check missing values
- distribution of the target variable `churn`
- numerical and categorical variables

### 3.5 Feature Importance: Churn Rate and Risk Ratio

- identify which feature affect the target variable
- churn rate = number of churned customers / total number of customers
- Risk ratio = churn rate of a segment / average churn rate

### 3.6 Feature Importance: Mutual Information

### 3.7 Feature Importance: Correlation

- correlation coefficient

### 3.8 One-hot encoding

- sklearn `DictVectorizer`

### 3.9 Logistic Regression

- for binary classification
- linear vs. logistic regression

### 3.10 Training a logistic regression with Scikit-Learn

- train a model
- apply the model to the validation set
- calculate the accuracy

### 3.11 Model Interpretation
