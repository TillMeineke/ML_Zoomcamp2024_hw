import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math
print(f"Torch version: {torch.__version__}")
print(f"Torchvision version: {torchvision.__version__}")

# Let us write PyTorch code that works on both GPU (using CUDA) and CPU.
# It is often called "model-agnostic" because it allows your model to run on
# either GPU or CPU without changing the rest of the code.
# check if mps or cuda is available and set device globally
if torch.mps.is_available():
    print("MPS is available")
    device = torch.device("mps")
elif torch.cuda.is_available():
    print("CUDA is available")
    device = torch.device("cuda")
else:
    print("No GPU available, using CPU instead.")
    device = torch.device("cpu")

# create a tensor
x = torch.rand(2,2)
y = torch.rand(2,2)
print(x)
print(y)

# addition
# z = x + y
z = torch.add(x, y)
print(z)

# works for subtraction, multiplication, division
# u = x-y
u = torch.sub(x, y)
print(u)

# v = x * y
v = torch.mul(x, y)
print(u)

# w = x / y
w = torch.div(x, y)
print(w)

# Slicing
x = torch.rand(5, 3)
print(x)
print(x[:, 0]) # all rows, column 0
print(x[1, :]) # row 1, all columns
print(x[1, 1]) # element at row 1, column 1

# Reshaping
x = torch.rand(4, 4)
y = x.view(16)
z = x.view(-1, 8) # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

# item() to get a Python number from a tensor containing a single value
x = torch.rand(1)
print(x)
print(x.item())

# Converting a Torch Tensor to a NumPy Array
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
print(type(b))

# See how the numpy array changed in value.
a.add_(1)
print(a)
print(b)

# Converting NumPy Array to Torch Tensor
a = np.ones(5)
print(a)
b = torch.from_numpy(a)
print(b)

a += 1
print(a)
print(b)

# MPS tensors
x = torch.randn((2, 2), device=device)
print(x.device)

x.to("cpu").numpy()

# Autograd
x = torch.randn(2, 2, requires_grad=True)
print(x)

y = x + 2
print(y)

z = y * y * 3
print(z)
z = z.mean()
print(z)

z.backward() # Vector-Jacobian product
print(x.grad)

# x.requires_grad_(False)
# x.detach()
with torch.no_grad():
    y = x + 2
    print(y)

# for gradients to be zeroed
weights = torch.ones(4, requires_grad=True)

for epoch in range(3):
    model_output = (weights*3).sum()
    model_output.backward()
    print(weights.grad)
    weights.grad.zero_()

# Optimizer
optimizer = torch.optim.SGD([weights], lr=0.01)
optimizer.step()
optimizer.zero_grad()

# Backpropagation
# Chain rule
# Computational graph
# Local gradients -> Loss function
# Three steps:
# 1. Forward pass: compute loss
# 2. Compute local gradients
# 3. Backward pass: compute dL/dw using chain rule

import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torch.optim import Adam

#`torchvision. transforms.v2` is an extension of the `torchvision.transforms`
# module, designed to provide more flexible and advanced data augmentation and
# preprocessing utilities in PyTorch, particularly for computer vision tasks.
# For example, resizing, normalizing, and flipping images and tensors.

import torchvision
import torchvision.transforms.v2 as transforms
import torchvision.transforms.functional as F
import matplotlib.pyplot as plt

################################################################################
#Part 1: Preparing Data

# Torchvision provides many built-in datasets in the torchvision.datasets module
# (https://pytorch.org/vision/0.20/auto_examples/transforms/plot_transforms_getting_started.html#sphx-glr-auto-examples-transforms-plot-transforms-getting-started-py)

from pathlib import Path
import torch
import torch.utils.data
from torchvision import models, datasets, tv_tensors

import matplotlib.pyplot as plt
plt.rcParams["savefig.bbox"] = 'tight'

from torchvision.transforms import v2
from torchvision.io import decode_image

torch.manual_seed(42)

ROOT = Path("../data/helloListenDog_v1_dog_detection.v1i.coco")
IMAGES_PATH = str(ROOT / "images/test")
ANNOTATIONS_PATH = str(IMAGES_PATH + r"/_annotations.coco.json")

from helpers import plot
import pycocotools
dataset = datasets.CocoDetection(IMAGES_PATH, ANNOTATIONS_PATH)

