import itertools 
from itertools import combinations_with_replacement

### 1. counting duplicates

def count_duplicate(string):
    string = string.upper()
    count = 0
    for x in set(string):
        #print(x)
        n = string.count(x)
        if n > 1:
            count += 1

    return count

string = input()
c = count_duplicate(string)
print(c)


#string = "counting"
#for x in set(string):
#    print(x)



### 2. multiplicative persistence

def multi_persis(n):
    num = 0
    
    while n >= 10:
        prod = 1
        for i in str(n):
            prod = prod * int(i)
            n = prod
        
        num += 1

    return num



#n = int(input())
#mp = multi_persis(n)
#print(mp)


### part II
n = int(input())
l = []
dic = {}
i = 1
for e in range(10, n+1):
    mp = multi_persis(e)
    l.append(mp)
    
    dic[e] = mp

#print(l)

l.reverse()
print(max(l))
#print(l.index(max(l)))
print(n-l.index(max(l)))
#print((dic))





### 3. systematic testing
def test_999():
    assert multi_persis(999) == 4

def test_39():
    assert multi_persis(39) == 3

### 4. test driven development
def test_atggctt():
    assert count_duplicate("atggctt") == 2

string = "ATGGCTTTCTTGAAGAGTTTCCCATTCTACGCTTTCTTGTGCTTCGGACAATACTTCGTGGCTGTGACTCACGCAGACAACTTCCCATGCTCTAAGTTGACCAACAGGACCATCGGTAAT"
#print(count_duplicate(string))

def test_ATGGCTTTCTTGAAGAGTTTCCCATTCTACGCTTTCTTGTGCTTCGGACAATACTTCGTGGCTGTGACTCACGCAGACAACTTCCCATGCTCTAAGTTGACCAACAGGACCATCGGTAAT():
    assert count_duplicate(string) == 4

### 5. counting DNA basepairs
def clean_up(string):
    string = string.upper()
    dna = []
    letters = set("ACGT")
    l = string.split()
    #print(l)
    for i in l:
        
        if count_duplicate(i) == 4:
            dna.append(i)

    dna = "".join(dna)

    return dna



raw_data = """
ENA|AAF26411|AAF26411.1 TGEV spike protein expression construct truncated spike protein
ATGGCTTTCTTGAAGAGTTTCCCATTCTACGCTTTCTTGTGCTTCGGACAATACTTCGTG
GCTGTGACTCACGCAGACAACTTCCCATGCTCTAAGTTGACCAACAGGACCATCGGTAAT
CAATGGAACTTGATCGAGACCTTCTTGTTGAACTACTCATCTAGGTTGCCACCAAACTCT
GACGACGTGTTGGGTGACTACTTCCCAACTGTGCAACCTTGGTTCAACTGCATCAGGAAC
AACTCTAACGACTTGTACGTGACTTTGGAGAACTTGAAGGCTCTCTACTGGGACTACGCT
ACTGAGAACATCACCTGGAACCACAGGCAAAGGTTGAACGTGGTGGTGAACGGATACCCA
TACAGTATCACAGTGACAACAACCCGCAACTTCAACTCTGCTGAGGGTGCTATTATCTGC
ATTTGCAAGGGAAGTCCACCAACTACCACCACCGAGTCTAGTTTGACTTGCAACTGGGGA
AGTGAGTGCAGGTTGAACCACAAGTTCCCTATCTGTCCATCTAACTCAGAGGCAAACTGC
GGAAACATGCTGTACGGCTTGCAATGGTTCGCAGACGAGGTGGTGGCTTACTTGCATGGA
GCTAGTTACCGGATTAGTTTCGAGAACCAATGGTCTGGCACTGTGACATTCGGTGACATG
CGGGCCACAACATTGGAGGTGGCTGGCACGTTGGTGGACTTGTGGTGGTTCAACCCAGTG
TACGATGTCAGTTACTACAGGGTGAACAACAAGAACGGGACTACCGTGGTGAGCAACTGC
ACTGACCAATGCGCTAGTTACGTGGCTAACGTGTTCACTACACAGCCAGGAGGATTCATC
CCATCAGACTTTAGTTTCAACAACTGGTTCCTCTTGACTAACAGCAGCACTTTGGTGAGT
GGTAAGTTGGTGACCAAGCAGCCGTTGCTCGTTAACTGCTTGTGGCCAGTCCCAAGCTTC
GAGGAGGCAGCTTCTACATTCTGCTTCGAGGGAGCTGGCTTCGACCAATGCAATGGAGCT
GTGCTCAACAATACTGTGGACGTGATTAGGTTCAACCTCAACTTCACTACAAACGTGCAA
TCAGGGAAGGGTGCCACAGTGTTCTCATTGAACACAACCGGTGGAGTCACTCTCGAGATT
TCATGCTACACAGTGAGTGACTCGAGCTTCTTCAGTTACGGAGAGATTCCGTTCGGCGTG
ACTGACGGACCACGGTACTGCTACGTGCACTACAACGGCACAGCTCTCAAGTACCTCGGA
ACACTCCCACCTAGTGTGAAGGAGATTGCTATCAGTAAGTGGGGCCACTTCTACATTAAC
GGTTACAACTTCTTCAGCACATTCCCAATTGACTGCATCTCATTCAACTTGACCACTGGT
GACAGTGACGTGTTCTGGACAATCGCTTACACAAGCTACACTGAGGCACTCGTGCAAGTT
GAGAACACAGCTATTACAAAGGTGACGTACTGCAACAGTCACGTTAACAACATTAAGTGC
TCTCAAATTACTGCTAACTTGAACAACGGATTCTACCCTGTTTCTTCAAGTGAGGTTGGA
CTCGTGAACAAGAGTGTTGTGCTCCTCCCAAGCTTCTACACACACACCATTGTGAACATC
ACTATTGGGCTCGGAATGAAGCGTAGTGGGTACGGGCAACCAATCGCCTCAACATTGAGT
AACATCACATTGCCAATGCAGGACCACAACACCGATGTGTACTGCATTCGGTCTGACCAA
TTCTCAGTTTACGTGCATTCTACTTGCAAGAGTGCTTTGTGGGACAATATTTTCAAGCGA
AACTGCACGGACCACCACCATCACCATCACTAA """


