
# Setting up the Environment

21.09.2024

We need for the course:

- [Python 3.11](https://docs.python.org/3.11/ "Python 3.11 Docs") (note that videos use 3.8)
- [NumPy](https://numpy.org "NumPy"), [pandas](https://pandas.pydata.org "pandas") and [scikit-learn](https://scikit-learn.org/stable/ "scikit-learn") (latest available versions)
- [matplotlib](https://matplotlib.org "matplotlib") and [seaborn](https://seaborn.pydata.org "Seaborn")
- [Jupyter notebooks](https://jupyter.org "Jupyter notebooks")

In this section, I'll describe how I prepared my local and remote environments for the course.

## Setup MacBook

I use a MacBook Pro 13" with Apple Silicon (arm64) and VSCode as my main editor. I use Conda as my package manager and created a dedicated environment for the course. I also installed some additional software that I find useful.

- First install [🍺 Homebrew](https://brew.sh) as a package manager, in `Terminal.app` run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install  `miniforge`, `visual-studio-code`, `zoom`

```bash
brew install miniforge visual-studio-code zoom
```

[Miniforge](https://github.com/conda-forge/miniforge) is a minimal installer for Conda specific to conda-forge. It is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others. I created a dedicated [environment.yml](../environment.yml) for the course.

To create this `ML_Zoomcamp2024` conda environment from the file run the following command in the folder containing this file:

```bash
conda env create -f environment.yml
```

Activate the environment with the following command:

```bash
conda activate ML_Zoomcamp2024
```

This installs the most important libraries for data science.

- Python=3.11
- NumPy, Pandas and Scikit-Learn (latest available versions)
- Matplotlib and Seaborn
- Jupiter notebooks

I also added some additional libraries (some needed for later in the course):

- PyTorch, Torchaudio, Torchvision,
- scipy, xgboost
- Tensorflow=2.14, Tensorflow-metal=1.1.0
- Flask, gunicorn, grpcio, requests, tqdm
- black, isort, pylint, ruff

Tensorflow and PyTorch are installed with Metal GPU support for Apple Silicon (arm64) Macs. Only working with Python<=3.11. You can test the installation with this [notebook](./apple_metal_test_env.ipynb)

Next to setup VSCode, I installed the following VSCode extensions:

- autoDocstring
- Black Formatter
- Code Spell Checker
- Docker
- Github Copilot
- isort
- Python Extension Pack
- Remote - SSH

### Optional: Install additional extensions

- Better Comments
- Code Runner
- colorize
- Data Wrangler
- Highlight Line
- indent-rainbow
- Material Icon Theme
- Markdown All in One
- Markdown PDF
- Markdown Preview Mermaid Support
- Path Intellisense
- Prettier - Code formatter
- Prettier SQL VSCode
- Python Indent
- Rainbow CSV
- TODO Highlight
- Todo Tree
- Trailing Spaces
- vscode-pdf

### Optional: Install additional software

- Install
  - `bat`: syntax highlighting for cat
  - `eza` or `lsd`: for a modern `ls` replacement
  - `fzf`: fuzzy search
  - `zsh-autosuggestions`, `zsh-syntax-highlighting`: zsh shell plugins for command suggestions and syntax highlighting
  - `font-hack-nerd-font`: a nice font in the terminal
  - `iterm2`: a better terminal
  - `dbeaver-community`: a database client
  - `tableau-public`: for data visualization
  - `keycastr`: for showing key presses
  - `rectangle`: for window management
  - `libreoffice` and `libreoffice-language-pack`: a free office suite
  - `slack` and `telegram`: for communication

## Ubuntu 24.04 on AWS EC2

Also I created an Ubuntu 24.04 instance on AWS EC2 with a conda environment for the course and setup port forwarding to access Jupyter server with VSCode (Remote-SSH).

Last I have accounts for [kaggle](https://www.kaggle.com/ "kaggle") and [Google Colab](https://colab.research.google.com/ "Google Colab") for running notebooks in the cloud.