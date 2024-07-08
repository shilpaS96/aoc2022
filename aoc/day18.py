"""
PART 1: Counting up all the sides that aren't connected to another cube.

"""

### function that returns count of non connected cubes -------------------------------------------
### for PART 1.

def adjcent_sides(X, set):
    count = 0

    for i in [-1, 1]:

        if (X[0]+i, X[1], X[2]) not in set :
            count += 1

        if (X[0], X[1] + i, X[2]) not in set:
            count += 1


        if (X[0], X[1], X[2] + i) not in set:
            count += 1

    return count

### function for PART 2. ---------------------------------------------------------------------------------
### it returns whether air goes out (1) or not (0) -------------------------------------------------------

def exterior_SA(X, pos):
    s = set() ### set of already seen points -------------------------------------------------------------
    #list = deque([X])
    list = [X]

    while len(list) != 0:
        X = list.pop()
        
        if X in pos: ### if its a lava point, we will ignore --------------------------------------------
            continue

        if X in s:
            continue

        s.add(X)

        ### if any cordinate axis goes out of the min or max, then it means air goes out -----------------
         
        if X[0] < min_x or X[0] > max_x or X[1] < min_y or X[1] > max_y or X[2] < min_z or X[2] > max_z:
            return 1   ### taking one immigiate neighbour of the lava point ---------------------------------

        for r in [-1, 1]: ### if X is not immigiate neighbor of lava point then add it into the list -------
            list.append((X[0] + r, X[1], X[2]))
            list.append((X[0], X[1] + r, X[2]))
            list.append((X[0], X[1], X[2] + r))
        
    return 0


        
############################################------------------------------------------------------------

with open('day18.txt', 'rt') as myfile:
    lines = myfile.read()
    #print(lines)
    pos = set()  ### this set will contain all 3-tuples ----------------------------------------------

    for l in lines.split('\n'):
        #print(l, type(l))
        #print(l.split(','))  ### ['2', '2', '2'] -----------------------------------------------------------
        x, y, z = l.split(',')
        #print(x, y, z)
        x, y, z = int(x), int(y), int(z)
        pos.add((x,y,z)) ### adding cube sides as tuple in a set pos ---------------------------------------  

    #print((pos))
    not_conn = 0

    ###  finding max and min of each cordinate axis --------------------------------------------------------
    x_l = [X[0] for X in pos] 
    max_x, min_x = max(x_l), min(x_l)
    #print(max_x, min_x)
    y_l = [X[1] for X in pos]
    max_y, min_y = max(y_l), min(y_l)
    z_l = [X[2] for X in pos]
    max_z, min_z = max(z_l), min(z_l)
    

    ### PART 1. ----------------------------------------------------------------------------------

    for p in pos:
        #print(p)
        
        c = adjcent_sides(p, pos)
        #print(c)
        not_conn += c

    print(not_conn)

    ### PART 2. -----------------------------------------------------------------------------------------
    ### reference for part 2: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/18.py
    """
    PART 2: The cooling rate depends on exterior surface area
    """
    
    count_2 = 0
    for x, y, z in pos:
        for r in [-1, 1]:
            if exterior_SA((x + r, y, z), pos): ### left and right of cube (x,y,z) in x axis --------------
                count_2 += 1

            if exterior_SA((x, y + r, z), pos): ### left and right of cube (x,y,z) in y axis --------------
                count_2 += 1

            if exterior_SA((x, y, z + r), pos): ### left and right of cube (x,y,z) in z axis --------------
                count_2 += 1


    print(count_2)

