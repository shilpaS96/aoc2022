
"""
def fibonacci_generator():
    small, large = 0,1
    while True:
        yield small
        (small, large) = (large, small+large)

F = fibonacci_generator()
print([next(F) for _ in range(3)])
"""


### 1. Generator functions
## i. factorials
def fact():
    last_fact, n = 1, 0
    while True:
        yield last_fact
        n = n+1
        last_fact = last_fact*n

Fact = fact()
#print([next(Fact) for _ in range(7)])


## ii. Triangular

def triangular():
    T_num, n = 0, 0
    while True:
        yield T_num
        n = n+1
        T_num = T_num + n

Triangular_num = triangular()
#print([next(Triangular_num) for _ in range(5)])




### 2. Baconian Code
## i.

def Bac_code_structure(filename):
    with open(filename, "rt") as f:
        #l = f.read().strip().split()
        #print((l))
        l = f.readlines()
        #l.strip().split("\t")
        Bacon_code = dict()

        for line in l:
            key, val = line.strip().split("\t")
            #print(line)
            #print(key, val)
            Bacon_code[key] = int(val,2)
            #print(val)

        #for line in l:
    assert len(Bacon_code) == 26
    assert len(set(Bacon_code.values())) == 26
            


    #print(Bacon_code)
    return Bacon_code


Bacon_code = Bac_code_structure("cipher.txt")
#print(Bacon_code)
#print(Bacon_code['A'])

## ii. convert string to byte array 

def str_to_bytearray(string, Bacon_code):
    baconian_bytearray = bytearray()
      #print(string)
    string = list(string.upper())
    for x in string:
     #   print(x)
        if x != ' ':
            baconian_bytearray.extend([Bacon_code[x]])
        #    print(baconian_list)
    return baconian_bytearray

#string = input()
#byte_array = str_to_bytearray(string,Bacon_code)
#print(str_to_bytearray(string,Bacon_code))
#print(type(str_to_bytearray(string,Bacon_code)))

## iii. bytearray to decoded string

def byterarray_to_string(byte_array):
    string = []
    for b in byte_array:
        p = (list(Bacon_code.values()).index(b))
        string.append(list(Bacon_code.keys())[p])
        #print(list(Bacon_code.keys())[p])
        #print(string)

    return ''.join(string)

#print(byterarray_to_string(byte_array))

## iv. binary code file

def encode_msg(Message):
    #Message = Message.upper()
    byte_array = str_to_bytearray(Message,Bacon_code)

    with open("EncodedMessage.txt", 'wb') as f:

        #for b in byte_array:           
        f.write(byte_array)

Message = input()
encode_msg(Message)

def decode_msg(filename):
    with open(filename, 'rb') as f:
        line = f.read()
        decoded = byterarray_to_string(line)

    return decoded

m = decode_msg("EncodedMessage.txt")
#print(m)




### 3. Advent of code: Day 04

## part I

with open("input04.txt", 'rt') as f:
    lines = f.read().split("\n")
    #print(lines)
    #print(type(lines))
    count = 0
    #list = []
    for l in lines:
        list = []
        print(l)
        for i in l.split():
            print(i)
            list.append(l.split().count(i))
        print(list)
        if max(list) == 1:
            count += 1
                
        #print(list(l))
#print(count)
#    for l in f.readlines():
#        print(l)


## part II
def analog_count(word_list):
    count = 0
    for i, x in enumerate(word_list):
        for j, y in enumerate(word_list):
            if sorted(x) == sorted(y) and i!=j:
                count += 1
    return count

list = ["nyot", "babgr", "babgr", "kqtu", "kqtu", "kzshonp", "ylyk", "psqk"]
#print(analog_count(list))

def passphrases():
    valid_passphrase = 0
    with open("input04.txt", 'rt') as f:
        lines = f.read().split("\n")

        for l in lines:
            #list = []
            #print(l)
            ana_count = analog_count(l.split())
            if ana_count == 0:
                valid_passphrase += 1
    return valid_passphrase 

    
print(passphrases())
