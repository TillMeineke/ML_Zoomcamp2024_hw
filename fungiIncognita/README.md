# 🍄 fungiIncognita - Mushroom Classification 🍄‍🟫

04.11.2024 - 19.11.2024

Author: Till Meineke

<div style="text-align:center;">
  <img src="./images/walking_sillyshrooman.webp" alt="Walking sillyshrooman" style="width:300px;height:auto;">
</div>

source: [Giphy](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnJxa2xoY2R0YnVnZGVuaWMzcjVzc3VwNGFmOXl1bTJzM2JjOXFmZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/BPvLYetv28UVFBHCO2/giphy.gif)

## Problem description

Walking through the woods collecting mushrooms can be a fun activity. However, it can also be dangerous if you don't know which mushrooms are edible or not. The goal of this project is to build and deploy a model that can predict which mushrooms you picked based on some simple characteristics.

To better understand the problem, I will use the [Classification Mushroom Data 2020](https://visualization.group/data/mushroom/) dataset. The primary data describes 173 mushroom species, which can be used for simulating hypothetical mushrooms. Since the secondary data contains 61,069 hypothetical mushrooms for __binary classification without names__, I have to generate simulated data with species names.

To ensure that the generated dataset is of high quality and relevant for the task you are attempting to solve.
When working with synthetic data, consider the following points:

- Clearly document how you generated the synthetic dataset and the reasoning behind its design.
- Provide sufficient context about the dataset and the model you are building for your peers who will review your project.

## Project structure

```plaintext
├── .gitignore        <- Files that are ignored by git.
├── data              <- Data folder
│   ├── raw
│   └── secondary_data_generated_with_names.csv
├── docker            <- Docker files
│   ├── serve.Dockerfile
│   └── test.Dockerfile
├── docs              <- Documentation files
│   ├── 41598_2021_87602_MOESM1_ESM.pdf
│   └── s41598-021-87602-3.pdf
├── environment.yml   <- Conda environment file.
├── images            <- Images folder
│   └── ...
├── LICENSE
├── Makefile          <- Makefile with commands like `make help`.
├── notebooks         <- Jupyter notebooks
│   ├── 01_eda.ipynb
│   └── generate_sample_dataset.ipynb
├── README.md         <- This file
└── src               <- Source code
    ├── __pycache__
    ├── data_cat.py
    ├── gen_corr_norm.py
    ├── generate_fungi_database_v1.py
    ├── primary_data_gen.py
    └── text_attr_match.py
```

## EDA

## Model training

## Exporting notebook to python script

## Reproducibility

## Model deployment

## Dependency and environment management

Preferably, you can use make commands (from Makefile) or directly run scripts from `scr`.
Refer to section below for the descriptions of make commands. Before running it, consider creating
a virtual environment

### Makefile and test example

Try out the make commands (see `make help`).

### Conda environment

Working in conda environment `./environment.yml`. Install with:

```bash
conda env create -f environment.yml
```

## Containerization

Currently, you can find the following docker files:

<!-- jupyter.Dockerfile builds an image for running notebooks. -->
`test.Dockerfile` builds an image to run all tests in (make test-docker).
`serve.Dockerfile` build an image to serve the trained model via a REST api.
<!-- To ease the serving it uses open source dploy-kickstart module. To find more info about dploy-kickstart click here. -->
Finally, you can start all services using `docker-compose`:
for example `docker-compose up test` or `docker-compose up serve`.

<!-- Do you need a notebook for development? Just run docker-compose up jupyter. It will launch a Jupyter Notebook with access to your local development files. -->

## Cloud deployment

## Submission

[link](https://courses.datatalks.club/ml-zoomcamp-2024/project/midterm)