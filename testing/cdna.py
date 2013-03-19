COMPLEMENTS = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complement(sequence):
    """
    Calculate the complementary sequence of a DNA sequence.

    @param sequence: DNA sequence expressed as a lower-case string.
    @return complementary sequence.
    """
    cdna = ''
    try:
        for ch in sequence:
            cdna += COMPLEMENTS[ch]
        return cdna
    except TypeError:
        print 'The input is not a sequence e.g. a string or list'
