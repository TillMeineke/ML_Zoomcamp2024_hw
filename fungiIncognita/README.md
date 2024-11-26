# 🍄 fungiIncognita - Mushroom Classification 🍄‍🟫

04.11.2024 - 26.11.2024

Author: Till Meineke

<div style="text-align:center;">
  <img src="./images/walking_sillyshrooman.webp" alt="Walking sillyshrooman" style="width:300px;height:auto;">
</div>

source: [Giphy](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnJxa2xoY2R0YnVnZGVuaWMzcjVzc3VwNGFmOXl1bTJzM2JjOXFmZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/BPvLYetv28UVFBHCO2/giphy.gif)

> [!IMPORTANT]
>
> Work in progress.
>
> My daugther got sick and I lost 1,5 weeks. I will finish the project, but you can rate this version. Basic functionality is working.
>
> Readme is not finished yet. EDA is missing some parts and is unstructured.
>
> You can test with `python predict_test.py` in a conda enviroment installed with `conda env create -f environment.yml` in this directory.
>
> ![Prediction is working](./images/prediction_working_low.mov "It's working")

## Problem description

Walking through the woods collecting mushrooms can be a fun activity. However, it can also be dangerous if you don't know which mushrooms are edible or not. The goal of this project is to build and deploy a model that can predict which mushrooms you picked based on some simple characteristics.

To better understand the problem, I will use the [Classification Mushroom Data 2020](https://visualization.group/data/mushroom/) dataset. The primary data describes 173 mushroom species, which can be used for simulating hypothetical mushrooms. Since the attached secondary data contains 61,069 hypothetical mushrooms for __binary classification without names__, I have to generate simulated data with species names.

Ensure that the generated dataset is of high quality and relevant for the task you are attempting to solve.
When working with synthetic data, consider the following points:

- Clearly document how you generated the synthetic dataset and the reasoning behind its design.
- Provide sufficient context about the dataset and the model you are building for your peers who will review your project.

## Project structure

```plaintext
├── data
│   ├── raw
│   │   ├── primary_data_edited.csv                 <-- Raw data from paper
│   │   ├── primary_data_meta.txt                   <-- Raw data from paper (description)
│   │   ├── secondary_data_generated.csv            <-- Raw data from paper
│   │   └── secondary_data_meta.txt                 <-- Raw data from paper (description)
│   └── secondary_data_generated_with_names.csv     <-- Generated data
├── images                                          <-- Images for readme
├── models
│   └── model_md=20_msl=5.bin                       <-- Trained model
├── notebooks
│   └── 01_eda.ipynb                                <-- Exploratory data analysis
├── references
│   ├── 'Collins Mushroom Miscellany.epub'          <-- Book with mushroom images
│   ├── 'Mushroom data creation.pdf'                <-- Main paper for creating mushroom data
│   ├── 'Mushroom data creation_sup.pdf'            <-- Supplementary material
│   └── mushrooms-collins-gem.pdf                   <-- Book with mushroom images
├── src                                             <-- Source code for use in this project
│   ├── services
│   │   ├── Images                                  <-- Images from book
│   │   ├── Text                                    <-- Text from book
│   │   └── rename_images.py                        <-- Script to rename images
│   ├── __init__.py                                 <-- Python package initializer file
│   ├── data_cat.py                                 <-- Script to categorize data
│   ├── gen_corr_norm.py                            <-- Script to generate correlated and normalized data
│   ├── mushroom_class_fix.py
│   ├── primary_data_gen.py
│   ├── secondary_data_gen.py                       <-- Script to generate secondary data
│   ├── stats_graphics.py
│   ├── text_attr_match.py
│   └── util_func.py
├── .dockerignore                                   <-- Docker ignore file
├── .gitignore                                      <-- Git ignore file
├── Dockerfile                                      <-- Docker file
├── environment.yml                                 <-- Conda environment file
├── LICENSE
├── Makefile
├── Pipfile                                         <-- Pipenv file
├── Pipfile.lock                                    <-- Pipenv lock file
├── predict.py                                      <-- Prediction script
├── predict_test.py                                 <-- Prediction test script
├── README.md                                       <-- The file you are currently reading
└── train.py                                        <-- Training script
```

## EDA

You can find the EDA in this [notebook](./notebooks/01_eda.ipynb).

### Ranges of values

![](./images/3D-scatter_fungi%20features.png)

### Missing values

### Analysis of the target variable

### Feature importance analysis

## Model training

I used a Logistic Regression model and a Decision Tree model. I used Cross-Validation to evaluate the models.

## Exporting notebook to python script

See `train.py`. Model is saved in `models` folder.

## Reproducibility

## Model deployment

## Dependency and environment management

Preferably, you can use make commands (from Makefile) or directly run scripts from `scr`.
Refer to section below for the descriptions of make commands. Before running it, consider creating
a virtual environment

### Makefile and test example (not fully implemented)

Try out the make commands (see `make help`).

> [!IMPORTANT]
>
> ```bash
> make grow_fungi
> ```
>
> will overwrite the generated data in `data/secondary_data_generated_with_names.csv`.

### Conda environment

Development was done in conda environment `./environment.yml`. Install with:

```bash
conda env create -f environment.yml
```

### Pipenv

For the Docker container, I used pipenv. You can install the environment with:

```bash
pipenv install
```

## Containerization

Currently, you can find the following docker files:

- [`Dockerfile`](./Dockerfile)

It is used to build an image for running the model. You can build the image with:

```bash
docker build -t fungi-incognita .
```

and run it with:

```bash
docker run -it --rm -p 9696:9696 fungi-incognita
```

This will start a Flask server on port 9696.

[`predict.py`](./predict.py) is the script that is run when the container starts. It is momentarily configured for testing with docker. You can modify it to test locally without docker, by commenting/uncommenting the following lines:

```python
# MODEL_FILE = "./models/model_md=20_msl=5.bin" # local testing without docker
MODEL_FILE = "./model_md=20_msl=5.bin"  # testing with docker
```

<!-- jupyter.Dockerfile builds an image for running notebooks. -->
<!-- `test.Dockerfile` builds an image to run all tests in (make test-docker). -->
<!-- `serve.Dockerfile` build an image to serve the trained model via a REST api. -->
<!-- To ease the serving it uses open source dploy-kickstart module. To find more info about dploy-kickstart click here. -->
<!-- Finally, you can start all services using `docker-compose`: -->
<!-- for example `docker-compose up test` or `docker-compose up serve`. -->

<!-- Do you need a notebook for development? Just run docker-compose up jupyter. It will launch a Jupyter Notebook with access to your local development files. -->

## Cloud deployment

### EB deployment

EB is running under `fungi-classifier.eba-rpcwcrqg.eu-central-1.elasticbeanstalk.com`

## Web application (not implemented)

Finally, I will create a web application to classify mushrooms. The user can enter the characteristics of the mushroom or generate a random mushroom.

The application will then classify the mushroom species and provide the user with full information about the species and a picture for reference.

## Submission

[link](https://courses.datatalks.club/ml-zoomcamp-2024/project/midterm)
