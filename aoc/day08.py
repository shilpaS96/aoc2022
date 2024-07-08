import math

"""
30373
25512
65332
33549
35390

1. The top-left 5 is visible from the left and top. 
 It isn't visible from the right or bottom since other trees of height 5 are in the way.

2. The center 3 is not visible from any direction; 
 for it to be visible, there would need to be only trees of at most height 2 between it and an edge.

PART 1: how many trees are visible from outside the grid?

PART 2:

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees 
    (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. 
For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2)

 What is the highest scenic score possible for any tree?

"""


with open('day08.txt', 'rt') as myfile:
    l = myfile.read().splitlines()
    #print(line.splitlines()[0])
    #print(line)

    #l = line.splitlines()
    #print((l))
    #print(len(l[0]))
    visible_trees = len(l)*2 + len(l[0]) * 2 - 4 ### edge trees always visible -------------------------------
   

    ### PART 1. --------------------------------------------------------------------------------------------

    for i in range(0, len(l)):
        l[i] = list(l[i]) ### separating digits as each digit represents a tree's height ----------------------
        #print(l)

        for j, x in enumerate(l[i]): 
            l[i][j] = int(x) ### converting it from string type to int type ---------------------------------
        
    ### l = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]] ------------

    #print(l)
    #print(l[1][0])

    ### Now, we will compare each tree along its corr row and column -------------------------------------

    for i in range(1,len(l)-1):
        
        #print(l[i])
        for j in range(1,len(l)-1):
            #print(l[i][j])
            #print((l[i][:j]))
            #print("for column is: ", [l[k][j] for k in range(0,i)])
            #print((l[i][i+1:]))

            if l[i][j] > max(l[i][:j]) or l[i][j] > max(l[i][j+1:]): ### condition for row i -----------------
                visible_trees += 1
            else:                                                    ### condition for column j -------------
                val1 = max([l[k][j] for k in range(0,i)])
                val2 = max([l[k][j] for k in range(i+1,len(l))])
                if l[i][j] > val1 or l[i][j] > val2:
                    visible_trees += 1 



    print(visible_trees)  

    ### PART 2. --------------------------------------------------------------------------------------------
    
    tree_house = []

    for i in range(1,len(l)):
        
        #print(l[i])
        for j in range(1,len(l)):
            count = 0 ### counting number of tress visible in each of the four directions --------------
            count_l = [] ### appending number of tress visible in each of the four directions --------------
            row_l1 = l[i][:j] 
            row_l1.reverse() ### taking reverse to scan it from tree l[i][j] ---------------------------
            row_l2 = l[i][j+1:] ### no need to take reverse ---------------------------------------------
            col_l1 = [l[k][j] for k in range(0,i)] 
            col_l1.reverse() ### taking reverse to scan it from tree l[i][j] ---------------------------
            col_l2 = [l[k][j] for k in range(i+1,len(l))]

            for r1 in row_l1: ### loop on list of trees which are on left of l[i][j] -----------------------
                if l[i][j] > r1:
                    #print("yes")
                    count += 1
                elif l[i][j] <= r1:
                    count += 1
                    break
                #elif l[i][j] < r1:
                #    count += 1
                #    break

                
                    #print("yes")
                    #break
            count_l.append(count)
            count = 0

            for r2 in row_l2: ### loop on list of trees which are on right of l[i][j] ------------------------
                if l[i][j] > r2:
                    #print("yes")
                    count += 1
                elif l[i][j] <= r2:
                    count += 1
                    break
                #elif l[i][j] < r2:
                #    count += 1
                #    break

                
                    #print("yes")
                    #break
            count_l.append(count)
            count = 0

            for c1 in col_l1:  ### loop on list of trees which are on top of l[i][j] ------------------
                if l[i][j] > c1:
                    #print("yes")
                    count += 1
                elif l[i][j] <= c1:
                    count += 1
                    break
                #elif l[i][j] < c1:
                #    count += 1
                #    break

                
                    #print("yes")
                    #break
            count_l.append(count)
            count = 0

            for c2 in col_l2:  ### loop on list of trees which are on bottom of l[i][j] -------------------
                if l[i][j] > c2:
                    #print("yes")
                    count += 1
                elif l[i][j] <= c2:
                    count += 1
                    break
               
            count_l.append(count)
    
            tree_house.append(math.prod(count_l))
            #count_l = []
    #print(tree_house)
    #print(len(tree_house))
    print(max(tree_house)) ### highest scenic score --------------------------------------------------




