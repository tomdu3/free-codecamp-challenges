def complementary_dna(strand):
    original = "ACGT"
    complement = "TGCA"
    translation_table = str.maketrans(original, complement)
    strand = strand.translate(translation_table)
    return strand