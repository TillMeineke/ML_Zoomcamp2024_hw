# CheatSheet: Dependency Management Tools for Python

## Pyenv

### Installation

Install via Homebrew
`brew install pyenv`

### Useful Commands

- Install a new Python version. `pyenv install 3.8.9`
- Set global Python version. `pyenv global 3.8.9`
- Set local Python version (for a project directory). `pyenv local 3.8.9`

## Poetry

### Installation

1. Install Poerty

```
curl -sSL https://install.python-poetry.org | python3 -
```

or

```
pip install poetry
```

2. Add Poetry's bin directory (/Users/<user>/.local/bin) in your `PATH`
   environment variable.

```
export PATH="/Users/<user>/.local/bin:$PATH"
```

3. Verify that it worked

```
poetry --version
```

### Useful Commands

- Create a new project. `poetry init -n`
- Create a new project with specific Python version. `poetry init --dependency="python:^3.9" --no-interaction` or edit `pyproject.toml`
- Activate the environment in a new subshell. `poetry shell`
- Run a script with the environment. `poetry run python main.py`
- Deactivate the environment / exit the subshell. `exit`
- Add dependency. `poetry add <dependency>`
- Add dependency to a group. `poetry add <dependency> --group <group>`
- Remove dependency. `poetry remove <dependency>`
- Get information about the current environment. `poetry env info`
- Make virtual environment part of project folder. `poetry config virtualenvs.in-project true`
- See active environments. `poetry env list`
- Remove virtual environment. `poetry env remove <environment>` or `rm -rf .venv`

## Pipenv

### Installation

1. Install Pipenv

```
pip install pipenv --user
```

or

```
brew install pipenv
```

### Useful Commands

- Create a new project. `pipenv`
- Create a new project with specific Python version. `pipenv --python=3.8.9` or edit `Pipfile`
- Setup environment using an existing Pipfile. `pipenv install`
- Activate the environment in a new subshell. `pipenv shell`
- Run a script with the environment. `pipenv run python main.py`
- Deactivate the environment / exit the subshell. `exit`
- Add dependency. `pipenv install <dependency>`
- Add dev dependency. `pipenv install <dependency> --dev`
- Remove dependency. `pipenv uninstall <dependency>`
- Make virtual environment part of project folder. `export PIPENV_VENV_IN_PROJECT=1`
- Remove virtual environment. `pipenv --rm` or `rm -rf .venv`

## Basic Example Workflows

### pyenv + pip + venv + pip-tools

```bash
# install desired python version
pyenv install 3.8.6

# set python version for project directory
pyenv local 3.8.6

# create a virtual environment
python -m venv .venv

# activate the environment
source .venv/bin/activate

# install pip-tools
pip install pip-tools

# create a requirements.in file
echo "requests" >> requirements.in

# compile the requirements.in file to create requirements.txt
pip-compile requirements.in

# install dependencies
pip install -r requirements.txt
```

### Pipenv + pyenv

```bash
# install desired python version
pyenv install 3.8.6

# set python version for project directory
pyenv local 3.8.6

# create new project
pipenv --python=3.8.6

# install dependencies
pipenv install requests

# activate shell
pipenv shell
```

### Poetry + pyenv

```bash
# install desired python version
pyenv install 3.8.6

# set python version for project directory
pyenv local 3.8.6

# create new project
poetry init -n

# install dependencies
poetry add requests
# activate shell

poetry shell
```
