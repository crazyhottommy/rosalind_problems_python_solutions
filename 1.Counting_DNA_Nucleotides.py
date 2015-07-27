
# the output should be four numbers separated by a space

# the simplest solution
def count_dna_nucleotides(dna):
    a_num = dna.count("A")
    c_num = dna.count("C")
    g_num = dna.count("G")
    t_num = dna.count("T")
    print a_num, c_num, g_num, t_num


# using list comprehension
def count_dna_nucleotides_1(DNA):
    print "%d %d %d %d" % tuple([DNA.count(l) for l in "ACGT"])


# it will be a string quoted by ''

def count_dna_nucleotides_2(dna):
    counts = [dna.count(l) for l in 'ACGT']
    # need to turn the integer to string
    print " ".join(str(l) for l in counts)

# DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
# 20 12 17 21

# interesting unix one liner

# sed -e 's/\([A-Z]\)/\1\n/g' rosalind_dna.txt | sort | uniq -c | cut -d' ' -f 5 | perl -pe 's/\n/ /g'
