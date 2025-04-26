# image_details_extractor.py
import base64
import requests # Using requests as openai v1+ requires it for image URLs or base64
import os
import mimetypes
from openai import OpenAI
import sys
import glob # Import glob for finding files
from dotenv import load_dotenv # Import the dotenv library

# --- Configuration ---
# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client to use OpenRouter endpoint and API key
try:
    openrouter_api_key = os.getenv("OpenRouter_API_KEY")
    if not openrouter_api_key:
        raise ValueError("OpenRouter_API_KEY not found in .env file or environment variables.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_api_key,
    )
    # Simple check to confirm client object creation
    if not client:
         raise Exception("Failed to create OpenAI client configured for OpenRouter.")

except Exception as e:
    print(f"Error initializing client for OpenRouter: {e}", file=sys.stderr)
    print("Please ensure the OpenAI library is installed (`pip install openai`),", file=sys.stderr)
    print("the python-dotenv library is installed (`pip install python-dotenv`),", file=sys.stderr)
    print("and the OpenRouter_API_KEY is correctly set in the .env file.", file=sys.stderr)
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
def get_image_details(image_path: str) -> str | None:
    """
    Sends an image to the OpenAI Vision API (gpt-4o) with a prompt instructing
    it to extract visible experimental data and return it as a self-generated JSON structure.

    Args:
        image_path: The local path to the image file.

    Returns:
        A JSON string containing the extracted data, or None if an error occurs.
    """
    # Define the simplified prompt for dynamic JSON generation
    prompt = """Analyze the provided image, which likely contains experimental data (e.g., graphs, tables, micrographs, setup diagrams) related to Chemical Mechanical Planarization (CMP) or similar scientific research.

Your task is to:
1.  Identify all specific data points, parameters, sample identifiers, results, conditions, labels, and relevant textual information visible ONLY within this image.
2.  Structure this extracted information logically into a valid JSON object. The structure should reflect the relationships between the data points found in the image (e.g., data series in a graph, columns/rows in a table).
3.  Do NOT use a predefined template. Create keys and structure based SOLELY on the information present in THIS image.
4.  Include units (e.g., nm/min, °C, wt%, M, psi, nm, µm) with the values if they are visible in the image.
5.  CRITICAL: The output MUST be ONLY the raw JSON object itself. Start directly with `{` and end directly with `}`. Do NOT include ```json, explanations, or any other text before or after the JSON object. If no relevant data is found, return an empty JSON object {}.

Example data to look for: Material Removal Rate (MRR), sample names, concentrations, temperatures, pressures, particle sizes, crystallite sizes, graph axes labels and values, table headers and cell values, labels in diagrams, scale bars in micrographs.
"""
    if not client:
        print("Error: OpenAI client is not initialized.", file=sys.stderr)
        return None

    base64_image = encode_image_to_base64(image_path)
    if not base64_image:
        return None # Error message already printed by encode_image_to_base64

    try:
        # Using OpenRouter's identifier for Anthropic Claude 3 Haiku (trying short form)
        # Verify this identifier if issues occur: https://openrouter.ai/models
        model_identifier = "google/gemini-2.5-pro-preview-03-25" # <-- Trying shorter model ID
        print(f"Using model: {model_identifier} via OpenRouter", file=sys.stderr)

        response = client.chat.completions.create(
            model=model_identifier,
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
            max_tokens=12000, # Adjust token limit as needed
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
    # --- Define Input and Output Folders ---
    input_folder = "Input_Md_Images\\0220_CMP_Slurries\\1_k9dmxr\\images"
    output_folder = "image_analysis_test\\output_jsons"

    # --- Check if Client Initialized (implies API key was found) ---
    if not client:
        print("OpenAI client failed to initialize. Exiting.", file=sys.stderr)
        sys.exit(1)

    # --- Create Output Folder ---
    try:
        os.makedirs(output_folder, exist_ok=True)
        print(f"Output will be saved in: {output_folder}")
    except Exception as e:
        print(f"Error creating output directory '{output_folder}': {e}", file=sys.stderr)
        sys.exit(1)

    # --- Find Image Files ---
    # Look for common image file extensions
    image_patterns = [os.path.join(input_folder, ext) for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']]
    image_files = []
    for pattern in image_patterns:
        image_files.extend(glob.glob(pattern))

    if not image_files:
        print(f"No image files found in '{input_folder}'. Please check the path and file extensions.", file=sys.stderr)
        sys.exit(0)

    print(f"Found {len(image_files)} images to process in '{input_folder}'.")

    # --- Process Each Image ---
    for image_path in image_files:
        print(f"\nProcessing image: {image_path}")
        try:
            json_output = get_image_details(image_path)

            if json_output:
                # Construct output filename
                base_filename = os.path.basename(image_path)
                name_part, _ = os.path.splitext(base_filename)
                output_filename = os.path.join(output_folder, f"{name_part}.json")

                # Clean up potential markdown fences before validation
                cleaned_output = json_output.strip()
                if cleaned_output.startswith("```json"):
                    cleaned_output = cleaned_output[7:] # Remove ```json\n
                if cleaned_output.endswith("```"):
                    cleaned_output = cleaned_output[:-3] # Remove ```
                cleaned_output = cleaned_output.strip() # Remove any extra whitespace

                # Validate and Save JSON
                try:
                    import json
                    # Try loading the cleaned output to validate
                    json_data = json.loads(cleaned_output)
                    # Save the validated JSON
                    with open(output_filename, 'w', encoding='utf-8') as f:
                        json.dump(json_data, f, indent=2) # Save with indentation
                    print(f"Successfully extracted, cleaned, and saved valid JSON to: {output_filename}")

                except json.JSONDecodeError as e:
                    # If cleaning didn't help, report the error with the cleaned output
                    print(f"WARNING: Output for {image_path} is STILL NOT valid JSON after cleaning. Error: {e}", file=sys.stderr)
                    print(f"--- Cleaned Output Attempt for {image_path} ---", file=sys.stderr)
                    print(cleaned_output, file=sys.stderr)
                    print("------------------------------------------", file=sys.stderr)
                    # Optionally save the raw invalid output (original, before cleaning) to a .txt file
                    # output_txt_filename = os.path.join(output_folder, f"{name_part}_error.txt")
                    # with open(output_txt_filename, 'w', encoding='utf-8') as f:
                    #     f.write(json_output)
                    # print(f"Saved raw invalid output to: {output_txt_filename}")

            else:
                print(f"Failed to get details from image: {image_path}. Check API key, network, etc.")

        except Exception as e:
            print(f"An unexpected error occurred while processing {image_path}: {e}", file=sys.stderr)

    print("\nFinished processing all images.")
