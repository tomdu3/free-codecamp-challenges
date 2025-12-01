import pytest
from complementary_dna import complementary_dna

def test_complementary_dna_examples():
    assert complementary_dna("ACGT") == "TGCA"
    assert complementary_dna("ATGCGTACGTTAGC") == "TACGCATGCAATCG"
    assert complementary_dna("GGCTTACGATCGAAG") == "CCGAATGCTAGCTTC"
    assert complementary_dna("GATCTAGCTAGGCTAGCTAG") == "CTAGATCGATCCGATCGATC"