dna = clean_up(raw_data)
#print(dna)

### 6. GC content
occ_A = dna.count("A")
occ_C = dna.count("C")
occ_G = dna.count("G")
occ_T = dna.count("T")

#print(occ_A)
#print(occ_C)
#print(occ_G)
#print(occ_T)

gc_content = (occ_C + occ_G)/len(dna) 
print(gc_content)



### 7. k-mers
def list_kmers(seq, k):
    l = []

    
    for i in range(len(seq)-k+1):
        l.append(seq[i:i+k])

    return l

#seq = "ACGTCCCC"
#k = int(input())
#l = list_kmers(seq,k)
#print(l)

def test_ACGTCCCC():
    assert list_kmers("ACGTCCCC",10) == []

def test_ACGTCCCG():
    assert list_kmers("ACGTCCCG",3) == ['ACG', 'CGT', 'GTC', 'TCC', 'CCC', 'CCG']

### unique k-mers
def number_of_unique_kmers(seq, k):
    
    l = list_kmers(seq, k)    
    count = 0

    for i in l:
        if l.count(i) < 2:
            count += 1

    return count

#seq = "ACGTCCCC"
#k = int(input())
#count = number_of_unique_kmers(seq,k)
#print(count)


def test_number_ACGTCCCC():
    assert number_of_unique_kmers("ACGTCCCC",10) == 0

def test_number_AAAA():
    assert number_of_unique_kmers("AAAA",2) == 0

def test_number2_ACGTCCCCC():
    assert number_of_unique_kmers("ACGTCCCC",3) == 4


### 8. integer encoding of k-mers

def kmer_code(kmer):
    kmer = kmer.upper()
    n = len(kmer)
    dic = {'A': 0, 'C': 1, 'G': 2, 'T' : 3}
    
    l = []
    for index, i in enumerate(list(kmer)):
        l.append(dic[i]*4**(n-index-1))


    #code = sum(l)
    return sum(l)

kmer = "ACGT"
encoding = kmer_code(kmer)
#print(encoding)

### 9.  canonical codes
def canonical_code(kmer):
    rev_kmer = list(kmer)
    for i, x in enumerate(kmer):
        if x == 'A':
            rev_kmer[i] = 'T'
        elif x == 'T':
            rev_kmer[i] = 'A'
        elif x == 'C':
            rev_kmer[i] = 'G'
        elif x == 'G':
            rev_kmer[i] = 'C'

    rev_kmer = "".join(rev_kmer)[::-1]
    

    return max(kmer_code(kmer), kmer_code(rev_kmer))

kmer = "AAAC"
code = canonical_code(kmer)
#print(code)

#def diff_canonical_code(k)

L = ['A', 'C', 'G', 'T']
l = []
comb = combinations_with_replacement(L, 2)
for s in comb:
    s = "".join(s)
    #code = canonical_code(s)
    #l.append(code)
    print(s)
    #print(type(s))

### for given k value, we will have 2^(2k-1) canonical codes
