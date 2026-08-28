"""
Regression test for the Table 1 parsing bug in master_extractor.parse_markdown().

Bug: the regex used to isolate "Table 1" (`r'Table 1\n(.*?)\n\n'`) grabbed the
caption paragraph that sits directly under the "Table 1" label, not the actual
Markdown pipe-table that follows a blank line later. Since the caption is a
single line, the `len(lines) > 7` sanity check always failed and the entire
Table 1 branch was silently skipped -- parse_markdown returned 0 samples for
1_k9dmxr.md (the exact paper this parsing logic was written for), even though
no warning was ever printed.

A second, compounding bug: once the real table block is captured, it includes
the Markdown alignment separator row (the "| :--: | :--: | ..." row that
sits between the group header and the ratio labels). The code read the ratio
labels from `lines[1]` (the separator row) instead of `lines[2]` (the actual
"1:1, 1:2, ..." row), so `ratios` ended up being a list of ":--:" strings.

This test parses the real sample paper shipped in this repo
(Input_Md_Images/0220_CMP_Slurries/1_k9dmxr/1_k9dmxr.md) and checks the
extracted sample count and a handful of known Table 1 values against the
hand-verified reference file 1_k9dmxr_Correct_Extraction.json.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import master_extractor as me

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER_DIR = os.path.join(
    REPO_ROOT, "Input_Md_Images", "0220_CMP_Slurries", "1_k9dmxr",
)
MD_FILE = os.path.join(PAPER_DIR, "1_k9dmxr.md")
IMAGE_JSON_DIR = os.path.join(REPO_ROOT, "image_analysis_test", "output_jsons")


def _samples_by_id(samples):
    return {s["sample_id"]: s for s in samples}


def test_table1_is_actually_parsed():
    """Before the fix this returned 0 samples for every paper."""
    _, samples = me.parse_markdown(MD_FILE)
    assert len(samples) == 18, (
        f"expected 18 samples from Table 1 of 1_k9dmxr.md, got {len(samples)}"
    )


def test_table1_values_match_known_reference():
    _, samples = me.parse_markdown(MD_FILE)
    by_id = _samples_by_id(samples)

    # Spot-check values straight out of the paper's Table 1 (see the
    # hand-verified 1_k9dmxr_Correct_Extraction.json for the full set).
    expected = {
        "Ce3+_1-1_RT": ("6.8", "83"),
        "Ce3+_1-2_80C": ("13.5", "86"),
        "Ce4+_1-2_RT": ("4.9", "63"),
        "Ce4+_1-5_RT": ("6.6", "64"),
    }
    for sample_id, (dxrd, cryst) in expected.items():
        assert sample_id in by_id, f"missing sample {sample_id}"
        char = by_id[sample_id]["characterization"]
        assert char["crystallite_size"]["value"] == dxrd, sample_id
        assert char["crystallinity_phase_composition"]["value"] == cryst, sample_id

    # Ce4+ has no 1:1 sample -- the paper reports no precipitation at that ratio.
    assert "Ce4+_1-1_RT" not in by_id
    assert "Ce4+_1-1_80C" not in by_id


def test_missing_trailing_crystallinity_cell_is_none_not_empty_string():
    """The last cell of the 80C crystallinity row is blank in the source table
    (not a '-'), so it must come through as None rather than an empty string."""
    _, samples = me.parse_markdown(MD_FILE)
    by_id = _samples_by_id(samples)
    value = by_id["Ce4+_1-5_80C"]["characterization"]["crystallinity_phase_composition"]["value"]
    assert value is None


def _load_image_jsons_map():
    image_jsons_map = {}
    for name in ["img-1.json", "img-2.json", "img-3.json", "img-4.json", "img-5.json", "img-6.json"]:
        path = os.path.join(IMAGE_JSON_DIR, name)
        with open(path, encoding="utf-8") as f:
            image_jsons_map[name] = json.load(f)
    return image_jsons_map


def test_ftir_no3_presence_and_downstream_raman_peaks_are_merged():
    """
    Regression test for a second bug in the same file: merge_data() only
    records the FTIR NO3-peak-presence result (from image_analysis_test/
    output_jsons/img-2.json) into
    samples_map[sample_id]['characterization']['surface_functional_groups']['NO3'],
    but parse_markdown() never created that 'surface_functional_groups' key on
    any sample. The merge code's own guard
    (`if 'surface_functional_groups' in ... and 'NO3' in ...`) then silently
    skipped every sample, so ftir_peak_present was never set for anyone.

    That flag also gates whether the >=700 cm-1 (NO3) Raman peaks from
    img-4.json get appended to a sample's raman_peaks_cm-1 list, so the bug
    silently disabled that merge too, for every sample, regardless of what
    the FTIR data actually said.
    """
    metadata, samples_data = me.parse_markdown(MD_FILE)
    image_jsons_map = _load_image_jsons_map()
    result = me.merge_data(metadata, samples_data, image_jsons_map)
    by_id = {s["sample_id"]: s for s in result["samples"]}

    # img-2.json's panel_a band_labels include "NO3", and ratio "1:2" is one of
    # the ratios where the paper says the NO3 peak is still present for Ce3+.
    ftir_flag = by_id["Ce3+_1-2_RT"]["characterization"]["surface_functional_groups"]["NO3"]["ftir_peak_present"]
    assert ftir_flag is True

    # With the FTIR flag set, the Raman NO3 peaks (>=700 cm-1, from img-4.json)
    # must be appended alongside the F2g/D peaks (<700 cm-1) for the 1:2 ratio
    # samples that the paper's Raman analysis was restricted to.
    raman_peaks = by_id["Ce3+_1-2_RT"]["characterization"]["raman_peaks_cm-1"]
    assert raman_peaks == [460, 600, 750, 1050, 1350], raman_peaks


if __name__ == "__main__":
    test_table1_is_actually_parsed()
    test_table1_values_match_known_reference()
    test_missing_trailing_crystallinity_cell_is_none_not_empty_string()
    test_ftir_no3_presence_and_downstream_raman_peaks_are_merged()
    print("All tests passed.")
