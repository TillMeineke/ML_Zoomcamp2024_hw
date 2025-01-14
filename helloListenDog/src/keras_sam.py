# https://github.com/keras-team/keras-hub
# https://keras.io/keras_hub/guides/segment_anything_in_keras_hub/

# import os
# os.environ["KERAS_BACKEND"] = "tensorflow"  # Or "jax" or "torch"!

# !!pip install -Uq git+https://github.com/keras-team/keras-hub.git
# !!pip install -Uq keras

import platform
import sys

print(f"Python Version: {sys.version}")
print(f"Python Platform: {platform.platform ()}")
print()

import pandas as pd
import numpy as np

print(f"Pandas Version: {pd.__version__}")
print(f"NumPy Version: {np.__version__}")

import sklearn as sk
import scipy as sp

print(f"Scikit-Learn Version: {sk.__version__}")
print(f"SciPy Version: {sp.__version__}")
print()

import tensorflow as tf
import keras
import torch

print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {keras.__version__}")

# Check if GPU for Tensorflow/Keras is available
gpu = len(tf.config.list_physical_devices()) > 0
print("GPU is", "available" if gpu else "NOT AVAILABLE")
print()

print(f"PyTorch version: {torch.__version__}")

# Check PyTorch has access to MPS (Metal Performance Shader, Apple's GPU architecture)
print(f"Is MPS (Metal Performance Shader) built? {torch.backends.mps.is_built()}")
print(f"Is MPS available? {torch.backends.mps.is_available()}")

import matplotlib.pyplot as plt

# import tensorflow.keras as keras

import keras_hub
from keras import ops
import timeit

