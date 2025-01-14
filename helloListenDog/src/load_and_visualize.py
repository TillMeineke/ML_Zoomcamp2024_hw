# usage
# python load_and_visualize.py

# import the necessary libraries
from imagesearch import config
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision import transforms
import matplotlib.pyplot as plt
# import numpy as np
import torch

def visualize_batch(batch, classes, dataset_type):
    # initialize a figure
    fig = plt.figure(f"{dataset_type} batch",
                     figsize=(config.BATCH_SIZE, config.BATCH_SIZE))

    # loop over the images in the batch
    for i in range(0, config.BATCH_SIZE):
        # create a subplot
        ax = plt.subplot(2, 4, i+1)

        # grab image, convert it from channels first ordering to
        # channels last ordering, and scale the raw pixel intensities
        # to the range [0, 255]
        image = batch[0][i].cpu.numpy()
        image = image.transpose((1, 2, 0))
        image = (image * 255).astype("uint8")

        # grab label id and get the label from the classes list
        idx = batch[1][i]
        label = classes[idx]

        # show the image along with label
        plt.imshow(image)
        plt.title(label)
        plt.axis("off")

    # show the plot
    plt.tight_layout()
    plt.show()

# initialize our data augmentation functions
resize = transforms.Resize((config.INPUT_HEIGHT, config.INPUT_WIDTH))
hFlip = transforms.RandomHorizontalFlip(p=0.25)
vFlip = transforms.RandomVerticalFlip(p=0.25)
rotate = transforms.RandomRotation(degrees=15)

# initialize the training and validation data augmentation pipeline
trainTransforms = transforms.Compose([resize, hFlip, vFlip, rotate, transforms.ToTensor()])
valTransforms = transforms.Compose([resize, transforms.ToTensor()])

# initialize the training and validation datasets
print("[INFO] loading training and validation datasets...")
trainDataset = ImageFolder(root=config.TRAIN, transform=trainTransforms)
valDataset = ImageFolder(root=config.VAL, transform=valTransforms)
print(f"[INFO] training dataset contains {len(trainDataset)} images.")
print(f"[INFO] validation dataset contains {len(valDataset)} images.")

# create training and validation set dataloaders
print("[INFO] creating training and validation dataloaders...")
trainDataLoader = DataLoader(trainDataset, batch_size=config.BATCH_SIZE, shuffle=True)
valDataLoader = DataLoader(valDataset, batch_size=config.BATCH_SIZE, shuffle=False)

# grab a batch of from both training and validation dataloader
trainBatch = next(iter(trainDataLoader))
valBatch = next(iter(valDataLoader))

# visualize the training and validation set batches
print("[INFO] visualizing training and validation batch...")
visualize_batch(trainBatch, trainDataset.classes, "train")
visualize_batch(valBatch, valDataset.classes, "val")