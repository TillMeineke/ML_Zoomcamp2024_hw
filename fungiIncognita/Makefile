# stolen from https://github.com/datarootsio/ml-skeleton-py/tree/master


#.PHONY: help conda_environment requirements train predict
#.PHONY: help grow_fungi conda_environment $(DATASET)
.DEFAULT_GOAL := help


DATASET := data/raw/primary_data_edited.csv

#install: ## install dependencies
# FIXME: code for installing dependencies
#	pip install -e ".[test, serve]"

new_conda_environment: ## 🎄 create conda environment 🎄
	@echo "Creating environment"
	conda env create -f environment.yml
# and activate FIXME: needs implementation / not working
#	@echo "Activating environment"
#	conda activate fungiIncognita
#    $(shell mkdir -p Data/raw)
#    $(shell mkdir -p Data/cleaned)
#    $(shell mkdir -p reports/figures)
#    $(shell mkdir -p reports/)

# FIXME: needs implementation / not working
# clean_conda_environment: ## 🗑️ deactivate and remove conda environment 🗑️
# 	@echo ">>> checking environment"
# 	@if conda env list | grep -q "fungiIncognita"; then \
# 		echo ">>> deactivating environment"; \
# 		source $$(conda info --base)/etc/profile.d/conda.sh && conda deactivate; \
# 		echo ">>> removing environment"; \
# 		conda env remove --name fungiIncognita  --yes; \
# 	else \
# 		echo ">>> environment not found, skipping cleanup"; \
# 	fi

#	@echo ">>> cleaning artifacts"
#	rm -rf data/raw/*
#	rm -rf data/cleaned/*

new_pipenv_environment: ## 🎄 create and activate pipenv environment 🎄
	@echo "Creating environment"
	pipenv install
	@echo "Activating environment"
	pipenv shell

clean_pipenv_environment: ## 🗑️  deactivate and remove pipenv environment 🗑️
	@echo ">>> deactivating environment"
	exit
	@echo ">>> removing environment"
	pipenv --rm

fungi_grow: $(DATASET) ## 🍄 generate dataset 🍄
#, you can pass arguments as follows: make ARGS="--foo 10 --bar 20" generate-dataset
$(DATASET):
	@echo ">>> generating dataset"
	python ./src/secondary_data_gen.py $(ARGS)

train: ## 🧠 train the model 🧠
#, you can pass arguments as follows: make ARGS="--foo 10 --bar 20" train
	@echo ">>> training model"
	pipenv run python "./train.py"

deploy: ## 💁 serve trained model with a REST API
	@echo ">>> serving the trained model as a REST API in a docker container"
	pipenv run docker build -t fungi-incognita .
	pipenv run docker run -it --rm -p 9696:9696 fungi-incognita

test_deploy: ## 🧪 test the deployed model 🧪
	@echo ">>> testing the deployed model"
	pipenv run python "./predict_test.py"

# run-pipeline: install clean_conda_environment generate-dataset train serve  ## install dependencies -> clean artifacts -> generate dataset -> train -> serve
#	FIXME: needs implementation

#lint: ## flake8 linting and black code style
#	@echo ">>> black files"
#	FIXME: needs implementation
#	black scripts ml_skeleton_py tests

#	@echo ">>> linting files"
#	FIXME: needs implementation
#	flake8 scripts ml_skeleton_py tests

# coverage: ## create coverage report
# 	@echo ">>> running coverage pytest"
# 	pytest --cov=./ --cov-report=xml

# test: ## run unit tests in the current virtual environment
# 	@echo ">>> running unit tests with the existing environment"
# 	pytest

# test-docker: ## run unit tests in docker environment
# 	@echo ">>> running unit tests in an isolated docker environment"
# 	docker-compose up test

help: ## ❓ show help on available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'