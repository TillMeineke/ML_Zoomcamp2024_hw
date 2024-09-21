
## Setting up the Environment

In this section, we'll prepare the environment

You need:

    Python 3.11 (note that videos use 3.8)
    NumPy, Pandas and Scikit-Learn (latest available versions)
    Matplotlib and Seaborn
    Jupyter notebooks

On computer with Apple Silicon use:
- Homebrew as package manager

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install bat, exa or lsd, fzf, zsh-autosuggestions, zsh-syntax-highlighting, dbeaver-community, font-hack-nerd-font, iterm2, keycastr, libreoffice, libreoffice-language-pack, miniforge, slack, tableau-public, visual-studio-code, zoom, 

```bash



-  Miniconda, iTerm2, Visual Studio Code, font-hack-nerd-font, Powerlevel10k, zsh, zsh-autosuggestions, zsh-syntax-highlighting, zsh-completions, 

```bash
brew install --cask miniconda iterm2 visual-studio-code
```



 [Miniconda]() create conda environment `ML_Zoomcamp2024` with the following command:

```bash
conda env create -f environment.yml
```

Activate the environment with the following command:

```bash
conda activate ML_Zoomcamp2024
```

This installs most important libraries (python=3.10 pandas, numpy, matplotlib, scipy, scikit-learn,  seaborn, tensorflow=2.14, xgboost, tensorflow-metal=1.1.0 ) for the course and needed for the homeworks.