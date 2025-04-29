import os
import json
import sys

def combine_corrected_json(input_base_dir, subdirs, output_filename):
    """
    Combines specific JSON files from subdirectories into a single dataset.

    Args:
        input_base_dir (str): The base directory containing the subdirectories.
        subdirs (list): A list of subdirectory names to process.
        output_filename (str): The name for the combined output JSON file.
    """
    combined_data = []
    processed_files_count = 0
    skipped_folders_count = 0
    found_corrected_files = False # Flag to track if any corrected files were found

    print(f"Starting JSON combination process...")
    print(f"Base input directory: {os.path.abspath(input_base_dir)}")
    print(f"Processing subdirectories: {', '.join(subdirs)}")
    print(f"Output file will be: {os.path.abspath(output_filename)}")
    print("-" * 30)

    if not os.path.isdir(input_base_dir):
        print(f"Error: Base input directory '{input_base_dir}' not found.")
        sys.exit(1)

    for subdir_name in subdirs:
        current_subdir_path = os.path.join(input_base_dir, subdir_name)
        print(f"\nProcessing subdirectory: {subdir_name}")

        if not os.path.isdir(current_subdir_path):
            print(f"  Warning: Subdirectory '{subdir_name}' not found. Skipping.")
            continue

        # Iterate through items (folders) within the current subdirectory
        for item_name in os.listdir(current_subdir_path):
            item_path = os.path.join(current_subdir_path, item_name)

            # Check if the item is a directory (representing a research paper folder)
            if os.path.isdir(item_path):
                print(f"  Entering paper folder: {item_name}")
                found_target_json = False
                # Look for the specific JSON file within the paper folder
                for filename in os.listdir(item_path):
                    if filename.endswith("_Correct_Extraction.json"):
                        json_file_path = os.path.join(item_path, filename)
                        print(f"    Found corrected JSON: {filename}")
                        try:
                            with open(json_file_path, 'r', encoding='utf-8') as f:
                                # Load JSON data - handles unicode escapes automatically
                                data = json.load(f)
                                combined_data.append(data)
                                processed_files_count += 1
                                found_target_json = True
                                found_corrected_files = True # Mark that at least one file was found overall
                                # Only process the first matching file per folder if multiple exist
                                break
                        except json.JSONDecodeError as e:
                            print(f"    Error: Could not decode JSON from {filename}. Skipping. Details: {e}")
                        except Exception as e:
                            print(f"    Error: Could not read file {filename}. Skipping. Details: {e}")

                if not found_target_json:
                    print(f"    Warning: No '*_Correct_Extraction.json' file found in folder '{item_name}'.")
                    skipped_folders_count += 1
            else:
                 # Optionally handle non-directory items if needed
                 # print(f"  Skipping non-directory item: {item_name}")
                 pass


    print("-" * 30)
    # Write the combined data to the output file
    if found_corrected_files:
        try:
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                # Dump data with ensure_ascii=False to keep unicode characters as symbols
                json.dump(combined_data, outfile, ensure_ascii=False, indent=4)
            print(f"\nSuccessfully combined data from {processed_files_count} files.")
            print(f"Skipped {skipped_folders_count} paper folders due to missing corrected JSON.")
            print(f"Combined dataset saved to: {os.path.abspath(output_filename)}")
        except Exception as e:
            print(f"\nError: Could not write combined data to {output_filename}. Details: {e}")
    else:
        print("\nWarning: No '*_Correct_Extraction.json' files were found in any of the specified directories.")
        print("No combined output file was created.")

# --- Configuration ---
INPUT_DIR = "Input_Md_Images/"
SUBDIRECTORIES = [
    "0220_CMP_Slurries",
    "Ceria_Related_Patents",
    "Doped_Ceria_After_Meeting"
]
OUTPUT_FILE = "combined_dataset.json"
# --- End Configuration ---

if __name__ == "__main__":
    combine_corrected_json(INPUT_DIR, SUBDIRECTORIES, OUTPUT_FILE)
