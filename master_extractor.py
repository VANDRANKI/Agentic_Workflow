# master_extractor.py
import re
import argparse
import os
import sys

# Import the function from the other script
try:
    from image_details_extractor import get_image_details
except ImportError:
    print("Error: Could not import 'get_image_details' from 'image_details_extractor.py'.", file=sys.stderr)
    print("Ensure 'image_details_extractor.py' is in the same directory or Python path.", file=sys.stderr)
    sys.exit(1)

# Regular expression to find Markdown image syntax: ![alt text](path/to/image.ext)
# This regex captures the image path. It handles various path characters.
# It assumes the path doesn't contain ')' unless it's the closing parenthesis.
IMAGE_REGEX = re.compile(r"!\[.*?\]\((.*?)\)")

def find_image_paths(content: str, base_dir: str) -> list[str]:
    """Finds all image paths in the markdown content and resolves them relative to the base directory."""
    relative_paths = IMAGE_REGEX.findall(content)
    absolute_paths = []
    for rel_path in relative_paths:
        # Construct path relative to the markdown file's directory
        joined_path = os.path.join(base_dir, rel_path)
        # Normalize path separators (replace \ with /) and get absolute path
        normalized_path = os.path.normpath(joined_path).replace('\\', '/')
        abs_path = os.path.abspath(normalized_path)
        absolute_paths.append(abs_path)
    return absolute_paths

def process_file(file_path: str):
    """Reads a file, extracts image paths, and gets details for each image."""
    print(f"Processing file: {file_path}")

    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}", file=sys.stderr)
        return

    # Get the directory containing the markdown file to resolve relative image paths
    base_directory = os.path.dirname(file_path)

    image_paths = find_image_paths(content, base_directory)

    if not image_paths:
        print("No image paths found in the file.")
        return

    print(f"Found {len(image_paths)} image path(s):")
    for img_path in image_paths:
        print(f"- {img_path}")

        # --- Define the prompt for the image details extractor ---
        # This prompt should be tailored based on the specific information needed
        # For now, using a generic prompt. This could be made more dynamic.
        prompt_for_image = "Describe the content of this image in detail, focusing on any scientific data, graphs, or experimental setups shown."
        # ---

        print(f"  Requesting details for: {os.path.basename(img_path)}...")
        print(f"  Prompt: \"{prompt_for_image}\"")

        # Call the function from the other script
        details = get_image_details(img_path, prompt_for_image)

        if details:
            print("\n  --- Image Details ---")
            print(details)
            print("  ---------------------\n")
        else:
            print(f"  Failed to get details for {os.path.basename(img_path)}.\n")

def main():
    parser = argparse.ArgumentParser(description="Master extractor to read files and analyze images using OpenAI Vision.")
    parser.add_argument("input_file", help="Path to the input file (e.g., a Markdown file) to process.")
    args = parser.parse_args()

    # Check if the image extractor function is available
    if 'get_image_details' not in globals():
        print("Exiting due to missing 'get_image_details' function.", file=sys.stderr)
        return # Already printed error in the import block

    process_file(args.input_file)

if __name__ == "__main__":
    main()
