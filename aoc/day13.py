"""
Test data:
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]

PART 1: What are the indices of the pairs that are already in the right order? 
output: What is the sum of the indices of those pairs?

"""


### Idea taken from: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/13.py ----------------

### function to compare elements of list  -----------------------------------------------------------------------------

def compare_elts(l, r):
    if type(l) == int and type(r) == int:
        #print('both are int')
        if l < r: ### left element is lesser than right element -----------------------------------------------------------
            return 'True'
        elif l == r: ### both are same. move to next if list is not ended -----------------------------------------------------
            return 0 
        else: ### right element is lesser than left ----------------------------------------------------------------------------
            return 'False'

    elif type(l) == list and type(r) == list:
        #print('both are list')
        #print(l, r)
        for i in range(min(len(l), len(r))): 
            ce = compare_elts(l[i], r[i])
            if ce == 'True': ### if l[i] < r[i]
                return 'True'
            elif ce == 'False': ### if l[i] > r[i]
                return 'False'

        ### if none of the above condition inside the for loop is true then: ---------------------------------------------------- 
        if len(l) < len(r): 
            return 'True'
        elif len(l) > len(r):
            return 'False'
        else: return 0

    elif type(l) == int and type(r) == list:
        #print('both are diff')
        ce = compare_elts([l], r)
        return ce
    else:
        ce = compare_elts(l, [r])
        return ce
 
### PART 1.  -------------------------------------------------------------------------------------------------------------

with open('day13.txt', 'rt') as myfile:
    lines = myfile.read().split()
    #print(lines) ### ['[[[[4,7,7],0,4,[6,3,3,7,10],2],2,[[3]]],[]]', '[[[[1,4,8],[3,3,1,4]]]]', ... ]

    for index, l in enumerate(lines):
        lines[index] = eval(l)    ### to convert string type list into list type  ------------------------
        ### for instance: '[[[[4,7,7],0,4,[6,3,3,7,10],2],2,[[3]]],[]]' -> [[[[4,7,7],0,4,[6,3,3,7,10],2],2,[[3]]],[]]

    count = 0 ### indices of pairs that are in right order ---------------------------------------------------
    i = 0 ### first element of a pair ------------------------------------------------------------------------
    j = 1 ### second element of a pair -----------------------------------------------------------------------
    pair = 1 ### since pair index starts from 0 --------------------------------------------------------------
    while i<len(lines) and j<len(lines):
        #print('we are finding, dont worry', j)

        ### pair of lists at index i and j -------------------------------------------------------------------
        ll = lines[i]
        rl = lines[j]

        #print(ll, rl)
        #print(type(ll), type(rl))

        if len(ll) == 0: ### if left list is empty then it is in right order ---------------------------------------------------
            count += pair
            
        #    print(count)

        elif len(rl) == 0 and len(ll) > 0: ### if right list is empty but left list isn't then not in right order --------------
            i += 2
            j += 2
            pair += 1
            continue

        elif len(ll) > 0 and len(rl) > 0:
            cc = compare_elts(ll, rl)
            #print(cc)

            if cc == 'True' or cc == 0:
                #print('found one pair', j)
                count += pair


        i += 2
        j += 2
        pair += 1

    print(count)

    ### PART 2.  ----------------------------------------------------------------------------------------------------------

    """
    Organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.
    Afterward, locate the divider packets.
    for instnace: the divider packets are 10th and 14th, and so the decoder key is 140.
    """

    for i in range(len(lines)):
        for j in range(len(lines)):
            cc = compare_elts(lines[i], lines[j])  ### sorting packings as a list -----------------------------------------------

            if cc == 'False': ### lines[i] > lines[j] ---------------------------------------------------------------------------
                lines[i], lines[j] = lines[j], lines[i]   ### swaping the elements ----------------------------------------------

    lines.reverse()  ### taking reverse of list to get it in an increasing order -----------------------------------------------
    #print(lines)


####  inserting divider ----------------------------------------------------------------------------------------------------

    for index, l in enumerate(lines):  #### inserting divider [[2]]  --------------------------------------------------------
        
        #print(l)
        cc2 = compare_elts(l, [[2]])
        #print(cc2)

        if cc2 == 'False': ### l > [[2]] -------------------------------------------------------------------------------------
            #print('inserting')
            lines.insert(index, [[2]])
            divider1 = index + 1 ### since index starts from 0 in python -----------------------------------------------------
            break

    for index, l in enumerate(lines):  #### inserting divider [[6]]  -----------------------------------------------------
        
        #print(l)
        cc6 = compare_elts(l, [[6]])

        

        if cc6 == 'False':
         #   print('inserting')
            lines.insert(index, [[6]])
            divider2 = index + 1 
            break

    #print(lines)

    print(divider1 * divider2)





