
# Setting up the Environment

21.09.2024

We need for the course:

- [Python 3.11](https://docs.python.org/3.11/ "Python 3.11 Docs") (note that videos use 3.8)
- [NumPy](https://numpy.org "NumPy"), [pandas](https://pandas.pydata.org "pandas") and [scikit-learn](https://scikit-learn.org/stable/ "scikit-learn") (latest available versions)
- [matplotlib](https://matplotlib.org "matplotlib") and [seaborn](https://seaborn.pydata.org "Seaborn")
- [Jupyter notebooks](https://jupyter.org "Jupyter notebooks")

In this section, I'll describe how I prepared my local and remote environments for the course.

## Setup Conda Environment on MacBook with Apple Silicon (arm64)

I use a MacBook Pro 13" with Apple Silicon (arm64) and VSCode as my main editor. I use Conda as my environment manager and created a dedicated environment for the course. I also installed some additional software that I find useful, but that is described in a separate [post](./01_setup_macBook.md "Setup MacBook").

- First install [🍺 Homebrew](https://brew.sh "🍺 Homebrew") as a package manager for macOS, in `Terminal.app` run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install  `iterm2`, `miniforge`, `visual-studio-code` and `zoom`

```bash
brew install iterm2 miniforge visual-studio-code zoom
```
TODO
FIXME:
<!-- FIXME: docker missing -->

### [iTerm2](https://iterm2.com "iTerm2")

I use iTerm2 as my terminal emulator and installed [Oh My Zsh](https://ohmyz.sh "Oh My Zsh") as my shell. I also installed some plugins and themes that I find useful, but I`ll describe this in a separate [post](./02_setup_iterm2.md "Setup iTerm").

### [Miniforge](https://github.com/conda-forge/miniforge)

This is a minimal installer for Conda specific to conda-forge. It is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others. I created a dedicated [environment.yml](../environment.yml) for the course.

To create this `ML_Zoomcamp2024` conda environment from the file run the following command in the folder containing this file:

```bash
conda env create -f environment.yml
```

Activate the environment with the following command:

```bash
conda activate ML_Zoomcamp2024
```

This installs the most important libraries for data science and needed for the course:

- Python=3.11
- NumPy, Pandas and Scikit-Learn (latest available versions)
- Matplotlib and Seaborn
- Jupiter notebooks

I also added some additional libraries (some needed for later in the course):

- [PyTorch](https://pytorch.org), Torchaudio, Torchvision,
- [SciPy](https://scipy.org), [xgboost](https://xgboost.readthedocs.io/en/stable/)
- [Tensorflow=2.14](https://www.tensorflow.org), [Tensorflow-metal=1.1.0](https://developer.apple.com/metal/tensorflow-plugin/)
- [Flask], [gunicorn], [grpcio], [requests], [tqdm]
- [black], [isort], [pylint], [ruff]
<!-- ! TODO:- [pytest] still missing -->

Tensorflow and [PyTorch](https://developer.apple.com/metal/pytorch/) are installed with Metal GPU support for Apple Silicon (arm64) Macs. Only working with Python<=3.11. You can test the installation with this [notebook](./apple_metal_test_env.ipynb)

### [Visual Studio Code](https://code.visualstudio.com "Visual Studio Code")

I use VSCode as my main editor and installed some extensions that I find useful, but I`ll describe this in a separate [post](./03_setup_vscode.md).

### [Zoom](https://zoom.us "Zoom")

Well, this is called ML_Zoomcamp, so I installed Zoom for the course, although it is not needed for the course itself. But as suggested in the course, there are slack channels and a telegram group for communication. So I installed [Slack](https://slack.com "Slack") and [Telegram](https://telegram.org "Telegram") as well.

```bash
brew install slack telegram
```

## Ubuntu 24.04 on AWS EC2

Also I created an Ubuntu 24.04 instance on AWS EC2 with a conda environment for the course and setup port forwarding to access Jupyter server with VSCode (Remote-SSH).

## Other Cloud Environments

Last I have accounts for [kaggle](https://www.kaggle.com/ "kaggle") and [Google Colab](https://colab.research.google.com/ "Google Colab") for running notebooks in the cloud.