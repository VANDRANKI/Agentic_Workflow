import os
import json
import glob
import re # For potential regex parsing
import argparse

# --- Configuration ---
# Directory where the pre-generated image JSONs are stored
IMAGE_JSON_DIR = "image_analysis_test/output_jsons/"
# Directory where the final combined JSON output will be saved
OUTPUT_DIR = "Experimental_Sample_Extraction/"
# Directory containing the paper subfolders (MD files + images/)
# This can be overridden by command-line argument
DEFAULT_INPUT_DIR = "Input_Md_Images/0220_CMP_Slurries/"

# --- Helper Functions ---

def find_files(paper_dir):
    """Finds the .md file and images directory within a paper directory."""
    md_files = glob.glob(os.path.join(paper_dir, '*.md'))
    if not md_files:
        print(f"Warning: No .md file found in {paper_dir}")
        return None, None
    md_file = md_files[0] # Assume only one MD file per folder

    images_dir = os.path.join(paper_dir, 'images')
    if not os.path.isdir(images_dir):
        print(f"Warning: No 'images' directory found in {paper_dir}")
        # Continue without images if necessary, or handle as error
        images_dir = None

    return md_file, images_dir

def parse_markdown_table(table_content):
    """Parses a Markdown table into a list of dictionaries."""
    lines = table_content.strip().split('\n')
    if len(lines) < 3: # Header, separator, at least one data row
        return []

    header = [h.strip() for h in lines[0].strip('|').split('|')]
    data = []

    for line in lines[2:]: # Skip separator line
        values = [v.strip() for v in line.strip('|').split('|')]
        if len(values) == len(header):
            row_dict = dict(zip(header, values))
            data.append(row_dict)
        else:
            print(f"Warning: Skipping malformed table row: {line}")
    return data

