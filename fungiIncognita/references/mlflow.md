# ML Flow - MLOps Zoomcamp Module 2

## 2.1 Experiment Tracking Intro

### Important Concepts

- **ML experiment**: a process of building a ML model
- **Experiment run**: each trial in a ML experiment
- **Run artifact**: any file that is associated with a ML run
- **Eperiment metadata**

### What's experiment tracking?

Experiment tracking is the process of keeping track of all the **relevant information** from a **ML experiment**, which includes:

- Source code
- Environment
- Data
- Model
- Hyperparameters
- Metrics
- ...

### Why is experiment tracking so important?

In general, because of these 3 main reasons:

- Reproducibility
- Organization
- Optimization

### Tracking experiments in spreadsheets

Why is it not enough?

- Error prone
- No standard format
- Visibility & Collaboration

### MLFlow

Definition: "An open source platform for the machine learning lifecycle." [Official mlflow documentation](https://mlflow.org/docs/latest/index.html)

In practice, it's just a Python package that can be installed with pip, and it contains four main modules:

- Tracking
- Models
- Model Registry
- Projects

### Tracking experiments with MLFlow

The mlflow Tracking module allows you to organize your experiments into runs, and to keep track of:

- Parameters
- Metrics
- Metadata
- Artifacts
- Models

Along with this information, MLFlow automatically logs extra information about the run:

- Source code
- Version of the code (git commit)
- Start and end time
- Author

### MLFlow demo

```bash
mlflow
```

shows the available commands.

```bash
mlflow ui
```

starts the MLFlow UI. Gunicorn server is started on localhost:5000. Play around with the UI to get a feel of how it works. See experiments and models. no models registered yet.

## 2.2.Getting started with MLFlow

- Prepare the local env
- Install mlflow client
- Add MLFlow to the existing notebook, log the predictions, show it in MLflow UI

Format: code-along

Input:

- Notebook from module 1

Output:

- Updated notebook with MLFlow
- Logged predictions

requirements.txt:

```txt
mlflow
jupyter
scikit-learn
pandas
seaborn
hyperopt
xgboost
```

install in conda environment

```bash
pip install -r requirements.txt
```

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

