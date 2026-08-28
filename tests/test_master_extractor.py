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
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import master_extractor as me

PAPER_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "Input_Md_Images", "0220_CMP_Slurries", "1_k9dmxr",
)
MD_FILE = os.path.join(PAPER_DIR, "1_k9dmxr.md")


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


if __name__ == "__main__":
    test_table1_is_actually_parsed()
    test_table1_values_match_known_reference()
    test_missing_trailing_crystallinity_cell_is_none_not_empty_string()
    print("All tests passed.")
