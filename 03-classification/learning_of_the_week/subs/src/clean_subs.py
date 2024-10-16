import os
import re


def clean_vtt(vtt_content):
    # Split the content by lines
    lines = vtt_content.splitlines()

    # Initialize a variable to store the cleaned text
    cleaned_text = []
    previous_line = None

    # Regex to match timestamps
    timestamp_regex = r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}"

    # Loop through lines and filter out timestamps and empty lines
    for line in lines:
        # Remove lines with timestamps or metadata (e.g., "WEBVTT", "Kind: captions")
        if (
            not re.match(timestamp_regex, line)
            and "align:" not in line
            and line.strip()
        ):
            # Clean inline tags (like <c>)
            cleaned_line = re.sub(r"<.*?>", "", line).strip()

            # Add line only if it's not a duplicate of the previous one
            if cleaned_line != previous_line:
                cleaned_text.append(cleaned_line)
                previous_line = cleaned_line

    # Join the lines into a single string
    return " ".join(cleaned_text)


def process_directory(vtt_dir, output_dir):
    # Check if output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the directory
    for filename in os.listdir(vtt_dir):
        # Only process .vtt files
        if filename.endswith(".vtt"):
            vtt_path = os.path.join(vtt_dir, filename)

            # Read the .vtt file content
            with open(vtt_path, "r", encoding="utf-8") as file:
                vtt_content = file.read()

            # Clean the VTT content
            cleaned_text = clean_vtt(vtt_content)

            # Define the output .txt file path
            output_filename = filename.replace(".vtt", ".txt")
            output_path = os.path.join(output_dir, output_filename)

            # Write the cleaned text to a .txt file
            with open(output_path, "w", encoding="utf-8") as output_file:
                output_file.write(cleaned_text)

            print(f"Processed: {filename} -> {output_filename}")


# Example usage
vtt_directory = "./raw_subs"  # Replace with your directory path
output_directory = (
    "./clean_subs"  # Replace with your desired output directory
)

process_directory(vtt_directory, output_directory)
