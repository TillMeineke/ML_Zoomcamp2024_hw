# Evaluation of midterm project

Evaluation done by Till Meineke on Nov. 29th 2024.

## Problem description

* 2 points: Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used

* very short README, no pictures, no real reference to dataset, simple usecase close to the one in the course 

## EDA

* 2 points: Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis)

* all good

## Model training

* 3 points: Trained multiple models and tuned their parameters.

* models
  * logistic regression
  * Random Forest -> tuned n_estimators

## Exporting notebook to script

* 1 point: The logic for training the model is exported to a separate script

## Reproducibility

* 1 point: It's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data

* `docker run -it --rm -p 9696:9696 midterm-project1`
  * /usr/local/lib/python3.11/site-packages/sklearn/base.py:376: InconsistentVersionWarning: Trying to unpickle estimator DecisionTreeClassifier from version 1.5.1 when using version 1.5.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to: <https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations>

## Model deployment

* 1 point: Model is deployed (with Flask)

## Dependency and environment management

* 2 points: Provided a file with dependencies and used virtual environment. README says how to install the dependencies and how to activate the env

* `pip install -r requirements.txt`
  * ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts. dash 2.13.0 requires Flask<2.3.0,>=1.0.4, but you have flask 3.1.0 which is incompatible. dash 2.13.0 requires Werkzeug<2.3.0, but you have werkzeug 3.1.3 which is incompatible.

## Containerization

* 2 points: The application is containerized and the README describes how to build a container and how to run it

## Cloud deployment

* 0 points: No deployment to the cloud

Total 14 points

[Criteria](https://docs.google.com/spreadsheets/d/e/2PACX-1vQCwqAtkjl07MTW-SxWUK9GUvMQ3Pv_fF8UadcuIYLgHa0PlNu9BRWtfLgivI8xSCncQs82HDwGXSm3/pubhtml)
