
## Setting up the Environment

In this section, we'll prepare the environment

We need for the course:

- Python 3.11 (note that videos use 3.8)
- NumPy, Pandas and Scikit-Learn (latest available versions)
- Matplotlib and Seaborn
- Jupyter notebooks

On computer with Apple Silicon (arm64) use:
- Homebrew as package manager, in terminal-app run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install  `miniforge`, `visual-studio-code`, `zoom`

```bash
brew install miniforge visual-studio-code zoom
```

[Miniforge](https://github.com/conda-forge/miniforge) is a minimal installer for Conda specific to conda-forge. It is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others. I created a dedicated [environment.yml](../environment.yml) for the course.

To create this conda environment `ML_Zoomcamp2024` from the file run the following command in the folder with this file:

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

Tensorflow and PyTorch are installed with Metal support for Apple Silicon (arm64) Macs. Only working with Python<=3.11. You can test the installation with this [notebook](./apple_metal_test_env.ipynb)

VSCode extensions:

- autoDocstring
- Better Comments
- Black Formatter
- Code Runner
- Code Spell Checker
- colorize
- Data Wrangler
- Docker
- Highlight Line
- indent-rainbow
- Python Extension Pack
- Rainbow CSV
- TODO Highlight
- Todo Tree
- Trailing Spaces
- vscode-pdf
- Remote - SSH

## Optional: Install additional software

- Install
  - `bat`: syntax highlighting for cat
  - `eza` or `lsd`: for a modern `ls` replacement
  - `fzf`: for fuzzy search
  - `zsh-autosuggestions`, `zsh-syntax-highlighting`: zsh shell plugins for command suggestions and syntax highlighting
  - `font-hack-nerd-font`: for a nice font in the terminal
  - `iterm2`: for a better terminal
  - `dbeaver-community`: for a database client
  - `keycastr`: for showing key presses
  - `libreoffice` and `libreoffice-language-pack`: for a free office suite
  - `slack` and `telegram`: for communication