def parse_markdown(md_file_path):
    """Parses the markdown file to extract metadata and sample data."""
    print(f"Parsing Markdown: {md_file_path}")
    metadata = {
        "doi": None,
        "title": None,
        "year_published": None,
        "journal": None
    }
    samples_map = {} # Use a map for easier updating: key = sample_id

    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # --- Metadata Extraction (Improved Checks) ---
        title_match = re.search(r'^#\s*(.*)', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1).strip()

        doi_match = re.search(r'https://doi\.org/([\d./\w-]+)', content)
        if doi_match:
            metadata['doi'] = doi_match.group(1).strip()
        else:
             doi_match_alt = re.search(r'(10\.\d{4,}/[\w.-]+)', content)
             if doi_match_alt: # Check if doi_match_alt found something
                 metadata['doi'] = doi_match_alt.group(1).strip()

        year_match = re.search(r'Received \d{1,2} \w+ (\d{4})', content)
        if year_match:
            metadata['year_published'] = year_match.group(1)
        else:
            year_match_alt = re.search(r'© (\d{4})', content)
            if year_match_alt: # Check if year_match_alt found something
                 metadata['year_published'] = year_match_alt.group(1)

        # Check DOI before using it for journal inference
        current_doi = metadata.get('doi')
        if current_doi and 'ceramint' in current_doi:
             metadata['journal'] = "Ceramics International"

        # --- General Experimental Details Extraction (Example) ---
        # Find precursor details, slurry prep, CMP conditions from text sections
        # This needs more specific regex based on section headers/keywords
        precursor_conc_match = re.search(r'(\d\.\d+)\s*M\s*(Ce\(NO₃\)₃|Ce\(NO3\)3)', content)
        precursor_conc = precursor_conc_match.group(1) if precursor_conc_match else "0.1" # Default from 1_k9dmxr

        slurry_conc_match = re.search(r'(\d\.\d+)\s*wt%\s*(PVA)', content)
        slurry_conc = slurry_conc_match.group(1) if slurry_conc_match else "0.2" # Default from 1_k9dmxr

        # --- Table 1 Parsing Logic ---
        table1_match = re.search(r'Table 1\n(.*?)\n\n', content, re.DOTALL | re.IGNORECASE)
        if table1_match:
            table1_content = table1_match.group(1)
            # Basic parsing assuming simple markdown table format
            lines = table1_content.strip().split('\n')
            if len(lines) > 7: # Check if it looks like the expected table
                headers = [h.strip() for h in lines[1].strip('|').split('|')] # Ce precursor/OH-, ratios...
                ratios = headers[1:6] # 1:1, 1:2, ...
                
                # Extract data rows (dXRD RT, dXRD 80C, Cryst RT, Cryst 80C)
                dxrd_rt_values = [v.strip() for v in lines[3].strip('|').split('|')][1:]
                dxrd_80c_values = [v.strip() for v in lines[4].strip('|').split('|')][1:]
                cryst_rt_values = [v.strip() for v in lines[7].strip('|').split('|')][1:]
                cryst_80c_values = [v.strip() for v in lines[8].strip('|').split('|')][1:]
                
                # Process Ce3+ samples
                for i, ratio in enumerate(ratios):
                    # RT Sample
                    sample_id_rt = f"Ce3+_{ratio.replace(':','-')}_RT" # Use '-' instead of ':' for safety
                    samples_map[sample_id_rt] = {
                        "sample_id": sample_id_rt,
                        "precursor_chemical": "Ce(NO₃)₃·6H₂O",
                        "molar_ratio_precursor_precipitant": ratio,
                        "reaction_temperature": {"value": "RT", "unit": ""},
                        "precursor_concentration": {"value": precursor_conc, "unit": "M"},
                        "slurry_preparation": {"abrasive_ceria_concentration": {"value": slurry_conc, "unit": "wt%"}}, # Example
                        "characterization": {
                            "crystallite_size": {"value": dxrd_rt_values[i] if dxrd_rt_values[i] != '-' else None, "unit": "nm"},
                            "crystallinity_phase_composition": {"value": cryst_rt_values[i] if cryst_rt_values[i] != '-' else None, "unit": "%"}
                        },
                        # Add other common fields as placeholders
                        "cmp_performance": {},
                        "theoretical_analysis": {}
                    }
                    # 80C Sample
                    sample_id_80c = f"Ce3+_{ratio.replace(':','-')}_80C"
                    samples_map[sample_id_80c] = {
                        "sample_id": sample_id_80c,
                        "precursor_chemical": "Ce(NO₃)₃·6H₂O",
                        "molar_ratio_precursor_precipitant": ratio,
                        "reaction_temperature": {"value": "80", "unit": "°C"},
                        "precursor_concentration": {"value": precursor_conc, "unit": "M"},
                        "slurry_preparation": {"abrasive_ceria_concentration": {"value": slurry_conc, "unit": "wt%"}}, # Example
                        "characterization": {
                            "crystallite_size": {"value": dxrd_80c_values[i] if dxrd_80c_values[i] != '-' else None, "unit": "nm"},
                            "crystallinity_phase_composition": {"value": cryst_80c_values[i] if cryst_80c_values[i] != '-' else None, "unit": "%"}
                        },
                        "cmp_performance": {},
                        "theoretical_analysis": {}
                    }

                # Process Ce4+ samples (indices shifted)
                ce4_ratios = headers[7:] # 1:2, 1:3, ... for Ce4+
                dxrd_rt_values_ce4 = [v.strip() for v in lines[3].strip('|').split('|')][7:]
                dxrd_80c_values_ce4 = [v.strip() for v in lines[4].strip('|').split('|')][7:]
                cryst_rt_values_ce4 = [v.strip() for v in lines[7].strip('|').split('|')][7:]
                cryst_80c_values_ce4 = [v.strip() for v in lines[8].strip('|').split('|')][7:]

                for i, ratio in enumerate(ce4_ratios):
                    if ratio == '-': continue # Skip empty columns if any
                    # RT Sample
                    sample_id_rt = f"Ce4+_{ratio.replace(':','-')}_RT"
                    samples_map[sample_id_rt] = {
                        "sample_id": sample_id_rt,
                        "precursor_chemical": "(NH₄)₂Ce(NO₃)₆",
                        "molar_ratio_precursor_precipitant": ratio,
                        "reaction_temperature": {"value": "RT", "unit": ""},
                        "precursor_concentration": {"value": precursor_conc, "unit": "M"},
                        "slurry_preparation": {"abrasive_ceria_concentration": {"value": slurry_conc, "unit": "wt%"}}, # Example
                        "characterization": {
                            "crystallite_size": {"value": dxrd_rt_values_ce4[i] if dxrd_rt_values_ce4[i] != '-' else None, "unit": "nm"},
                            "crystallinity_phase_composition": {"value": cryst_rt_values_ce4[i] if cryst_rt_values_ce4[i] != '-' else None, "unit": "%"}
                        },
                        "cmp_performance": {},
                        "theoretical_analysis": {}
                    }
                    # 80C Sample
                    sample_id_80c = f"Ce4+_{ratio.replace(':','-')}_80C"
                    # Handle potentially missing last value in 80C crystallinity row
                    cryst_80c_val = None
                    if i < len(cryst_80c_values_ce4) and cryst_80c_values_ce4[i] != '-':
                         cryst_80c_val = cryst_80c_values_ce4[i]
                    elif i == len(cryst_80c_values_ce4) -1 and len(cryst_80c_values_ce4) < len(ce4_ratios): # Assume last value missing
                         print(f"Warning: Assuming missing crystallinity value for {sample_id_80c}")
                         cryst_80c_val = None # Or try to infer based on trend/previous value

                    samples_map[sample_id_80c] = {
                        "sample_id": sample_id_80c,
                        "precursor_chemical": "(NH₄)₂Ce(NO₃)₆",
                        "molar_ratio_precursor_precipitant": ratio,
                        "reaction_temperature": {"value": "80", "unit": "°C"},
                        "precursor_concentration": {"value": precursor_conc, "unit": "M"},
                        "slurry_preparation": {"abrasive_ceria_concentration": {"value": slurry_conc, "unit": "wt%"}}, # Example
                        "characterization": {
                            "crystallite_size": {"value": dxrd_80c_values_ce4[i] if dxrd_80c_values_ce4[i] != '-' else None, "unit": "nm"},
                            "crystallinity_phase_composition": {"value": cryst_80c_val, "unit": "%"}
                        },
                        "cmp_performance": {},
                        "theoretical_analysis": {}
                    }
        else:
            print("Warning: Could not find or parse Table 1.")

        # --- Placeholder for Table 2, Table 3, and other text parsing ---
        print(f"Placeholder: Further parsing needed for Tables 2, 3, and text in {md_file_path}")

    except Exception as e:
        print(f"Error parsing Markdown file {md_file_path}: {e}")

    # Convert map to list
    samples_data = list(samples_map.values())
    return metadata, samples_data

