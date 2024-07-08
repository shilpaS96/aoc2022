with open('day15.txt', 'rt') as myfile:
    lines = myfile.read()#.strip()
    #print(lines) ### read file as it is ------------------------------------------------------------------

    Sensors = set() ### set of sensors and respective beacon ---------------------------------------------
    Manhattan_distance = []


    for l in lines.split('\n'): ### adding pairs of sensor and its beacon in a set Sensors ----------------
        #print(l, type(l))
        l = l.strip().split()
        #print(l) ### ['Sensor', 'at', 'x=2,', 'y=18:', 'closest', 'beacon', 'is', 'at', 'x=-2,', 'y=15'] -----
        x_S = int([i[0:-1] for i in l[2].split('=') if i[0:-1].lstrip('-').isdigit() == True][0])
        #print(x_S)
        """
        splitting "x=2" excluding '='
        i[0:-1] for i in l[2].split('='): taking only integer.
        i[0:-1].lstrip('-').isdigit(): .isdigit() function is applicable for positive digits.
        .lstrip(): strip '-' from string 
        """
        y_S = int([i[0:-1] for i in l[3].split('=') if i[0:-1].lstrip('-').isdigit() == True][0])
        #print(x_S, y_S)
        #print(l[8])

        x_B = int([i[0:-1] for i in l[8].split('=') if i[0:-1].lstrip('-').isdigit() == True][0])
        #print(l[8].split('='))
        #print(x_B)

        y_B = int([i for i in l[9].split('=') if i.lstrip('-').isdigit() == True][0])

        Sensors.add((x_S, y_S, x_B, y_B))
        manhattan_dist = abs(x_S - x_B) + abs(y_S - y_B)
        
    #print(Signals)
    
    
    ###  PART 1. ----------------------------------------------------------------------------------------

    remove_bpos = set()

    for x_S, y_S, x_B, y_B in Sensors:
        print(x_S, y_S, x_B, y_B)

        manhattan_dist = abs(x_S - x_B) + abs(y_S - y_B)

        y = 2000000
        #y = 10

        for x in range(-10000000, 10000000): ### taking x range to ve large enough ------------------------
            #print(x)
            dist = abs(x_S - x) + abs(y_S - y)

            if x == x_B and y_B == y or dist > manhattan_dist:
                #remove_bpos.remove(x)
                continue


            remove_bpos.add(x)
                
            
            #if x == x_B and y_B == y:
            #    remove_bpos.remove(x)
                

            
    print('Part1: ', len((remove_bpos)))
    

    ### PART 2. -------------------------------------------------------------------------------------------
    """
                   1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....


    """

    exit_loop = False
    exit_main_loop = False
    for x_S, y_S, x_B, y_B in Sensors:
        manhattan_dist = abs(x_S - x_B) + abs(y_S - y_B)
            #print((x_S, y_S))
        print(manhattan_dist)
        #print('sensor is: ', x_S, y_S)
                       
        for i in range(0, manhattan_dist+2):
            Y = manhattan_dist + 1 - i
            long_distance = [(x_S + i, y_S + Y), (x_S + i, y_S - Y), (x_S - i, y_S + Y), (x_S - i, y_S - Y)]
            #print(long_distance)
            for x, y in long_distance:
            #    print(x,y)

                if (x > 4000000 or x < 0) or (y > 4000000 or y < 0):
            #        print('out of the grid')
                    continue

                common_pt = {(x,y)}
                for Sx, Sy, Bx, By in Sensors:
                    manhattan_dist = abs(Sx - Bx) + abs(Sy - By)
                    dist = abs(Sx - x) + abs(Sy - y)
                    #print(dist)

                    if manhattan_dist > dist:
                        common_pt = set()
                        break

                    #common_pt.add((x,y))
        
                    #print(common_pt)

                if len(common_pt) != 0:
                    print(common_pt)
                    exit_loop = True
                    print('Part 2: ', 4000000 * x + y)
                #    print(x,y)

            if exit_loop:
                exit_main_loop = True

                break

        if exit_main_loop:
            break


