# Evaluation of midterm project

Evaluation done by Till Meineke on Nov. 29th 2024.

## Problem description

* 2 points: Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used

## EDA

* 2 points: Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis)

## Model training

* 3 points: Trained multiple models and tuned their parameters.

## Exporting notebook to script

* 1 point: The logic for training the model is exported to a separate script

## Reproducibility

* 1 point: It's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data

* `python codes/predict_main.py`, had to change into `codes` folder to run the script, otherwise it would not find the `dv.bin` file. Not mentioned in `README.md` file.

```plaintext
Traceback (most recent call last): File "/Users/tillmeineke/ML/ML_Zoomcamp2024_hw/Midterm-Project/codes/predict_main.py", line 8, in <module>
    with open("../models/dv.bin", "rb") as file_in:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '../models/dv.bin'
```

* no env file provided

```plaintext
/Users/tillmeineke/.pyenv/versions/3.11.3/lib/python3.11/site-packages/sklearn/base.py:376: InconsistentVersionWarning: Trying to unpickle estimator RandomForestClassifier from version 1.5.1 when using version 1.5.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
[15:04:23] WARNING: /Users/runner/work/xgboost/xgboost/python-package/build/temp.macosx-11.0-arm64-cpython-38/xgboost/src/learner.cc:553: 
  If you are loading a serialized model (like pickle in Python, RDS in R) generated by
  older XGBoost, please export the model by calling `Booster.save_model` from that version
  first, then load it back in current version. See:

    https://xgboost.readthedocs.io/en/latest/tutorials/saving_model.html

  for more details about differences between saving model and serializing.
```

* last cell does not run

```plaintext
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[48], line 2
      1 with open("../models/dv.bin", "wb") as file_in:
----> 2     pickle.dump(dv, file_in)
      4 with open("../models/lr.bin", "wb") as file_in:
      5     pickle.dump(model, file_in)

NameError: name 'pickle' is not defined
```

## Model deployment

* 1 point: Model is deployed (with Flask, BentoML or a similar framework)

## Dependency and environment management

* 1 point: Provided a file with dependencies (pipfile)

## Containerization

* 1 point: Dockerfile is provided

* not mentioned in `README.md` file, no explanation how to run the docker container

## Cloud deployment

* 0 points: No deployment to the cloud

Total 12 points

[Criteria](https://docs.google.com/spreadsheets/d/e/2PACX-1vQCwqAtkjl07MTW-SxWUK9GUvMQ3Pv_fF8UadcuIYLgHa0PlNu9BRWtfLgivI8xSCncQs82HDwGXSm3/pubhtml)