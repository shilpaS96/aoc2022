"""
PART 1: For example, to move the 1 in a sequence like 4, 5, 6, 1, 7, 8, 9, the 1 moves one position forward: 
4, 5, 6, 7, 1, 8, 9. 
To move the -2 in a sequence like 4, -2, 5, 6, 7, 8, 9, the -2 moves two positions backward, 
wrapping around: 4, 5, 6, 7, 8, -2, 9

Initial arrangement:
1, 2, -3, 3, -2, 0, 4

1 moves between 2 and -3:
2, 1, -3, 3, -2, 0, 4

2 moves between -3 and 3:
1, -3, 2, 3, -2, 0, 4

-3 moves between -2 and 0:
1, 2, 3, -2, -3, 0, 4

3 moves between 0 and 4:
1, 2, -2, -3, 0, 3, 4

-2 moves between 4 and 1:
1, 2, -3, 0, 3, 4, -2

0 does not move:
1, 2, -3, 0, 3, 4, -2

4 moves between -3 and 0:
1, 2, -3, 4, 0, 3, -2

output: the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers 
after the value 0. What is the sum of the three numbers that form the grove coordinates?


PART 2: First, you need to apply the decryption key, 811589153. 
Multiply each number by the decryption key before you begin

output: Second, you need to mix the list of numbers ten times
"""

### define function that returns final mixed list ----------------------------------------------------------
def move(list, part):
    #seen = set()
    ### list = [(1, 0), (2, 1), (-3, 2), (3, 3), (-2, 4), (0, 5), (4, 6)] ------------------------------
    length = len(list)
    #print(length) ### for instance: length = 7 --------------------------------------------------------


    if part == 1: ### for part 1 -----------------------------------------------------------------------
        for i in range(len(list)):
            #print(i)
            for l in list: 
                if l[1] == i: ### taking elements in the increasing index order --------------------------
                    #print('yes', i, l)
                    ind = list.index(l) ### current position of l in list --------------------------------

                    if l[0] < 0: ### move left -----------------------------------------------------------
                        for j in range(abs(l[0])): ### one step to left until j reaches abs(l[0]) --------
                            list[ind], list[(ind-1)%length] = list[(ind-1)%length], list[ind]
                            ind = (ind-1) % length ### update index of l after swapping -------------------

                    elif l[0] > 0: ### move right ---------------------------------------------------------
                        for j in range(l[0]): ### one step to left until j reaches (l[0]) -----------------
                            list[ind], list[(ind+1)%length] = list[(ind+1)%length], list[ind]
                            
                            ind = (ind+1) % length ### ### update index of l after swapping -------------------
                #print(list)

                    break

    elif part == 2:

        for i in range(len(list)):
            print(i)
            for l in list: 
                if l[1] == i:
                    #print('yes', i, l)
                    ind = list.index(l)

                    new_l = l[0] % (length-1) 
                    ### logic from: https://github.com/womogenes/AoC-2022-Solutions/blob/main/day_20/day_20_p2.py 

                    if new_l < 0: ### move left --------------------------------------------------------
                        for j in range(abs(new_l)):
                            list[ind], list[(ind-1)%length] = list[(ind-1)%length], list[ind]
                            #list = swaping_elements(list, ind, (ind-1)%length)
                            ind = (ind-1) % length

                    elif new_l > 0:
                        for j in range(new_l):
                            list[ind], list[(ind+1)%length] = list[(ind+1)%length], list[ind]
                            #list = swaping_elements(list, ind, (ind+1)%length)
                            ind = (ind+1) % length
                #print(list)

                    break


    return list

                


with open('day20.txt', 'rt') as myfile:
    lines = myfile.read().split()
    #print(lines) ### ['1', '2', '-3', '3', '-2', '0', '4'] ------------------------------------------------

    ### PART 1. --------------------------------------------------------------------------------------------

    for i in range(len(lines)): ### converting a digit into int and appending its index and 
                                ### then updating the list lines ------------------------------------------
        lines[i] = (int(lines[i]),i)

    #print(lines) ### [(1, 0), (2, 1), (-3, 2), (3, 3), (-2, 4), (0, 5), (4, 6)] ----------------------------
    #print(move(lines))
    final_l = move(lines, 1)
    #print('final list is: ')
    #print(final_l) ### [(-2, 4), (1, 0), (2, 1), (-3, 2), (4, 6), (0, 5), (3, 3)] ---------------------------
    #print(len(final_l))

    for l in final_l:
        #print(l)
        if l[0] == 0: ### search for index of 0 element in the list -----------------------------------------------
            index_zero = final_l.index(l)
            #print(index_zero)
            
            break


    print(final_l[(index_zero+1000) % len(final_l)][0]) ### 1000th element after 0 -------------------------
    print(final_l[(index_zero+2000) % len(final_l)][0]) ### 2000th element after 0 -------------------------
    print(final_l[(index_zero+3000) % len(final_l)][0]) ### 3000th element after 0 -------------------------

    Part1 = (final_l[(index_zero+1000) % len(final_l)][0] + final_l[(index_zero+2000) % len(final_l)][0] + final_l[(index_zero+3000) % len(final_l)][0])
    
    

### PART 2. -----------------------------------------------------------------------------------------------

with open('day20.txt', 'rt') as myfile:
    lines = myfile.read().split()
    #print(lines)

    for i in range(len(lines)): ### converting a digit into int, Multiply each number by the decryption key  
                                ### appending its index and then updating the list lines --------------------
        lines[i] = (int(lines[i]) * 811589153,i)

    #print(lines)

    for round in range(10): ### running it for 10 times ---------------------------------------------------
        lines = move(lines, 2)

    #print(lines)

    for l in lines:
        #print(l)
        if l[0] == 0:
            index_zero = lines.index(l)
            print(index_zero)
            
            break

    Part2 = (lines[(index_zero+1000) % len(lines)][0] + lines[(index_zero+2000) % len(lines)][0] + lines[(index_zero+3000) % len(lines)][0])
     
    print('Part1 and Part2 are: ', Part1, Part2)

