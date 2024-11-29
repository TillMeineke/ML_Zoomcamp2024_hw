# Evaluation of midterm project

Evaluation done by Till Meineke on Nov. 29th 2024.

## Problem description

* 2 points: Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used

1. Dataset source is not mentioned in the README.
2. Laptop price prediction dataset used in HW 2

## EDA

* 2 points: Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis)

* not mentioned in README
* EDA with AutoViz?

## Model training

* 3 points: Trained multiple models and tuned their parameters.

## Exporting notebook to script

* 1 point: The logic for training the model is exported to a separate script

## Reproducibility

* 0 points: Not possible to execute the notebook and the training script. Data is missing or it's not easily accessible

* first cell not running -> ModuleNotFoundError: No module named 'autoviz'
* instructions for environment setup in README don't work on macOS

## Model deployment

* 1 point: Model is deployed (with Flask, BentoML or a similar framework)

## Dependency and environment management

* 1 point: Provided a file with dependencies (requirements.txt, pipfile, bentofile.yaml with dependencies, etc)

* environment.yml not working on macOS
* pip install -r requirements.txt -> 31331 segmentation fault
* pipenv install -> ERROR: Couldn't install package: [1m{}[0m [33mPackage installation failed...[0m

## Containerization

* 2 points: The application is containerized and the README describes how to build a container and how to run it

## Cloud deployment

* 0 points: No deployment to the cloud

Total 12 points

[Criteria](https://docs.google.com/spreadsheets/d/e/2PACX-1vQCwqAtkjl07MTW-SxWUK9GUvMQ3Pv_fF8UadcuIYLgHa0PlNu9BRWtfLgivI8xSCncQs82HDwGXSm3/pubhtml)
