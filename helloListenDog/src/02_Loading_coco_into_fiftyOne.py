# Load a COCO dataset into FiftyOne
# voxel51 on DTC-YT: https://www.youtube.com/watch?v=gditgUhTmVs

import fiftyone as fo
import json
import os

labels_path = "../data/helloListenDog_v1_dog_detection.v1i.coco/images/test/_annotations.coco.json"
images_dir = "../data/helloListenDog_v1_dog_detection.v1i.coco/images/test"

name = "helloDog1"

# Load the COCO annotations
with open(labels_path) as f:
    data = json.load(f)

# Print the image paths being checked
for img in data["images"]:
    img_path = os.path.join(images_dir, img["file_name"])
    print(f"Checking image path: {img_path}")

# Create the FiftyOne dataset
dataset = fo.Dataset.from_dir(
    name=name,
    dataset_type=fo.types.COCODetectionDataset,
    labels_path=labels_path,
    data_path=images_dir,  # Ensure this is the path where images are stored
)

print(dataset)

# https://docs.voxel51.com/environments/index.html#notebooks

# Launch a new App session
session = fo.launch_app(dataset)

session.view = dataset.take(10)

# Replace active App instance with screenshot so App state is viewable offline
session.freeze()