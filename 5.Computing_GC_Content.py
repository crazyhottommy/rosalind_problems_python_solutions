

def gc_content(dna):
    g_num = dna.count("G")
    c_num = dna.count("C")
    # floating number to get decimals
    # times 100 to get percentage
    return (g_num + c_num)/float(len(dna)) * 100

def read_fasta(infile):
    # intitate a dictionray with keys are the seq_names, and the values are the sequences
    seqs = {}
    for line in infile:
        # strip the newline at the end (if any) at the end of the line
        line = line.rstrip()
        if line.startswith(">"):
            seq_name = line[1:]
            seqs[seq_name] = ''
        else:
            seqs[seq_name] = seqs[seq_name] + line
    return seqs

try:
    infile = open("/Users/Tammy/Downloads/rosalind_gc.txt")
except IOError:
    print "File does not exist!"


seqs = read_fasta(infile)

# use list comprehension
li = [(key, gc_content(value)) for key, value in seqs.items()]

# max gc content
max(li, key=lambda x: x[1])

# sort by the second value in the tuple
# sorted(li, key=lambda x: x[1])

