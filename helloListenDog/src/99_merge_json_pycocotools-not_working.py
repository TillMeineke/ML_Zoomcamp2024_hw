# not full working code
# outputfile is not correct

import os
import json
from pycocotools.coco import COCO

def merge_coco_json(files):
    # Initialize an empty COCO dataset
    merged_coco = {
        "info": [],
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": [],
        "filenames": [],  # Add a new field for filenames
        "version": "",
        "flags": {},
        "shapes": [],
        "imagePath": "",
        "imageData": None,
        "imageHeight": 0,
        "imageWidth": 0,
        "text": ""
    }

    # Iterate over each input file
    for file in files:
        with open(file, "r") as f:
            coco_data = json.load(f)
            merged_coco["images"].extend(coco_data.get("images", []))
            merged_coco["annotations"].extend(coco_data.get("annotations", []))
            merged_coco["filenames"].append(file)  # Add the filename to the list
            merged_coco["version"] = coco_data.get("version", merged_coco["version"])
            merged_coco["flags"].update(coco_data.get("flags", {}))
            merged_coco["shapes"].extend(coco_data.get("shapes", []))
            merged_coco["imagePath"] = coco_data.get("imagePath", merged_coco["imagePath"])
            merged_coco["imageData"] = coco_data.get("imageData", merged_coco["imageData"])
            merged_coco["imageHeight"] = coco_data.get("imageHeight", merged_coco["imageHeight"])
            merged_coco["imageWidth"] = coco_data.get("imageWidth", merged_coco["imageWidth"])
            merged_coco["text"] = coco_data.get("text", merged_coco["text"])

    # Create a new COCO object
    merged_coco_obj = COCO()
    merged_coco_obj.dataset = merged_coco
    merged_coco_obj.createIndex()

    return merged_coco_obj


# List of all "*.json" in "../data/renamed_dub_removed" directory
coco_files = []
for root, dirs, files in os.walk("../data/renamed_dub_removed"):
    for file in files:
        if file.endswith(".json"):
            coco_files.append(os.path.join(root, file))


# Merge the COCO JSON files
merged_coco_obj = merge_coco_json(coco_files)

# Specify the output path
output_path = "../data/merged_coco.json"

# Save the merged COCO JSON to the output path
with open(output_path, "w") as f:
    json.dump(merged_coco_obj.dataset, f)
