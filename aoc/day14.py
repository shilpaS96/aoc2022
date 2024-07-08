"""
Sand is produced one unit at a time, 
and the next unit of sand is not produced until the previous unit of sand comes to rest.

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
"""


#def rocks(filename):

with open('day14.txt', 'rt') as myfile:
    lines = myfile.read()#.strip()
    #print(lines)


  ####  PART 1. ----------------------------------------------------------------------------------------

    rock_list = set()   ### positions at which rocks are placed ------------------ ------------------------

    #print(lines.split('\n')) ### ['498,4 -> 498,6 -> 496,6', '503,4 -> 502,4 -> 502,9 -> 494,9'] ------------
    for l in lines.split('\n'):   ### splitting lines w.r.t new line  ----------------------------------------
        #print(l)
        l = l.split('->')   ### splitting lines w.r.t '->'  ----------------------------------------------
        #print(l) ### ['498,4 ', ' 498,6 ', ' 496,6'] ---------------------------------------------------
        line_start = ()    ### start point of every new line  --------------------------------------------

        for index, i in enumerate(l):   ### enumerating over lines  --------------------------------------
            #print(i.split(','))
            x, y = i.split(',')
            x, y = int(x), int(y)
            #print(x, y)
            #print(line_start)
            rock_list.add((x,y))   
            if index > 0:
                h = x-line_start[0]
                v = y-line_start[1]
                if h == 0:    ### moving top to down or vice versa ----------------------------------------------------------------
                    for j in range(1, abs(v)):    ### adding all points from p1 to p2 while moving vertically -----------------
                        #nx = line_start[0] + j*(1 if v >0 else -1)
                        ny = line_start[1] + j*(1 if v >0 else -1)
                        rock_list.add((x,ny))

                elif v == 0:   ### moving left to right or vice versa ---------------------------------- ----------------------
                    for j in range(1, abs(h)):    ### ### adding all points from p1 to p2 while moving horizontally -----------
                        nx = line_start[0] + j*(1 if h >0 else -1)
#                        ny = line_start[1] + j*(1 if v >0 else -1)
                        rock_list.add((nx,y))

            line_start = (x,y) ### updating start position of every new line -----------------------------------------------------
        #print(rock_list)



    #rock_list = set(rock_list)   ### converting list into set to remove duplicates  -------------------------------------------
    #print(rock_list)
    #print(len(rock_list))

    #print(max(e[1] for e in rock_list))

    ### top and bottom end of the cave -------------------------------------------------------------------------------------
    max_rows = max(e[1] for e in rock_list)
    min_rows = min(e[1] for e in rock_list)
    #print(max_rows, min_rows)

    ### left and right end of the cave -------------------------------------------------------------------------------------
    max_col = max(e[0] for e in rock_list)
    min_col = min(e[0] for e in rock_list)
    #print(max_col, min_col)
    #print(max_col * max_rows)


    start_pos = (500, 0) ### position from where unit of sand is falling --------------------------------------------------
    sand_unit = []   ### for storing number of sand units -------------------------------------------------

    for k in range(max_col * max_rows):   ### sliding sand units for enough number of times -----------------------------
        rock_slide = start_pos ### starting from 500, 0 ----------------------------------------------------------------
        for r in range(max_rows): ### as sand unit can not go down taking more than max_rows steps ---------------------------
            if rock_slide[0] < min_col or rock_slide[0] > max_col:  ### break -------------------------------------------------
                #print(rock_slide[0], rock_slide[1])
                break
            if (rock_slide[0], rock_slide[1]+1) not in rock_list: ### one step down -----------------------------------------
                #print('move down', k)
                #print((rock_slide[0], rock_slide[1]+1))
                rock_slide = (rock_slide[0], rock_slide[1]+1)

            elif (rock_slide[0]-1, rock_slide[1]+1) not in rock_list: ### one step left to the bottom ------------------------
                #print('move down-left', k)
                #print(rock_slide[0]-1, rock_slide[1]+1)
                rock_slide = (rock_slide[0]-1, rock_slide[1]+1)

            elif (rock_slide[0]+1, rock_slide[1]+1) not in rock_list: ### one step right to the bottom ------------------------
                #print('move down-right', k)
                #print(rock_slide[0]+1, rock_slide[1]+1)
                rock_slide = (rock_slide[0]+1, rock_slide[1]+1)

            else:
                #print(k+1)
                break

        if rock_slide == start_pos or min_col > rock_slide[0] or rock_slide[0] > max_col:
            #print(k)  ### as soon as the sand stopped moving ---------------------------------------------------------------
            #print('no sliding')
            #print(rock_slide[0], rock_slide[1])
            break

        if min_col <= rock_slide[0] <= max_col: ### adding the unit into sand_unit list and rock_list (blocked postions) ---------

            rock_list.add(rock_slide)
            sand_unit.append(rock_slide)
            #print(rock_list)
        #print(sand_unit)


    print(len(set(sand_unit)))
    #print((sand_unit))

    #### PART 2. ---------------------------------------------------------------------------------------------------------

    """
    Assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point 
    in your scan.
    """
    
    depth = 2 + max_rows ### depth of the cave if increased by 2 length --------------------------------------------------
    #print(floor)
    #print(min_col, max_col)

    for x in range(-max_col * 1000, max_col * 1000):   ### adding base of cave to rock list ----------------------------------------
        rock_list.add((x,depth))

    """
    for instance:
        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->
    """
    
    #print(len(rock_list))

    start_pos = (500, 0)
    #sand_unit = []   ### for storing number of sand units -------------------------------------------------------------
                      ### adding to the previous sand list as new points will be added and old points remains --

    for k in range(max_col * 1000):   ### sliding sand units for enough number of times ---------------------------------
        rock_slide = start_pos
        for r in range(depth+1):
           
            if (rock_slide[0], rock_slide[1]+1) not in rock_list:
                #print('move down', k)
                #print((rock_slide[0], rock_slide[1]+1))
                rock_slide = (rock_slide[0], rock_slide[1]+1)

            elif (rock_slide[0]-1, rock_slide[1]+1) not in rock_list:
                #print('move down-left', k)
                #print(rock_slide[0]-1, rock_slide[1]+1)
                rock_slide = (rock_slide[0]-1, rock_slide[1]+1)

            elif (rock_slide[0]+1, rock_slide[1]+1) not in rock_list:
                #print('move down-right', k)
                #print(rock_slide[0]+1, rock_slide[1]+1)
                rock_slide = (rock_slide[0]+1, rock_slide[1]+1)

            else:
                #print(k+1)
                break

        if rock_slide == start_pos:
            #print(k)  ### as soon as it sand stopped moving -----------------
            #print('no sliding')
            rock_list.add(rock_slide)
            sand_unit.append(rock_slide)   ### to add the last point i.e. starting point (500, 0) --------
            break

        #if min_col <= rock_slide[0] <= max_col:

        rock_list.add(rock_slide)
        sand_unit.append(rock_slide)
            #print(rock_list)
        #print(sand_unit)


    print(len(set(sand_unit)))
    

