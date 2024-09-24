# Setting up the Environment for ML Zoomcamp 2024

21.09.2024

We need for the course:

- [Python 3.11](https://docs.python.org/3.11/ "Python 3.11 Docs") (note that videos use 3.8)
- [NumPy 1.26.4 Release date: 5 Feb, 2024](https://numpy.org "NumPy") (NumPy 2 only works with Python 3.13), [pandas 2.2.3 Release date: 20 Sep 20, 2024](https://pandas.pydata.org "pandas") and [scikit-learn 1.5.2 Release date: Sep, 2024](https://scikit-learn.org/stable/ "scikit-learn") (latest available versions)
- [matplotlib 3.9.2 Release date: 12 Aug, 2024)](https://matplotlib.org "matplotlib") and [seaborn 0.13.2 Jan, 2024)](https://seaborn.pydata.org "Seaborn")
- [Jupyter notebooks](https://jupyter.org "Jupyter notebooks")

In this section, I'll describe how I prepared my local and remote environments for the course.

## Setup Conda Environment on MacBook 13", M1, 2020, 16GB  with Apple Silicon (arm64) running on Sonoma 14.6.1

I use a MacBook Pro 13" with Apple Silicon (arm64) and VSCode as my main editor. I use Conda as my environment manager and created a dedicated environment for the course. I also installed some additional software that I find useful, but that is described in a separate [post](./01_setup_macBook.md "Setup MacBook"). I know macOS 15 was just released, but I prefer to wait a bit before upgrading my system.

- First install [🍺 Homebrew](https://brew.sh "🍺 Homebrew") as a package manager for macOS, in `Terminal.app` run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install  `iterm2`, `miniforge`, `visual-studio-code` and `zoom` as your basic requirements:

```bash
brew install iterm2 miniforge visual-studio-code zoom
```

Caveat: brew install conflict with docker desktop and command line tools. You need to install docker desktop first and then the command line tools. [Issue](https://github.com/Homebrew/brew/issues/16309)

- When installing docker with brew, if you want to install [docker desktop](https://www.docker.com/products/docker-desktop/), you need to run the following command:

```bash
brew install --cask docker
```

- Then install the following packages:

```bash
brew install docker docker-compose
```

### [iTerm2](https://iterm2.com "iTerm2")

I use iTerm2 as my terminal emulator and installed [Oh My Zsh](https://ohmyz.sh "Oh My Zsh") as plugin manager for zsh. I also installed some plugins and themes that I find useful, but I`ll describe this in a separate [post](./02_setup_iterm2.md "Setup iTerm").

### [Miniforge](https://github.com/conda-forge/miniforge)

This is a minimal installer for Conda specific to conda-forge. It is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others. I created a dedicated [environment.yml](../../environment.yml) for the course.

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
- [Flask](https://flask.palletsprojects.com/en/3.0.x/), [gunicorn](https://gunicorn.org), [grpcio](https://grpc.io), [requests](https://docs.python-requests.org/en/latest/index.html), [tqdm](https://tqdm.github.io)
- [black](https://black.readthedocs.io/en/stable/index.html), [isort](https://pycqa.github.io/isort/), [pylint](https://www.pylint.org), [ruff]()
<!-- ! TODO:- [pytest] still missing -->

Tensorflow and [PyTorch](https://developer.apple.com/metal/pytorch/) are installed with Metal GPU support for Apple Silicon (arm64) Macs. You can test the installation with this [notebook](./apple_metal_test_env.ipynb)

For me the output looks like this, so everything is installed correctly:

```plaintext
Python 3.11.10 | packaged by conda-forge | (main, Sep 22 2024, 14:11:13) [Clang 17.0.6 ]
Python Platform: macOS-14.6.1-arm64-arm-64bit

Pandas 2.2.2
NumPy 1.26.4
Scikit-Learn 1.5.1
SciPy 1.14.1

Tensor Flow Version: 2.14.0
Keras Version: 2.14.0
GPU is available

PyTorch version: 2.4.1
Is MPS (Metal Performance Shader) built? True
Is MPS available? True
Using device: mps
```

FIXME:
I still need to test the installation of the other libraries required for the course later.

- [ ] pipenv
- [ ] poetry
- [ ] 

### [Visual Studio Code](https://code.visualstudio.com "Visual Studio Code")

I use VSCode as my main editor and installed some extensions that I find useful, but I`ll describe this in a separate [post](./03_setup_vscode.md).

### [Zoom](https://zoom.us "Zoom")

Well, this is called ML_Zoomcamp, so I installed Zoom for the course, although it is not needed for the course itself. But as suggested in the course, there are slack channels and a telegram group for communication. So I installed [Slack](https://slack.com "Slack") and [Telegram](https://telegram.org "Telegram") as well.

```bash
brew install slack telegram
```

## Ubuntu 24.04 on AWS EC2

Also I created an Ubuntu 24.04 x86_64 instance on AWS EC2 with a conda environment for the course and setup port forwarding to access Jupyter server with VSCode (Remote-SSH).

The video suggested installing Ubuntu 22.04, but I prefer to use the latest LTS version.

Hopefully I will not run into problems with running code locally on Apple Silicon (arm64) and remotely on x86_64. But as pointed out in the video, I can create an arm64 instance on AWS as well.

I'm wondering if there is a more convenient way to connect to the Jupyter server without copying the IP address manually into the `.ssh/config`. If you have any simple suggestion please let me know.

## Other Cloud Environments

Last I have accounts for [kaggle](https://www.kaggle.com/ "kaggle") and [Google Colab](https://colab.research.google.com/ "Google Colab") for running notebooks in the cloud.