def read_image_json(image_json_path):
    """Reads a JSON file containing data extracted from an image."""
    if not os.path.exists(image_json_path):
        print(f"Warning: Image JSON file not found: {image_json_path}")
        return None
    try:
        with open(image_json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading image JSON file {image_json_path}: {e}")
        return None

def merge_data(metadata, samples_data, image_jsons_map):
    """Merges Markdown data with corresponding image data."""
    print("Merging data...")
    
    # Convert samples list back to map for easier lookup by sample_id
    samples_map = {sample['sample_id']: sample for sample in samples_data}

    # --- Merge MRR data (Fig 2 / img-1.json) ---
    mrr_data = image_jsons_map.get('img-1.json')
    if mrr_data and 'data_series' in mrr_data:
        for series in mrr_data['data_series']:
            condition = series.get('condition', {})
            source = condition.get('source', '')
            temp_str = condition.get('temperature', '')
            temp_code = "RT" if temp_str == "RT" else "80C"
            precursor_type = "Ce3+" if "Ce³⁺" in source else "Ce4+" if "Ce⁴⁺" in source else None

            if precursor_type:
                for ratio, value in series.get('data_points', {}).items():
                    sample_id = f"{precursor_type}_{ratio.replace(':','-')}_{temp_code}"
                    if sample_id in samples_map:
                        if 'cmp_performance' not in samples_map[sample_id]:
                            samples_map[sample_id]['cmp_performance'] = {}
                        # Update MRR, ensuring value and unit exist
                        samples_map[sample_id]['cmp_performance']['material_removal_rate'] = {
                            "value": value,
                            "unit": series.get("unit", "nm/min") # Use unit from image json
                        }
                        # Add other general CMP params if not already present
                        if 'polishing_time' not in samples_map[sample_id]['cmp_performance']:
                             samples_map[sample_id]['cmp_performance']['polishing_time'] = {"value": "1", "unit": "min"} # Default from text
                        if 'pad_conditioning_pressure' not in samples_map[sample_id]['cmp_performance']:
                             samples_map[sample_id]['cmp_performance']['pad_conditioning_pressure'] = {"value": "3", "unit": "psi"} # Default from text


    # --- Merge FTIR peak presence (Fig 3 / img-2.json) ---
    ftir_data = image_jsons_map.get('img-2.json', {}).get('FTIR_Analysis', {})
    if ftir_data:
         # Panel A (Ce3+)
         panel_a = ftir_data.get('panel_a', {})
         no3_present_a = "NO₃" in panel_a.get('band_labels', [])
         for spectrum in panel_a.get('spectra', []):
             ratio = spectrum.get('ratio_value')
             if ratio:
                 # Determine NO3 presence based on text description (absent beyond 1:2)
                 no3_peak_present = no3_present_a and ratio in ["1:1", "1:2"]
                 for temp_dataset in spectrum.get('dataset', []):
                     temp_code = "RT" if temp_dataset == "RT" else "80C"
                     sample_id = f"Ce3+_{ratio.replace(':','-')}_{temp_code}"
                     if sample_id in samples_map:
                         if 'surface_functional_groups' in samples_map[sample_id]['characterization'] and \
                            'NO3' in samples_map[sample_id]['characterization']['surface_functional_groups']:
                             samples_map[sample_id]['characterization']['surface_functional_groups']['NO3']['ftir_peak_present'] = no3_peak_present

         # Panel B (Ce4+)
         panel_b = ftir_data.get('panel_b', {})
         no3_present_b = "NO₃" in panel_b.get('band_labels', [])
         for spectrum in panel_b.get('spectra', []):
             ratio = spectrum.get('ratio_value')
             if ratio:
                 for temp_dataset in spectrum.get('dataset', []):
                     temp_code = "RT" if temp_dataset == "RT" else "80C"
                     sample_id = f"Ce4+_{ratio.replace(':','-')}_{temp_code}"
                     if sample_id in samples_map:
                         if 'surface_functional_groups' in samples_map[sample_id]['characterization'] and \
                            'NO3' in samples_map[sample_id]['characterization']['surface_functional_groups']:
                             # For Ce4+, NO3 peak is always present according to text/Fig3b
                             samples_map[sample_id]['characterization']['surface_functional_groups']['NO3']['ftir_peak_present'] = no3_present_b


    # --- Merge TGA Weight Loss (Fig 4 / img-3.json) ---
    tga_data = image_jsons_map.get('img-3.json', {}).get('subplot_d', {}).get('data_series', [])
    if tga_data:
        for series in tga_data:
            sample_desc = series.get('sample', '')
            weight_loss_str = series.get('weight_loss', '')
            try:
                weight_loss_val = float(weight_loss_str.replace('%',''))
            except:
                weight_loss_val = None

            if weight_loss_val is not None:
                precursor_type = "Ce3+" if "Ce³⁺" in sample_desc else "Ce4+" if "Ce⁴⁺" in sample_desc else None
                if precursor_type:
                    # Apply to the 1:2 ratio samples as per text context
                    for temp_code in ["RT", "80C"]:
                        sample_id = f"{precursor_type}_1-2_{temp_code}"
                        if sample_id in samples_map:
                            samples_map[sample_id]['characterization']['tga_weight_loss_percent'] = weight_loss_val

    # --- Merge UV-Vis/Raman Peaks (Fig 5 / img-4.json) ---
    uv_raman_data = image_jsons_map.get('img-4.json', {})
    if uv_raman_data:
        # UV-Vis peaks (apply to 1:2 ratio samples)
        uv_peaks = []
        for annotation in uv_raman_data.get('figure_a',{}).get('annotations',[]):
            if annotation.get('type') == 'indicator_line':
                 uv_peaks.append(annotation.get('position_approx'))
        if uv_peaks:
             for precursor_type in ["Ce3+", "Ce4+"]:
                 for temp_code in ["RT", "80C"]:
                     sample_id = f"{precursor_type}_1-2_{temp_code}"
                     if sample_id in samples_map:
                         samples_map[sample_id]['characterization']['uv_vis_peaks_nm'] = sorted([p for p in uv_peaks if p]) # Store sorted list

        # Raman peaks (apply to 1:2 ratio samples)
        raman_peaks = []
        raman_no3_present = False
        for peak in uv_raman_data.get('figure_b',{}).get('peak_labels',[]):
             pos = peak.get('position_approx')
             if pos:
                 raman_peaks.append(pos)
             if peak.get('label') == 'NO₃':
                 raman_no3_present = True

        if raman_peaks:
             for precursor_type in ["Ce3+", "Ce4+"]:
                 for temp_code in ["RT", "80C"]:
                     sample_id = f"{precursor_type}_1-2_{temp_code}"
                     if sample_id in samples_map:
                         # Only add NO3 peaks if relevant based on FTIR/text
                         current_no3_present = samples_map[sample_id]['characterization'].get('surface_functional_groups',{}).get('NO3',{}).get('ftir_peak_present', False)
                         peaks_to_add = sorted([p for p in raman_peaks if p < 700]) # F2g, D
                         if current_no3_present and raman_no3_present:
                             peaks_to_add.extend(sorted([p for p in raman_peaks if p >= 700])) # Add NO3 peaks
                         samples_map[sample_id]['characterization']['raman_peaks_cm-1'] = peaks_to_add


    # --- Merge XPS data (Fig 6 / img-5.json) ---
    xps_data = image_jsons_map.get('img-5.json', {})
    if xps_data:
        # Panel A (Ce 3d - Ce3+ percentage)
        for spectrum in xps_data.get('Panel_a', {}).get('spectra', []):
            desc = spectrum.get('sample_description', '')
            ce3_perc = spectrum.get('Ce3_percentage', {}).get('value')
            precursor_type = "Ce3+" if "Ce3+" in desc else "Ce4+" if "Ce4+" in desc else None
            if precursor_type and ce3_perc is not None:
                # Apply to RT, 1:2 ratio sample based on Table III context
                sample_id = f"{precursor_type}_1-2_RT"
                if sample_id in samples_map:
                    samples_map[sample_id]['characterization']['surface_ce3_percent_xps'] = ce3_perc

        # Panel B (O 1s - Oxygen species)
        for spectrum in xps_data.get('Panel_b', {}).get('spectra', []):
            desc = spectrum.get('sample_description', '')
            species_perc = spectrum.get('oxygen_species_percentage', [])
            precursor_type = "Ce3+" if "Ce3+" in desc else "Ce4+" if "Ce4+" in desc else None
            if precursor_type and species_perc:
                 # Apply to RT, 1:2 ratio sample based on Table III context
                sample_id = f"{precursor_type}_1-2_RT"
                if sample_id in samples_map:
                    samples_map[sample_id]['characterization']['oxygen_species_percent_xps'] = {
                        item['species']: item['value'] for item in species_perc if 'species' in item and 'value' in item
                    }

    # --- Merge Adhesion Work (Fig 7 / img-6.json) ---
    wad_data = image_jsons_map.get('img-6.json', {})
    if wad_data:
        # Crystalline (maps to Ce3+)
        for sim in wad_data.get('Simulation_Set_a', {}).get('Simulations', []):
            conditions = sim.get('System_Label', '').split(' ')[-1] # e.g., OH, NO3, Ov
            wad_value = sim.get('Adhesion_Work', {}).get('Value')
            if wad_value is not None and conditions in ['OH', 'NO3', 'Ov']: # Add relevant conditions
                 for ratio_code in ["1-1", "1-2", "1-3", "1-4", "1-5"]:
                     for temp_code in ["RT", "80C"]:
                         sample_id = f"Ce3+_{ratio_code}_{temp_code}"
                         if sample_id in samples_map:
                             # Store the most relevant one (OH based on text) or potentially all?
                             # Storing the one matching text description for now
                             if conditions == 'OH':
                                 samples_map[sample_id]['theoretical_analysis']['work_of_adhesion'] = {
                                     "value": wad_value,
                                     "unit": "J/m²",
                                     "conditions": f"Crystalline CeO₂ with {conditions} groups"
                                 }

        # Amorphous (maps to Ce4+)
        for sim in wad_data.get('Simulation_Set_b', {}).get('Simulations', []):
            conditions = sim.get('System_Label', '').split(' ')[-1] # e.g., OH, NO3, Ov
            wad_value = sim.get('Adhesion_Work', {}).get('Value')
            if wad_value is not None and conditions in ['OH', 'NO3', 'Ov']:
                 for ratio_code in ["1-2", "1-3", "1-4", "1-5"]: # Ce4+ starts from 1:2
                     for temp_code in ["RT", "80C"]:
                         sample_id = f"Ce4+_{ratio_code}_{temp_code}"
                         if sample_id in samples_map:
                             # Store the most relevant one (NO3 based on text)
                             if conditions == 'NO3':
                                 samples_map[sample_id]['theoretical_analysis']['work_of_adhesion'] = {
                                     "value": wad_value,
                                     "unit": "J/m²",
                                     "conditions": f"Amorphous CeO₂ with {conditions} groups"
                                 }


    # Add image data sources for reference
    metadata["image_data_sources"] = list(image_jsons_map.keys())

    print("Finished merging data.")

    # Convert map back to list for final output
    final_samples = list(samples_map.values())

    return {
        "doi": metadata.get("doi"),
        "title": metadata.get("title"),
        "year_published": metadata.get("year_published"),
        "journal": metadata.get("journal"),
        "samples": final_samples
        # Potentially add raw image json data here too if needed for debugging
    }

# --- Main Processing Function ---

def process_paper(paper_dir):
    """Processes a single paper directory."""
    print(f"\nProcessing directory: {paper_dir}")
    paper_name = os.path.basename(paper_dir)

    md_file, images_dir = find_files(paper_dir)
    if not md_file:
        return # Skip if no markdown file found

    # 1. Parse Markdown
    metadata, samples_data = parse_markdown(md_file)

    # 2. Load Image JSONs
    image_jsons_map = {}
    # Assuming image JSONs are named like the images (img-0.json, img-1.json etc.)
    # We need a way to map figure numbers (Fig 1, Fig 2) to these filenames.
    # This mapping might need to be inferred or predefined.
    # Example: Manually map based on the first paper
    figure_to_image_map = {
        "Fig1": "img-0.json", # XRD
        "Fig2": "img-1.json", # MRR
        "Fig3": "img-2.json", # FTIR
        "Fig4": "img-3.json", # TGA/FTIR
        "Fig5": "img-4.json", # UV-Vis/Raman
        "Fig6": "img-5.json", # XPS
        "Fig7": "img-6.json"  # Adhesion Sim
    }
    for fig_key, img_json_name in figure_to_image_map.items():
        img_json_path = os.path.join(IMAGE_JSON_DIR, img_json_name)
        img_data = read_image_json(img_json_path)
        if img_data:
            image_jsons_map[img_json_name] = img_data # Store loaded JSON data

    # 3. Merge Data
    final_data = merge_data(metadata, samples_data, image_jsons_map)

    # 4. Save Output
    output_filename = os.path.join(OUTPUT_DIR, f"{paper_name}_extracted_data.json")
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(final_data, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved combined data to: {output_filename}")
    except Exception as e:
        print(f"Error saving final JSON to {output_filename}: {e}")

# --- Script Execution ---

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and merge experimental data from Markdown files and associated image JSONs.")
    parser.add_argument("input_dir", nargs='?', default=DEFAULT_INPUT_DIR,
                        help=f"Directory containing paper subfolders (default: {DEFAULT_INPUT_DIR})")
    args = parser.parse_args()

    input_directory = args.input_dir

    if not os.path.isdir(input_directory):
        print(f"Error: Input directory not found: {input_directory}")
        exit(1)

    print(f"Starting extraction process for directory: {input_directory}")

    # Find all subdirectories in the input directory
    paper_dirs = [d for d in glob.glob(os.path.join(input_directory, '*')) if os.path.isdir(d)]

    if not paper_dirs:
        print(f"No subdirectories found in {input_directory}. Nothing to process.")
        exit(0)

    for paper_dir in paper_dirs:
        process_paper(paper_dir)

    print("\nFinished processing all directories.")
