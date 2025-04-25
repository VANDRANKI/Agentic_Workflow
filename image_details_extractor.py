# image_details_extractor.py
import base64
import requests # Using requests as openai v1+ requires it for image URLs or base64
import os
import mimetypes
from openai import OpenAI
import sys

# --- Configuration ---
# Ensure your OpenAI API key is set as an environment variable:
# export OPENAI_API_KEY='your_api_key'
# If the environment variable is not set, uncomment and set it here (less secure):
# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"

try:
    client = OpenAI()
    # Check if the API key is actually configured
    if not client.api_key:
        raise ValueError("OpenAI API key is not configured. Set the OPENAI_API_KEY environment variable.")
except Exception as e:
    print(f"Error initializing OpenAI client: {e}", file=sys.stderr)
    print("Please ensure the OpenAI library is installed (`pip install openai`) and the API key is configured.", file=sys.stderr)
    client = None # Ensure client is None if initialization fails

# --- Helper Function ---
def encode_image_to_base64(image_path):
    """Encodes a local image file into base64 format."""
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}", file=sys.stderr)
        return None
    if not os.path.isfile(image_path):
        print(f"Error: Path provided is not a file: {image_path}", file=sys.stderr)
        return None

    try:
        # Guess the MIME type of the image
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type or not mime_type.startswith('image'):
            print(f"Warning: Cannot determine a valid image MIME type for {image_path}. Attempting to proceed.", file=sys.stderr)
            # Default or make a best guess if needed, e.g., 'image/png' or 'image/jpeg'
            # For simplicity, we'll let it proceed and OpenAI might handle it or error out.
            # A more robust solution might involve checking file headers.

        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            # Ensure the MIME type is included, default if necessary
            mime_type = mime_type if mime_type else 'image/png' # Defaulting to png if undetectable
            return f"data:{mime_type};base64,{encoded_string}"
    except Exception as e:
        print(f"Error encoding image {image_path}: {e}", file=sys.stderr)
        return None

# --- Main Function ---
def get_image_details(image_path: str, prompt: str) -> str | None:
    """
    Sends an image and a prompt to the OpenAI Vision API and returns the text response.

    Args:
        image_path: The local path to the image file.
        prompt: The text prompt describing what information to extract from the image.

    Returns:
        The text response from the OpenAI API, or None if an error occurs.
    """
    if not client:
        print("Error: OpenAI client is not initialized.", file=sys.stderr)
        return None

    base64_image = encode_image_to_base64(image_path)
    if not base64_image:
        return None # Error message already printed by encode_image_to_base64

    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Updated to use gpt-4o as requested
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": base64_image,
                                "detail": "high" # Use high detail for potentially complex images
                            },
                        },
                    ],
                }
            ],
            max_tokens=1000 # Adjust token limit as needed
        )
        # Accessing the response content correctly
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content
        else:
            print("Error: No response content received from OpenAI.", file=sys.stderr)
            return None

    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        return None

# --- Example Usage (Optional) ---
if __name__ == "__main__":
    # This block runs only when the script is executed directly
    # Replace with a valid image path and prompt for testing
    test_image_path = "path/to/your/test_image.png" # <--- CHANGE THIS
    test_prompt = "Describe the main elements in this image."

    if not os.environ.get("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY environment variable not set.", file=sys.stderr)
        print("Please set it or add it directly to the script for testing (not recommended for production).", file=sys.stderr)
    elif not os.path.exists(test_image_path):
         print(f"Warning: Test image path '{test_image_path}' does not exist. Skipping example usage.", file=sys.stderr)
    else:
        print(f"Testing with image: {test_image_path}")
        print(f"Prompt: {test_prompt}")
        details = get_image_details(test_image_path, test_prompt)

        if details:
            print("\n--- OpenAI Response ---")
            print(details)
            print("----------------------")
        else:
            print("\nFailed to get details from the image.")
