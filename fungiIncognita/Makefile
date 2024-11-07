# stolen from https://github.com/datarootsio/ml-skeleton-py/tree/master
# .PHONY: help conda_environment requirements train predict
.DEFAULT_GOAL := help

DATASET := data/raw/primary_data_edited.csv

# install: ## install dependencies
# FIXME: code for installing dependencies
#	pip install -e ".[test, serve]"



conda_environment: ## create conda environment
	@echo "Creating environment"
	conda env create -f environment.yml
	@echo "Activating environment"
	conda activate fungiIncognita
#    $(shell mkdir -p Data/raw)
#    $(shell mkdir -p Data/cleaned)
#    $(shell mkdir -p reports/figures)
#    $(shell mkdir -p reports/)

clean: ## clean artifacts
	@echo ">>> cleaning artifacts"
#	rm -rf data/raw/*
	rm -rf data/cleaned/*

grow_fungi: $(DATASET) ## 🍄 generate dataset, you can pass arguments as follows: make ARGS="--foo 10 --bar 20" generate-dataset

$(DATASET):
	@echo ">>> generating dataset"
#	FIXME: needs implementation
	python ./src/generate_fungi_database.py $(ARGS)

train: $(DATASET) ## train the model, you can pass arguments as follows: make ARGS="--foo 10 --bar 20" train
	@echo ">>> training model"
#	FIXME: needs implementation
	python ./src/train.py $(ARGS)

serve: ## serve trained model with a REST API
# using dploy-kickstart
	@echo ">>> serving the trained model"
#	FIXME: code for building docker image and serving the model
# 	kickstart serve -e ml_skeleton_py/model/predict.py -l .

run-pipeline: install clean generate-dataset train serve  ## install dependencies -> clean artifacts -> generate dataset -> train -> serve
#	FIXME: 

lint: ## flake8 linting and black code style
	@echo ">>> black files"
#	FIXME: needs implementation
#	black scripts ml_skeleton_py tests

	@echo ">>> linting files"
#	FIXME: needs implementation
#	flake8 scripts ml_skeleton_py tests

coverage: ## create coverage report
	@echo ">>> running coverage pytest"
	pytest --cov=./ --cov-report=xml

test: ## run unit tests in the current virtual environment
	@echo ">>> running unit tests with the existing environment"
	pytest

test-docker: ## run unit tests in docker environment
	@echo ">>> running unit tests in an isolated docker environment"
	docker-compose up test

help: ## show help on available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

~~