'''
PART 1.  In how many assignment pairs does one range fully contain the other?
PART 2. In how many assignment pairs do the ranges overlap?
'''

### 1. containment between pairs ---------------------------------------------------------------------------------------

### returning whether lists are contained in one another or not ---------------------------------------------------------
def pairs_containments(list1, list2):
    if set(list1).issubset(set(list2)) == True or set(list2).issubset(set(list1)) == True:
        return 1
    
    return 0


### returning a big list using a pair of numbers in a list of length 2 -------------------------------------------------------
'''
1. this function takes input a list of digits
2. returns a full list of numbers between two digits
'''

def list_range(my_list):
    my_biglist = []
    if int(my_list[0])>int(my_list[1]): ### for instance: ['5', '2']
        return []

    if len(my_list) == 2: ### for instance: ['2', '5'] ---------------------------------------------------------
        for i in range(int(my_list[0]), int(my_list[1])+1): ### range of digits from 2 to 6, excluding 6 -----------------------
            my_biglist.append(i)
        
    return my_biglist ### [2,3,4,5]


### retruning whether 2 lists have non empty intersection -----------------------------------------------------------------
def overlap_lists(list1, list2):
    if set(list1).intersection(set(list2)) != set():
        return 1
    
    return 0


with open('day04.txt', 'rt') as myfile:
    lines = myfile.readlines()
    #print(lines)  ### ['13-53,17-82\n', '32-32,32-42\n', ... ] ---------------------------------------------
    pairs = 0
    overlaps = 0

    i = 0
    while i < len(lines):
        l1 = lines[i].strip().split(',')
        ### lines[i].strip() returns lines[i] element as a string without \n: 52-95,96-97 ----------------------------------------
        ### lines[i].strip().split(','): split the string by ',' and returns a list of elements of two in this problem ['13-53', '17-82']-------
        #print((l1))
        
        r11 = l1[0].split('-') ### ['13', '53']
        r12 = l1[1].split('-')

        #print(r11, r12)

        r11_range = list_range(r11) ### for 13-53: [13, 14, ...]
        r12_range = list_range(r12) ### for 17-82: [17, 18, ...]


        #print(r11_range)
        #print(r12_range)

        if r11_range == [] or r11_range == []:
            continue

        ### PART 1. -------------------------------------------------------------------------------------------------------------

        containing_pairs = pairs_containments(r11_range, r12_range) ### checking whether r11_range is contained in r12_range (1)------
        pairs += containing_pairs                                   ### or vice versa(1) or neither of them(0) -------------------------
        
        ### PART 2. -------------------------------------------------------------------------------------------------------------

        overlap_pairs = overlap_lists(r11_range, r12_range)
        overlaps += overlap_pairs

        i += 1

    print(pairs)
    print(overlaps)


