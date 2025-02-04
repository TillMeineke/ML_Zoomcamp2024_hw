# 🚖 NY Taxi demand forecast 🚕

03.01.2025 - 04.02.2025

Author: Till Meineke

![NY Taxi](./images/NEW-YORK-TAXI.jpg#taxi)

## Problem description

Demand forecasting is always helpful for companies to optimize their resources and make better decisions. In this project, we will work with a dataset of New York taxi trips. The goal is to predict the number of taxi trips for the next week.

## Run the project

### Clone the repository

Either clone my whole [repository](https://github.com/TillMeineke/ML_Zoomcamp2024_hw)

```bash
git clone https://github.com/TillMeineke/ML_Zoomcamp2024_hw.git
# and move to the project folder
cd ML_Zoomcamp2024_hw/NYTaxiForecast
```

or download needed files from this repository.

### Install dependencies

```bash
conda env create -f environment.yml
conda activate NYTaxiForecast
```

### Run the notebook

```bash
jupyter notebook notebooks/00_EDA_prophet_train.ipynb
```

### Run the training script

```bash
python src/train.py
```

## EDA

### Ranges of values

I restrict the data to a period from 01.01.2023 to 31.12.2023, because it the last full year of data.

### Missing values

Did some check

### Analysis of target variable

- mean
- trend
- seasonality

### Feature importance analysis

## Model training

- Prophet

## Exporting notebook to python script

see `train.py` in `src`-folder

## Reproducibility

## Model deployment

## Dependency and environment management

### Conda environment

see running the project and `environment.yml`

## Containerization



## Cloud deployment

## Deliverables

For a project, the repository/folder should contain the following:

- `README.md` with
  - [x] Description of the problem
    - [ ] 0 points: Problem is not described
    - [x] 1 point: Problem is described in README birefly without much details
    - [ ] 2 points: Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used
  - [ ] Instructions on how to run the project
- Data
  - [x] You should either commit the dataset you used or have clear instructions how to download the dataset
- Notebook (suggested name - `notebook.ipynb`) with
  - [x] Data preparation and data cleaning
  - [ ] EDA, feature importance analysis
    - [ ] 0 points: No EDA
    - [x] 1 point: Basic EDA (looking at min-max values, checking for missing values)
    - [ ] 2 points: Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis) For images: analyzing the content of the images. For texts: frequent words, word clouds, etc
  - [x] Model selection process and parameter tuning
- Script `train.py` (suggested name)
  - [x] Training the final model
    - [ ] 0 points: No model training
    - [x] 1 point: Trained only one model, no parameter tuning
    - [ ] 2 points: Trained multiple models (linear and tree-based). For neural networks: tried multiple variations - with dropout or without, with extra inner layers or without
    - [ ] 3 points: Trained multiple models and tuned their parameters. For neural networks: same as previous, but also with tuning: adjusting learning rate, dropout rate, size of the inner layer, etc.
  - [x] Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
    - [ ] 0 points: No script for training a model
    - [x] 1 point: The logic for training the model is exported to a separate script
- [ ] Reproducibility
  - [ ] 0 points: Not possible to execute the notebook and the training script. Data is missing or it's not easily accessible
  - [x] 1 point: It's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data
- Script `predict.py` (suggested name)
  - [ ] Loading the model
  - [ ] Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)
    - [ ] 0 points: Model is not deployed
    - [ ] 1 point: Model is deployed (with Flask, BentoML or a similar framework)
- Files with dependencies
  - [ ] `Pipenv` and `Pipenv.lock` if you use Pipenv
  - [x] or equivalents: conda environment file, `requirements.txt` or `pyproject.toml`
    - [ ] 0 points: No dependency management
    - [ ] 1 point: Provided a file with dependencies (requirements.txt, pipfile, bentofile.yaml with dependencies, etc)
    - [x] 2 points: Provided a file with dependencies and used virtual environment. README says how to install the dependencies and how to activate the env
- [ ] Dockerfile for running the service
  - [ ] 0 points: No containerization
  - [ ] 1 point: Dockerfile is provided or a tool that creates a docker image is used (e.g. BentoML)
  - [ ] 2 points: The application is containerized and the README describes how to build a contained and how to run it
- Cloud Deployment
  - [ ] URL to the service you deployed or
  - [ ] Video or image of how you interact with the deployed service
    - [ ] 0 points: No deployment to the cloud
    - [ ] 1 point: Docs describe clearly (with code) how to deploy the service to cloud or kubernetes cluster (local or remote)
    - [ ] 2 points: There's code for deployment to cloud or kubernetes cluster (local or remote). There's a URL for testing - or video/screenshot of testing it

<style>img[src$="#taxi"] {
  display: block;
  margin: 0 auto;
  border-radius: 10px;
  width: 600px;
}
</style>
