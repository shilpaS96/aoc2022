
### Part 1

with open('day09.txt', 'rt') as myfile:
    line = myfile.read()
    #print(line)
    line = line.splitlines()
    #print(line)

    H_position = (0,0)
 
    T_position = (0,0)

    T_pos = [(0,0)]

    for l in line:
        l, steps = l.split()
        #print(l)
        #print(steps)
        if l == 'D':
            for p in range(int(steps)):
                H_position = (H_position[0] + 1, H_position[1])
                x_dist = abs(H_position[0] - T_position[0])
                y_dist = abs(H_position[1] - T_position[1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position = (T_position[0]+1 if H_position[0] - T_position[0]>0 else T_position[0]-1, T_position[1]-1 if H_position[1] - T_position[1]<0 else (T_position[1]+1)) 
                    
                elif x_dist > 1 and y_dist == 1:
                    T_position = (T_position[0]+1, T_position[1]+1 if H_position[1]-T_position[1] > 0 else T_position[1] -1)

                elif x_dist > 1  and y_dist == 0:
                    T_position = (T_position[0]+1, T_position[1])
#                elif y_dist > 1:
#                    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)

                T_pos.append(T_position)
            #print(H_position)
            #print(T_pos)

        elif l == 'R':
            for p in range(int(steps)):
                H_position = (H_position[0], H_position[1]+1)
                x_dist = abs(H_position[0] - T_position[0])
                y_dist = abs(H_position[1] - T_position[1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position = (T_position[0]+1 if H_position[0] - T_position[0]>0 else T_position[0]-1, T_position[1]-1 if H_position[1] - T_position[1]<0 else (T_position[1]+1)) 
                    
                elif x_dist == 1 and y_dist > 1:
                    T_position = (T_position[0]+1 if H_position[0] - T_position[0]>0 else T_position[0]-1, T_position[1]+1)

                elif x_dist == 0 and y_dist > 1:
                    T_position = (T_position[0], T_position[1]+1)
#                elif y_dist > 1:
#                    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)

                T_pos.append(T_position)
            #print(H_position) 
            #print(T_pos)


        elif l == 'U':
            for p in range(int(steps)):
                H_position = (H_position[0]-1, H_position[1])
                x_dist = abs(H_position[0] - T_position[0])
                y_dist = abs(H_position[1] - T_position[1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position = (T_position[0]+1 if H_position[0] - T_position[0]>0 else T_position[0]-1, T_position[1]-1 if H_position[1] - T_position[1]<0 else (T_position[1]+1)) 
                    
                elif x_dist > 1 and y_dist == 1:
                    T_position = (T_position[0]-1, T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[1]-1)

                elif x_dist > 1 and y_dist == 0:
                    T_position = (T_position[0]-1, T_position[1])
                #elif y_dist > 1:
                #    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)

                T_pos.append(T_position) 
            
        elif l == 'L':
            for p in range(int(steps)):
                H_position = (H_position[0], H_position[1]-1)
                x_dist = abs(H_position[0] - T_position[0])
                y_dist = abs(H_position[1] - T_position[1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position = (T_position[0]+1 if H_position[0] - T_position[0]>0 else T_position[0]-1, T_position[1]-1 if H_position[1] - T_position[1]<0 else (T_position[1]+1)) 
                    
                elif x_dist == 1 and y_dist > 1:
                    T_position = (T_position[0]+1 if H_position[0] - T_position[0]>0 else T_position[0]-1, T_position[1]-1)

                elif x_dist == 0 and y_dist > 1:
                    T_position = (T_position[0], T_position[1]-1)
                #elif y_dist > 1:
                #    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)

                T_pos.append(T_position) 
            
#    print(set(T_pos))
    print(len(set(T_pos)))
    print(len(T_pos))





### Part 2


    H_position = (0,0)
    
    T_position = [(0,0)] * 9
    #print(T_position)
    pos_list = []

    T_pos = [(0,0)]
   

    for l in line:
        l, steps = l.split()
        #print(l)
        #print(steps)
        if l == 'D':
            for p in range(int(steps)):
                H_position = (H_position[0] + 1, H_position[1])
                x_dist = abs(H_position[0] - T_position[0][0])
                y_dist = abs(H_position[1] - T_position[0][1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position[0] = (T_position[0][0]+1 if H_position[0] - T_position[0][0]>0 else T_position[0][0]-1, T_position[0][1]-1 if H_position[1] - T_position[0][1]<0 else (T_position[0][1]+1)) 
                    
                elif x_dist > 1 and y_dist == 1:
                    T_position[0] = (T_position[0][0]+1, T_position[0][1]+1 if H_position[1]-T_position[0][1] > 0 else T_position[0][1] -1)

                elif x_dist > 1  and y_dist == 0:
                    T_position[0] = (T_position[0][0]+1, T_position[0][1])

                for j in range(1,9):
                    x_dist = abs(T_position[j-1][0] - T_position[j][0])
                    y_dist = abs(T_position[j-1][1] - T_position[j][1])

                    if x_dist >=2 and y_dist >= 2:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist < 2 and y_dist<2:
                        continue

                    elif (x_dist >= 2 and y_dist == 1) or (y_dist >= 2 and x_dist == 1):
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist >= 2 and y_dist == 0:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1])

                    elif y_dist >=2 and x_dist == 0:
                        T_position[j] = (T_position[j][0], T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                pos_list.append(T_position[8])
#                elif y_dist > 1:
#                    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)

        elif l == 'R':
            for p in range(int(steps)):
                H_position = (H_position[0], H_position[1]+1)
                x_dist = abs(H_position[0] - T_position[0][0])
                y_dist = abs(H_position[1] - T_position[0][1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position[0] = (T_position[0][0]+1 if H_position[0] - T_position[0][0]>0 else T_position[0][0]-1, T_position[0][1]-1 if H_position[1] - T_position[0][1]<0 else (T_position[0][1]+1)) 
                    
                elif x_dist == 1 and y_dist > 1:
                    T_position[0] = (T_position[0][0]+1 if H_position[0] - T_position[0][0]>0 else T_position[0][0]-1, T_position[0][1]+1)

                elif x_dist == 0 and y_dist > 1:
                    T_position[0] = (T_position[0][0], T_position[0][1]+1)

                for j in range(1,9):
                    x_dist = abs(T_position[j-1][0] - T_position[j][0])
                    y_dist = abs(T_position[j-1][1] - T_position[j][1])

                    if x_dist >=2 and y_dist >= 2:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist < 2 and y_dist<2:
                        continue

                    elif (x_dist >= 2 and y_dist == 1) or (y_dist >= 2 and x_dist == 1):
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist >= 2 and y_dist == 0:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1])

                    elif y_dist >=2 and x_dist == 0:
                        T_position[j] = (T_position[j][0], T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                pos_list.append(T_position[8])
#                elif y_dist > 1:
#                    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)


        elif l == 'U':
            for p in range(int(steps)):
                H_position = (H_position[0]-1, H_position[1])
                x_dist = abs(H_position[0] - T_position[0][0])
                y_dist = abs(H_position[1] - T_position[0][1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position[0] = (T_position[0][0]+1 if H_position[0] - T_position[0][0]>0 else T_position[0][0]-1, T_position[0][1]-1 if H_position[1] - T_position[0][1]<0 else (T_position[0][1]+1)) 
                    
                elif x_dist > 1 and y_dist == 1:
                    T_position[0] = (T_position[0][0]-1, T_position[0][1]+1 if H_position[1] - T_position[0][1]>0 else T_position[0][1]-1)

                elif x_dist > 1 and y_dist == 0:
                    T_position[0] = (T_position[0][0]-1, T_position[0][1])

                for j in range(1,9):
                    x_dist = abs(T_position[j-1][0] - T_position[j][0])
                    y_dist = abs(T_position[j-1][1] - T_position[j][1])

                    if x_dist >=2 and y_dist >= 2:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist < 2 and y_dist<2:
                        continue

                    elif (x_dist >= 2 and y_dist == 1) or (y_dist >= 2 and x_dist == 1):
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist >= 2 and y_dist == 0:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1])

                    elif y_dist >=2 and x_dist == 0:
                        T_position[j] = (T_position[j][0], T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                pos_list.append(T_position[8])
                #elif y_dist > 1:
                #    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)

            #break
        elif l == 'L':
            for p in range(int(steps)):
                H_position = (H_position[0], H_position[1]-1)
                x_dist = abs(H_position[0] - T_position[0][0])
                y_dist = abs(H_position[1] - T_position[0][1])

                if x_dist <= 1 and y_dist <=1:
                    #print("yes")
                    pass 
                elif x_dist > 1 and y_dist >1:
                    #print("yep")
                    T_position[0] = (T_position[0][0]+1 if H_position[0] - T_position[0][0]>0 else T_position[0][0]-1, T_position[0][1]-1 if H_position[1] - T_position[0][1]<0 else (T_position[0][1]+1)) 
                    
                elif x_dist == 1 and y_dist > 1:
                    T_position[0] = (T_position[0][0]+1 if H_position[0] - T_position[0][0]>0 else T_position[0][0]-1, T_position[0][1]-1)

                elif x_dist == 0 and y_dist > 1:
                    T_position[0] = (T_position[0][0], T_position[0][1]-1)
                #elif y_dist > 1:
                #    T_position = (T_position[0], T_position[1]+1 if H_position[1] - T_position[1]>0 else T_position[0]-1)

                T_pos.append(T_position) 
           

                for j in range(1,9):
                    x_dist = abs(T_position[j-1][0] - T_position[j][0])
                    y_dist = abs(T_position[j-1][1] - T_position[j][1])

                    if x_dist >=2 and y_dist >= 2:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist < 2 and y_dist<2:
                        continue

                    elif (x_dist >= 2 and y_dist == 1) or (y_dist >= 2 and x_dist == 1):
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                    elif x_dist >= 2 and y_dist == 0:
                        T_position[j] = (T_position[j][0]-1 if T_position[j-1][0] - T_position[j][0]<0 else T_position[j][0]+1, T_position[j][1])

                    elif y_dist >=2 and x_dist == 0:
                        T_position[j] = (T_position[j][0], T_position[j][1]+1 if T_position[j-1][1] - T_position[j][1]>0 else T_position[j][1]-1)

                pos_list.append(T_position[8])


    print(len(pos_list))
    print(len(set(pos_list)))