sample = dataset[0]
img, target = sample
print(f"{type(img) = }\n{type(target) = }\n{type(target[0]) = }\n{target[0].keys() = }")

dataset = datasets.wrap_dataset_for_transforms_v2(dataset, target_keys=("boxes", "labels"))

# print classes
# print(dataset.coco.cats[1]["name"])
classes = [dataset.coco.cats[k]["name"] for k in dataset.coco.cats]

# format classes as dict for easy lookup 1: "..."
classes = {k: v for k, v in enumerate(classes)}

sample = dataset[0][1]["boxes"]
img, target = sample
label = target["labels"]
# lookup class name
print(classes[label])

print(f"{type(img) = }\n{type(target) = }\n{target.keys() = }")
print(f"{type(target['boxes']) = }\n{type(target['labels']) = }")

plot([dataset[0], dataset[1], dataset[2]])
# print([target['labels'], target['boxes']])
# print boxes and labels for each picture
for i in range(0, 3):
    print(dataset[i][1]["boxes"])

    # print(dataset[i][1]["labels"])
    # match labels with classes
    print([classes[i] for i in dataset[i][1]["labels"].int().numpy()])





# print([classes[i] for i in target['labels']])

'''
rootPath = "../data/helloListenDog_v1_dog_detection.v1i.coco"

imagePath = "/images/test"
fullImagePath = rootPath + imagePath
imageFilename = "Image_2_jpg.rf.a29c195e5769db1d6109c6d3a38465ff.jpg"
img = decode_image(Path(fullImagePath) / (imageFilename))
print(f"{type(img) = }, {img.dtype = }, {img.shape = }")
'''







# Basics

transform = v2.RandomCrop(size=(224, 224))
out = transform(img)

plot([img, out])

# Image classification - A basic pipeline

transforms = v2.Compose([
    v2.RandomResizedCrop(size=(224, 224), antialias=True),
    v2.RandomHorizontalFlip(p=0.5),
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
out = transforms(img)

plot([img, out])

# Detection, Segmentation, Videos

# The new Torchvision transforms in the `torchvision.transforms.v2` namespace
# support tasks beyond image classification: they can also transform bounding
# boxes, segmentation / detection masks, or videos.

# Let’s briefly look at a detection example with bounding boxes.

from torchvision import tv_tensors  # we'll describe this a bit later, bare with us

# boxes = tv_tensors.BoundingBoxes(
#     [
#         [15, 10, 370, 510],
#         [275, 340, 510, 510],
#         [130, 345, 210, 425]
#     ],
#     format="XYXY", canvas_size=img.shape[-2:])

labelPath = "/labels/test"
fullLabelPath = rootPath + labelPath
labelFilename = "Image_2_jpg.rf.a29c195e5769db1d6109c6d3a38465ff.txt"

# read the bounding boxes from the file
boxes = np.loadtxt(Path(fullLabelPath) / (labelFilename)).reshape(-1, 5)[:, 1:]
print(f"{type(boxes) = }, {boxes.shape = }")
# convert the bounding boxes to tvtensors
boxes = tv_tensors.BoundingBoxes(boxes, "XYWH", "XYXY")

# read the class labels from the file
class_id = np.loadtxt(Path(fullLabelPath) / (labelFilename)).reshape(-1, 5)[:, 0]




transforms = v2.Compose([
    v2.RandomResizedCrop(size=(224, 224), antialias=True),
    v2.RandomPhotometricDistort(p=1),
    v2.RandomHorizontalFlip(p=1),
])
out_img, out_boxes = transforms(img, boxes)
print(type(boxes), type(out_boxes))

plot([(img, boxes), (out_img, out_boxes)])

# In PyTorch, `torchvision.transforms.functional.to_tensor` is a function that
# converts a given image (in the form of a PIL Image or NumPy array) into a
# PyTorch tensor.

image_tensor = F.to_tensor(image)

# Implementing dataset
class DogDataset(Dataset):
    def __init__(self):
        # data loading
        xy = np.loadtxt()
        
    def __getitem__(self, index):
        # return data and label
        # dataset[0]

    def __len__(self):
        # return size of dataset
        # len(dataset)


# https://christianjmills.com/posts/torchvision-coco-annotation-tutorials/bounding-boxes/
# Working with COCO Bounding Box Annotations in Torchvision