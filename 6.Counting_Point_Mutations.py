## count how many corresponding bases are different between two equal length
## DNA strings

def hamming_distance(infile):
    # read in the file contains two two lines of dna
    with open(infile) as f:
        s = f.readline().strip()
        t = f.readline().strip()
        print s, t
        hamming_dist = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                hamming_dist = hamming_dist + 1
            else:
                pass
    return hamming_dist


## some really nice solutions using list comprehension
# s1 = 'GAGCCTACTAACGGGAT'
# s2 = 'CATCGTAATGACGGCCT'
# print [ a!=b for (a, b) in zip(s1, s2)].count(True)
# sum([a != b for a, b in zip(s1, s2)])
