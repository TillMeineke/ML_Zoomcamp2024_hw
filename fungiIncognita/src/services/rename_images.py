from bs4 import BeautifulSoup
import os
from pathlib import Path
import re


def clean_filename(title):
    # Remove special characters and spaces, replace with underscores
    cleaned = re.sub(r"[^\w\s-]", "", title)
    return cleaned.strip().replace(" ", "_")


def rename_images_from_html(html_file, images_dir):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

        # Get title from the HTML file
        title = soup.find("title").text
        cleaned_title = clean_filename(title)

        # Find all img tags
        images = soup.find_all("img")

        # Counter for multiple images
        for index, img in enumerate(images, 1):
            old_filename = os.path.basename(img["src"])
            extension = os.path.splitext(old_filename)[1]

            # Create new filename with index
            new_name = f"{cleaned_title}_{index}{extension}"

            old_path = os.path.join(images_dir, old_filename)
            new_path = os.path.join(images_dir, new_name)

            if os.path.exists(old_path):
                print(f"Renaming {old_filename} to {new_name}")
                os.rename(old_path, new_path)


# Process multiple HTML files
def process_all_html_files(html_dir, images_dir):
    for html_file in sorted(Path(html_dir).glob("*.html")):
        print(f"\nProcessing {html_file.name}")
        rename_images_from_html(html_file, images_dir)


# Usage example
if __name__ == "__main__":
    html_dir = './text'
    images_dir = './Images'
    process_all_html_files(html_dir, images_dir)
