# get the reverse-complement DNA sequence

def ReverseComplement1(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([seq_dict[base] for base in reversed(seq)])



# make it more robust, lower case DNA

def ReverseComplement2(seq):
    # too lazy to construct the dictionary manually, use a dict comprehension
    seq1 = 'ATCGTAGCatcgtagc'
    seq_dict = { seq1[i]:seq1[i+4] for i in range(16) if i < 4 or 8<=i<12 }
    return "".join([seq_dict[base] for base in reversed(seq)])



# make it even more robust to check the if the seq is a DNA sequence or not

def ReverseComplement3(seq):
    for base in seq:
        if base not in 'ATCGatcg':
            print "Error: NOT a DNA sequence"
            return None
    seq1 = 'ATCGTAGCatcgtagc'
    seq_dict = {seq1[i]: seq1[i+4] for i in range(16) if i < 4 or 8 <= i < 12}
    return "".join([seq_dict[base] for base in reversed(seq)])

