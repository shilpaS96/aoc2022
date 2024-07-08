
#from day03 import *
from collections import Counter


#with open("sequence.fasta", "rt") as myfile:
#    digits = myfile.read().strip()

#print(digits)

### 1. function that reads the .fasta file

def readfasta(file_name):
    with open(file_name, "rt") as file:
        digits = file.readlines()[1:]
        #l = digits.split()

    #dna = file.readlines()
    
    dna = "".join(digits).split()
    dna = "".join(dna)
    #dna_seq = clean_up(digits)

    return (dna)

dna = readfasta("sequence.fasta")
#l = clean_up(digits)
print((dna))
print(Counter(dna))

#print(readfasta("sequence.fasta"))


#file = open('sequence.fasta')
#dna = (readfasta("sequence.fasta"))
#print(dna)
#print(dna.isspace())


### 2. Genetic code: function to store codon to aa

def Pro_Codon(file_name):
    with open(file_name, "rt") as myfile:
        digits = myfile.readlines()

    pro_codon = dict()
    for l in digits:
    #print(l)
        k, codon = l.strip().split(":")
        #print(k)
        if k == "STOP":
            break
    #print(k,value)
    #print(type(value.split(" ")))
        for Codon in codon.strip().split(" "):
        #print(Codon)
            pro_codon[Codon] = k

    
    return pro_codon


dic = Pro_Codon("04-genetic-code.txt")
#print(dic)


    #print((digits))


#with open("04-genetic-code.txt", "rt") as myfile:
#    digits = myfile.readlines()

"""
### only sample code which is already used inside the function Pro_Codon
pro_codon = dict()
#print((digits))
for l in digits:
    #print(l)
    k, codon = l.strip().split(":")
    print(k)
    if k == "STOP":
        break
    #print(k,value)
    #print(type(value.split(" ")))
    for Codon in codon.strip().split(" "):
        #print(Codon)
        pro_codon[Codon] = k

print(pro_codon)

#key, codon = digits.split("\n")



#print((digits))
pro_codon = {}
#print((digits))
for l in digits.split("\n"):
    #print(type(l))
    P, Codon = l.strip().split(":")
    print(P, Codon)
    print((Codon).split(" "))

    #pro_codon[P.strip()] = Codon.strip()

    #print(l)
#print(pro_codon)
"""


### DNA to protein sequence upto stop condition

def dna_to_aa(dna_seq, dic):
    dna_aa = []
    j = dna_seq.find('ATG')
    #print(j)

    #for i in range(j, len(dna_seq)):
    while 0 <= j <len(dna_seq):
        if dna_seq[j:j+3] != 'TAA' and dna_seq[j:j+3] != 'TGA' and dna_seq[j:j+3] != 'TAG':
            #print(j)
            for codon, pro in dic.items():
                #print(codon)
                if codon == dna_seq[j:j+3]:
                    dna_aa.append(pro)
                    continue
                    # = dna_seq.replace(dna_seq[j:j+3], pro)
                    #yield j

        else:
            break   
            
        j += 3

    dna_aa = "".join(dna_aa)
    #print(len(dna_aa))
    
    #for items in pro_codon.items():
    #    print(items)
    #    for i in range(len(dna_seq)):
    #        if dna_seq[i:i+3] == 'ATG':
                

#    terminatingPosition = j
    if len(dna_aa) > 0:
            return [dna_aa, j]
    else:
        return ["None",j] 



#seq = "ACATGTGTAACGT"
#seq = "ACATGTGTAACTAAATG"
#seq = "TAA"
seq = "TAGTAAATTATCATA"
a =(dna_to_aa(seq, dic))
print("protein encoding is: " + a[0])
print("protein encoding stops at: " +  str(a[1]))
#print(l)



### Whole DNA to protein sequence
def wholeDNA_to_pro(seq, dic):
    
    j = 0
    with open('file.txt', 'w') as f:
        procod = dna_to_aa(seq, dic)
        #print(procod[1])
        #f.write(procod[0])
        seq = seq[j:]
        j = procod[1]
        #print(j)
        while 0<=j<len(seq) and seq.find('ATG') != -1:
            f.write(procod[0])
            f.write("\n") 
            
            seq = seq[j:]
            #print(seq)
            j = 10+100
            procod = dna_to_aa(seq, dic)
            #print(procod)
            if procod[1] == -1:
                #print("yes")
                
                break
            else:
                #print(procod[1])
                #print(procod[0])
                     
                f.write(procod[0])
                #f.write("\n")
                  
                j = procod[1] 
            #if seq.find('ATG') != -1:
            #    f.write("\n")
            #else: break

            #f.write("\n")
            #f.close()
            
            
        
    #with open('file.txt', 'w') as f:
    #    f.write(procod[0])
    #    f.write("\n")
    #    f.write('Sharma')

    f.close()

#seq = "ACATGTGTAACTAAATG"
seq = "ACATGGCTCGCTGATAGTAAATGATTATCATA"
#seq = "TAGTAAATTATCATA"

wholeDNA_to_pro(seq, dic)


### 3. advent of code: Day01

def match_sum(n):
    n = str(n)

    sum = 0

    for i, x in enumerate(list(n)):
        #print(i, x)
        if i < len(list(n))-1 and x == list(n)[i+1]:
            #print(i)
            sum += int(x)

        elif i == len(list(n))-1 and x == list(n)[0]:
            sum += int(x) 

    return sum

#n = int(input())
#count = match_sum(n)
#print(count)


### 4. advent of code: Day02

def check_sum(filename):
    sum = 0
    with open(filename, 'rt') as f:
        #lines = f.read().strip().split()
        #print(lines)
        #lines = int(lines)
        #print(type(int(lines)))
        for l in f:
            l = l.split()
            for i, x in enumerate(l):
                #i = int(i)
                l[i] = int(x)
                #print(type(l[i]))

            sum += max(l) - min(l)
            #print(l)
            #print(type(l))

    return sum

#a = check_sum("input02.txt")
#print(a)


### part II: Optinal Challenge

def row_value(numberlist):
    #y = numberlist[0]
    #short_numberlist = numberlist[1:]
    #print(short_numberlist)
    for i, x in enumerate(numberlist):
        for j, y in enumerate(numberlist):
            if (x%y == 0 or y%x == 0) and x!=y:
                return max(x/y, y/x)


#print(row_value([5, 9, 2, 8]))
def test_1():
    assert row_value([5, 9, 2, 8]) == 4

def test_2():
    assert row_value([9, 4, 7, 3]) == 3


with open("input02.txt", 'rt') as f:
        #lines = f.read().strip().split()
        #print(lines)
        #lines = int(lines)
    summ = []
        #print(type(int(lines)))
    for l in f:
        l = l.split()
        for i, x in enumerate(l):
                i = int(i)
                l[i] = int(x)
        num = row_value(l)
        summ.append(num)

    row_sum = sum(summ)


print(row_sum)



