'''
 A given rucksack always has the same number of items in each of its two compartments, 
 so the first half of the characters represent items in the first compartment, 
 while the second half of the characters represent items in the second compartment.


    Lowercase item types 'a' through 'z' have priorities 1 through 26.
    Uppercase item types 'A' through 'Z' have priorities 27 through 52.

'''

###  PART 1. Rucksack -------------------------------------------------------------------------------------------------

### Defining a function to get priority sum of elements (letters) that are repeated in both 
### compartments of a given rucksack ----------------------------------------------------------------------------------

def priority(rucksack_list):
    priority_sum = 0

    for line in rucksack_list:

        ### removing the '\n' new line from a string and returning rest of the string --------------------------
        line = line.strip()   
        ### for example: line = sfDRhjhHsHhgWPJvPmmQnmPqnW (first element of the list l) -------------------------      

        l = list(set(line[0:int(len(line)/2)]).intersection(set(line[int(len(line)/2):])))
        #print((l))  ### ['W'] for first element of list

        '''
        1. line[0:int(len(line)/2)], line[int(len(line)/2):]): returning first half and last half of the string resp. ------------
        2. applying intersection for getting common letter in both compartment. we need to convert it into set --------------
        3. storing or converting the set back to a list
        '''

        ### since rucksack is case sensitive, we need to consider 'A' and 'a' as different strings -------------------------

        if l[0].isupper() == True: 
            priority_sum += ord(l[0]) - 38  ### for 'A': 65 - 38 = 27
        else:
            priority_sum += ord(l[0]) - 96

    return priority_sum


### PART 2. groups --------------------------------------------------------------------------------------------------------
### Every set of three lines in your list corresponds to a single group, 
### but each group can have a different badge item type --------------------------------------------------------------------

### defining a function that calculate priority sum
### by diving a list of rucksack into group of 3 elements ---------------------------------------------------------------

def priority_bygroup(rucksack_list):

    priority_sum_bygroup = 0
    i = 0

    while i < len(rucksack_list):
        sub_l = rucksack_list[i:i+3] ### list of first 3 elements of rucksack_list (one group)-------------------------------------
        #print(sub_l)                ### ['sfDRhjhHsHhgWPJvPmmQnmPqnW\n', 'pTddGVwcpMTTCdnQJqqQqqqVtVms\n', 'MdZCZGdcrCNRFZRhFssL\n']

        s = list(set(sub_l[0].strip()).intersection(set(sub_l[1])).intersection(set(sub_l[2])))
        #print(sub_l[0])
        #print(sub_l[1])
        ### s: common letter found in a group of 3 --------------------------------------------------------------------------

        #print(s)
        if s[0].isupper() == True:
            priority_sum_bygroup += ord(s[0]) - 38
        else:
            priority_sum_bygroup += ord(s[0]) - 96


        i += 3

    return priority_sum_bygroup
 

with open('day03.txt', 'rt') as myfile:
        rucksack_list = myfile.readlines()
        #print(rucksack_list)   ### ['sfDRhjhHsHhgWPJvPmmQnmPqnW\n', 'pTddGVwcpMTTCdnQJqqQqqqVtVms\n', ... ] -----------------
        print(priority(rucksack_list))
        print(priority_bygroup(rucksack_list))

