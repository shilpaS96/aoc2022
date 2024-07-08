"""
You'd like to reach E, but to save energy, you should do it in as few steps as possible.
PART 1: Current position (S) and the location that should get the best signal (E)

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

"""

### function that returns elevation of each square box in a grid -------------------------------------------

def elevation(letter):
    if letter == 'S':
        return ord('a')

    elif letter == 'E':
        return ord('z')

    else:
        return ord(letter)

with open('day12.txt', 'rt') as myfile:
    lines = myfile.read().split()
    #print(lines) ### ['abcccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaccccccccccccc
                 ###  aaaaaaaccccccccccccccccaaaaaaccccccccccccccccccccccccccaaaaacccaaa
                 ###  ccccccccccccccccccccccccccccccaaaaa', ...] 

    ### forming an array (list of lists) ------------------------------------------------------------------

    for i in range(len(lines)):
        lines[i] = list(lines[i])


    ### PART 1. --------------------------------------------------------------------------------------

    seen = set() ### set that contains positions which are already visited -----------------------------------

    ### Finding the start (S) and end (E) position in my array ------------------------------------------------

    for c in range(len(lines[0])):
        for r in range(len(lines)):
            if lines[r][c] == 'S':
                #print(lines[r][c])
                #print(r, c)
                pos = []  ### list that stores the positions to be visited ---------------------------------
                seen.add((r,c))
                pos.append((r,c,0))

            if lines[r][c] == 'E':
                best_signal_r = r
                best_signal_c = c
                
    #print(best_signal_r, best_signal_c)
    #print(pos)
    not_reached = 1
    ### using BFS to get shortest path to E -----------------------------------------------------------------    
    while not_reached: 
        x, y, dist = pos.pop(0)

        ###  four neigbors of (x,y) -------------------------------------------------------------------------
        xy_neighbor = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        #print(x, y, dist)

        for i in xy_neighbor:
            #print(i[0], i[1])
            

            if (i[0], i[1]) in seen: ### if already visited then move to next -------------------------------
                continue

            if i[0] < 0 or i[0] >= len(lines) or i[1] < 0 or i[1] >= len(lines[0]):
                #print('if 1 stop here')
                 continue

            #print(elev_curr, elev_next)
            if elevation(lines[i[0]][i[1]]) - elevation(lines[x][y]) > 1:
                #print('if 3 stop here')
                continue
            
            ### print it in the last because we want our elevation to be high by one or less unit -------------
            if ((i[0], i[1]) == (best_signal_r, best_signal_c)): 
                #print('if 4 stop here')

                print('we got to E:', dist + 1)
                ### to stop while loop --------------------------------------------------------
                not_reached = 0 
                break                          
             
            seen.add((i[0], i[1]))
            pos.append((i[0], i[1], dist+1))

            #print(seen)
            #print(pos)

    #print(seen)
    #print((best_signal_r, best_signal_c+1) in seen)
       
    #print(lines)
    


    
    ###  PART 2. ----------------------------------------------------------------------------------------------

    """
    Find the shortest path from any square at elevation a to the square marked E.
    """
    
    ### list of all start positions ---------------------------------------------------------
    start_pos = []

    for c in range(len(lines[0])):
        for r in range(len(lines)):
            if lines[r][c] == 'a' or lines[r][c] == 'S':
                #print(lines[r][c])
                #print(r, c)
                pos = []

                start_pos.append((r,c))

            if lines[r][c] == 'E':
                best_signal_r = r
                best_signal_c = c

    #print(start_pos)


    ### will store all the lengths of path travelled by each of the start position --------------------------
    distances = [] 
    for p in start_pos:  ### repeating the steps above for each start position -----------------------------
        #print(p[0], p[1])
        seen = set()
        pos = []
        pos.append((p[0],p[1],0))
        seen.add((p[0],p[1]))
        not_reached = 1
        while len(pos) != 0 and not_reached: 
            ### it might be the case that there is no way to move forward from a given position---------------
            ### so in that case pos list will become empty and never reach to E.------------------------------
            ### That is why len(pos) has to be in consideration ----------------------------------------------
            x, y, dist = pos.pop(0)

            ###  four neigbors of (x,y) ----------------------------------------------------------------
            xy_neighbor = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            #print(x, y, dist)

            for i in xy_neighbor:
                #print(i[0], i[1])

                if (i[0], i[1]) in seen:
                    continue

                if i[0] < 0 or i[0] >= len(lines) or i[1] < 0 or i[1] >= len(lines[0]):
                    #print('if 1 stop here')
                    continue

                #print(elev_curr, elev_next)
                if elevation(lines[i[0]][i[1]]) - elevation(lines[x][y]) > 1:
                    #print('if 3 stop here')
                    continue
            
                ### print it in the last because we want our elevation to be high by one or less unit----------
                if ((i[0], i[1]) == (best_signal_r, best_signal_c)): 
                    #print('if 4 stop here')

                    #print('we got to E:', dist + 1)
                    distances.append(dist+1)
                    ### to stop while loop ------------------------------------------------------------------
                    not_reached = 0
                    #pos = [] 
                    break                          
             
                seen.add((i[0], i[1]))
                pos.append((i[0], i[1], dist+1))

    #print(distances)
    print(min(distances))
    
