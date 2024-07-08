
import csv
"""
 Moving crates from one stack to another.
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
 PART 1: After the rearrangement procedure completes, what crate ends up on top of each stack?
         Start picking the crates from the top

"""

### function that returns list of all digits in a string -------------------------------------------------------------------- 
def extract_digits(index, list_of_lines):
    num = []

    for j in list_of_lines[index].split(): ### starting from lines 10 in the input data ---------------------------------------------
        #print(j)
        #print(j.isdigit()) ### ['move', '3', 'from', '2', 'to', '1']
        if j.isdigit() == True:
            num.append(int(j))

    return num

### function for rearranging the crates using CreateMover 9000 --------------------------------------------------------
def CrateMover_9000(l, data):
    
    for k in range(l[0]): ### as we need to move l[0] number of crates from stack l[1] to stack l[2] ------------------------------
            data[l[2]].insert(0,data[l[1]][0]) ### inserting crate at position 0 (picking up crate from the top of l[1]) one by one--------------
                                               ### from stack l[1] to l[2] -------------------------------------------------------------
            data[l[1]].pop(0) ### poping the moved element from l[1] -------------------------------------------------------------------------
            #print("yes")
        #print(dic)

    return data

### function for rearranging the crates using CreateMover 90001 --------------------------------------------------------
def CrateMover_90001(l, data):
    for k in range(l[0]-1, -1, -1): ### as we need to move l[0] number of crates from stack l[1] to stack l[2] ----------------
        """
        lets say We want move 3 crates from stack 2 to 1. Now this new crateMover 9001, it can pick 3 crates all at once
        so, it will pick first three elements from list (stack 2) (thats why it is iterating in the range: (2,1,0)) and insert those
        first three elements in the same order, in list of stack 1.

        for eg.: stack 2 = [1,2,3,4,5,6], stack 1: [2,3] => stack 2 = [4,5,6], stack 1 = [1,2,3,2,3]
        inserting element at 2nd index in stack 2, into stack 1 at position 0. loop goes on till k = 0
        """

        data[l[2]].insert(0,data[l[1]][k]) ### inserting element at kth index of stack, to the other stack at position 0 ---------- 
        data[l[1]].pop(k) ### removing the element at kth index -------------------------------------------------------------
        #print("yes")
    return data

### function that returns the letters of the crates that are at the top of all the stacks ----------------------------------

def top_crates(data):
    message = "" ### storing the letters

    for value in data.values():
        #print("yes")
        #print(type(value[0]))
        #print(value[0].replace('[','').replace(']',''))
        message += value[0].replace('[','').replace(']','') ### replacing first elements of all list values and [H] -> H----------
                                                            ### adding the result in empty string ------------------------------
    return message


        
                

### 1. moving crates

### Parsing data manually in a dictionary ----------------------------------------------------------------------------
### values are list type. crates inside these lists are placed from top to bottom -----------------------------
### i.e. dic[1][0] == top crate of stack 1 -----------------------------------------------------------------

dic = {1: ['[H]','[L]','[R]','[F]','[B]','[C]','[J]','[M]'], 2: ['[D]','[C]','[Z]'], 3: ['[W]','[G]','[N]','[C]','[F]','[J]','[H]'], 4: ['[B]','[S]','[T]','[M]','[D]','[J]','[P]'], 5: ['[J]','[R]','[D]','[C]','[N]'], 6: ['[Z]','[G]',
'[J]',
'[P]',
'[Q]',
'[D]',
'[L]',
'[W]'], 7: ['[H]',
'[R]',
'[F]',
'[T]',
'[Z]',
'[P]'], 8: ['[G]',
'[M]',
'[V]',
'[L]'], 9: ['[J]',
'[R]',
'[Q]',
'[F]',
'[P]',
'[G]',
'[B]',
'[C]']}

with open('day05.txt', 'rt') as myfile:
    digits = myfile.readlines()
    #print(digits)  ### ['[H]                 [Z]         [J]\n', '[L]     [W] [B]     [G]         [R]\n', ...]
                    ### list of lines

    
    ### PART 1. ---------------------------------------------------------------------------------------------------------------  
    
    i = 10 ### Start reading the file from line 10 ----------------------------------------------------------------------------
    while i < len(digits):
        #print(digits[i])
        #print(type(digits[i]))

        #print(digits[i].split())

        num = extract_digits(i, digits)

        dic1 = CrateMover_9000(num, dic)

        #dic2 = rearrange2(num, dic)

        i += 1

    print(top_crates(dic1))

    ### PART 1. is finished ------------------------------------------------------------------------------
    
    print("NOTE: Run one part at a time and comment other part. Otherwise, it will give error!")
    
    ### PART 2. --------------------------------------------------------------------------------------------

    i = 10 ### Start reading the file from line 10 ----------------------------------------------------------------------------
    while i < len(digits):
        #print(digits[i])
        #print(type(digits[i]))

        #print(digits[i].split())

        num = extract_digits(i, digits)

        dic2 = CrateMover_90001(num, dic)

        i += 1

    print(top_crates(dic2))
    