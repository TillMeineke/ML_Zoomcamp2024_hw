import os
import json


def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)


def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def process_json_files(json_folder, output_file):
    """
    Process JSON files in the given folder and merge their annotations.
    """
    combined_data = {
        "licenses": [],
        "info": {},
        "categories": [],
        "images": [],
        "annotations": [],
    }
    image_id = 1
    annotation_id = 1
    cat_name_map = {}

    # Process each JSON file in the folder
    for json_file in os.listdir(json_folder):
        if not json_file.endswith(".json"):
            continue

        json_path = os.path.join(json_folder, json_file)
        data = load_json(json_path)

        # Extract categories (labels)
        for shape in data.get("shapes", []):
            label = shape["label"]
            if label not in cat_name_map:
                new_cat_id = len(cat_name_map) + 1
                cat_name_map[label] = new_cat_id
                combined_data["categories"].append({"id": new_cat_id, "name": label})

        # Add image information
        combined_data["images"].append(
            {
                "id": image_id,
                "file_name": data["imagePath"],
                "width": data["imageWidth"],
                "height": data["imageHeight"],
            }
        )

        # Add annotations
        for shape in data.get("shapes", []):
            points = shape["points"]
            x_min = min(points[0][0], points[1][0])
            y_min = min(points[0][1], points[1][1])
            x_max = max(points[0][0], points[1][0])
            y_max = max(points[0][1], points[1][1])

            combined_data["annotations"].append(
                {
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": cat_name_map[shape["label"]],
                    "bbox": [x_min, y_min, x_max - x_min, y_max - y_min],
                    "area": (x_max - x_min) * (y_max - y_min),
                    "iscrowd": 0,
                }
            )
            annotation_id += 1

        image_id += 1

    # Save the combined annotations to the output file
    save_json(combined_data, output_file)


def main():
    """
    Main function to execute the script.
    This script processes multiple JSON files from a single folder
    and combines their data into a COCO-style dataset.
    """
    json_folder = input("Enter the path to the folder containing JSON files: ")
    output_file = input(
        "Enter the path to the output file (e.g., combined_coco.json): "
    )

    # Process JSON files
    process_json_files(json_folder, output_file)


if __name__ == "__main__":
    main()
