import re


def clean_vtt(vtt_content):
    # Split the content by lines
    lines = vtt_content.splitlines()

    # Initialize a variable to store the cleaned text
    cleaned_text = []

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
            cleaned_line = re.sub(r"<.*?>", "", line)
            cleaned_text.append(cleaned_line)

    # Join the lines into a single string
    return " ".join(cleaned_text)


# Example usage
vtt_content = """
WEBVTT
Kind: captions
Language: en

00:00:00.320 --> 00:00:02.149 align:start position:0%
 
hello<00:00:00.719><c> everyone</c>

00:00:02.149 --> 00:00:02.159 align:start position:0%
hello everyone
 

00:00:02.159 --> 00:00:04.070 align:start position:0%
hello everyone
this<00:00:02.399><c> is</c><00:00:02.560><c> our</c><00:00:02.879><c> first</c><00:00:03.120><c> lesson</c><00:00:03.520><c> of</c><00:00:03.600><c> the</c><00:00:03.760><c> first</c>

00:00:04.070 --> 00:00:04.080 align:start position:0%
this is our first lesson of the first
 

00:00:04.080 --> 00:00:06.230 align:start position:0%
this is our first lesson of the first
session<00:00:04.560><c> of</c><00:00:04.720><c> machine</c><00:00:05.040><c> learning</c><00:00:05.279><c> zoom</c><00:00:05.520><c> camp</c>

00:00:06.230 --> 00:00:06.240 align:start position:0%
session of machine learning zoom camp
"""

cleaned_text = clean_vtt(vtt_content)
print(cleaned_text)
