"""Unit tests for markdown file copy detection"""

from pathlib import Path
import pytest
from copydetect import CodeFingerprint, compare_files, CopyDetector

TESTS_DIR = str(Path(__file__).parent)

def test_markdown_detection():
    """Test that copy detection works with markdown files"""
    fp1 = CodeFingerprint(TESTS_DIR + "/sample_md/original.md", 25, 1)
    fp2 = CodeFingerprint(TESTS_DIR + "/sample_md/copied.md", 25, 1)
    token_overlap, similarities, slices = compare_files(fp1, fp2)
    
    # Verify that there is significant overlap between the files
    assert token_overlap > 0
    assert similarities[0] > 0.3  # At least 30% similarity
    assert similarities[1] > 0.3
    
    # Verify that the slices contain the copied sections
    assert len(slices[0]) > 0
    assert len(slices[1]) > 0

def test_markdown_detector():
    """Test that the CopyDetector class works with markdown files"""
    config = {
        "test_directories": [TESTS_DIR + "/sample_md"],
        "reference_directories": [TESTS_DIR + "/sample_md"],
        "extensions": ["md"],
        "noise_threshold": 25,
        "guarantee_threshold": 25,
        "display_threshold": 0.3,
        "silent": True
    }
    
    detector = CopyDetector.from_config(config)
    detector.run()
    
    # Verify that the similarity matrix contains non-zero values
    # (excluding self-comparisons which are -1)
    similarity_matrix = detector.similarity_matrix
    non_self_comparisons = similarity_matrix[similarity_matrix[:,:,0] != -1]
    
    assert len(non_self_comparisons) > 0
    assert non_self_comparisons.max() > 0.3
