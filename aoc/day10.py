"""
Start by figuring out the signal being sent by the CPU. 
The CPU has a single register, X, which starts with the value 1. 
It supports only two instructions:

- addx V takes two cycles to complete. 
  After two cycles, the X register is increased by the value V. (V can be negative.)
- noop takes one cycle to complete. It has no other effect.

For now, consider the signal strength (the cycle number multiplied by the value of the X register) 
during the 20th cycle and every 40 cycles after that 
(that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

PART 1: Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
        What is the sum of these six signal strengths?

"""



with open('day10.txt', 'rt') as myfile:
    line = myfile.readlines()
    #print(line)  ### ['addx 2\n', 'addx 3\n', 'addx 3\n', ...]

    ### PART 1. ------------------------------------------------------------------------------------------------------------

    X = 1
    
    cycle_num = 0
    
    signal_strength = [] ### stroing signal strength after 20th and every 40th cycle -----------------------------------
    #cycle_num_l = []
    cycles = [20, 60, 100, 140, 180, 220] ### number of cycles ---------------------------------------------------------

    for l in line:
        #print(l)
        l = l.strip().split()
        #print(l)  ###  ['addx', '2']
        #print(index)
        if l[0] == "noop":  ### if its noop, number of cycle will increase by one and nothing happens -------------------
            #print("its noop")
            cycle_num += 1
            #if cycle_num < cycles[0]:

            if cycle_num not in set(cycles):
                continue

            signal_strength.append(cycle_num * X) ### if cycle_num reaches the nth cycle from cycles list -----------------
                                                  ### signal strength is calculated --------------------------------------

           


            #print(signal_strength)
            #print(X)
            #print("cycle_num is ", cycle_num)

        else: ### if its addx v, it will take two cycles to complete ------------------------------------------
            i = 1 ### to start cycle -------------------------------------------------------------------------
            while i < 3: ### to run two cycles of addx v ------------------------------------------------------
                cycle_num += 1 ### cycle is started ----------------------------------------------------------
                               
                if cycle_num not in set(cycles):
                   
                    i += 1
                    continue
                
                signal_strength.append(cycle_num * X)
                i += 1
               
            X += int(l[1]) ### updating X after two completion of two cycles of addx v -------------------------------
            

    #print(signal_strength)
    print(sum(signal_strength))
    #print(X)
    #print(cycle_num_l)


    ### PART 2. ---------------------------------------------------------------------------------------------------------------------

    """
    #If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, 
    #the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.)

    #Cycle   1 -> ######################################## <- Cycle  40
    #Cycle  41 -> ######################################## <- Cycle  80
    #Cycle  81 -> ######################################## <- Cycle 120
    #Cycle 121 -> ######################################## <- Cycle 160
    #Cycle 161 -> ######################################## <- Cycle 200
    #Cycle 201 -> ######################################## <- Cycle 240
    
    Render the image given by your program. What eight capital letters appear on your CRT?

    """
    X = 1
    cycle_num = 0
    sprite_pos = ["#"]*3
    dots = "."*37
    dots = list(dots)
    #print(dots)
    cycles_2 = [40, 80, 120, 160, 200, 240] ### move to new row after completion of every 40th cycle --------------------------------

    for d in dots:  ### appending dots to list sprite_pos and get Sprite position: ###..................................... -----------

        sprite_pos.append(d)
    #print((sprite_pos)) ### ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 
          ###                '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

    sprite_pos_l = []
    for k in range(len(cycles_2)): ### list Sprite_pos for every new row ------------------------------------------------------------
        sprite_pos_l.append(sprite_pos)

    #print(sprite_pos_l[1])
    #print((sprite_pos_l))

    """
    # [['#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 
    # '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['#', '#', '#', '.', ...], ...]

    """


    pattern = "" ### pattern of '#' and '.' of string type ----------------------------------------------------------------
    pattern_l = [] ### list of strings of length 40 ------------------------------------------------------------------------

    for l in line:
        l = l.strip().split()
        #print(l)

        if l[0] == 'addx': 
            i = 1  ### addx v take two cycles. initializing with i = 1 -----------------------------------------------------------
            while i < 3:
                cycle_num += 1
                if cycle_num <= cycles_2[0]: ### taking first 40 cycles -----------------------------------------------------------
                    #print("for 40", l)
                    s = 0
                    pattern = pattern + sprite_pos_l[s][cycle_num-1] ### since indexing starts from zero in python ----------------
                    ### adding the string which is at position sprite_pos_l[0][cycle_num-1] to pattern -----------------------------
                    #s = 0

                elif cycle_num <= cycles_2[1]:  ### taking second 40 cycles -------------------------------------------------------
                    #print("for 80", cycle_num)
                    s = 1
                    pattern = pattern + sprite_pos_l[s][cycle_num-41] ### since indexing starts from zero in python ----------------
                    

                elif cycle_num <= cycles_2[2]:  ### taking third 40 cycles -------------------------------------------------------
                    s = 2
                    pattern = pattern + sprite_pos_l[s][cycle_num-81] ### since indexing starts from zero in python ----------------
                    

                elif cycle_num <= cycles_2[3]:  ### taking fourth 40 cycles -------------------------------------------------------
                    s = 3
                    pattern = pattern + sprite_pos_l[s][cycle_num-121] ### since indexing starts from zero in python ----------------
                    

                elif cycle_num <= cycles_2[4]:  ### taking fifth 40 cycles -------------------------------------------------------
                    s = 4
                    pattern = pattern + sprite_pos_l[s][cycle_num-161] ### since indexing starts from zero in python ----------------
                    

                elif cycle_num <= cycles_2[5]:  ### taking sixth 40 cycles -------------------------------------------------------
                    s = 5
                    pattern = pattern + sprite_pos_l[s][cycle_num-201] ### since indexing starts from zero in python ----------------
                    
                i += 1  ### going to second cycle -------------------------------------------------------------------------------
                #print(cycle_num)
                #print(pattern)
            X += int(l[1])  ### updating X after completing two cycles -------------------------------------------------------------
            #print(X)
            for index, j in enumerate(sprite_pos_l[s]): ### after updating X, updating the sprite position according to X value ----
                ### iterating over sprite whose if elif condition has just executed ------------------------------------------------
                #print(" new sprit", s)
                #print(X)
                if index in {X-1, X, X+1}: ###  moving '###' to index X-1, X, X+1 ------------------------------------------------
                    sprite_pos_l[s][index] = "#"
                else:
                    sprite_pos_l[s][index] = "."
            #print("new sprit is: ", sprite_pos_l[s])

        else:
            #print("its noop") ### noop has no effect on X and hence on sprite position ----------------------------------------
            cycle_num += 1
            if cycle_num <= cycles_2[0]:
                    pattern = pattern + sprite_pos_l[0][cycle_num-1]

            elif cycle_num <= cycles_2[1]:
                    pattern = pattern + sprite_pos_l[1][cycle_num-41]

            elif cycle_num <= cycles_2[2]:
                    pattern = pattern + sprite_pos_l[2][cycle_num-81]

            elif cycle_num <= cycles_2[3]:
                    pattern = pattern + sprite_pos_l[3][cycle_num-121]

            elif cycle_num <= cycles_2[4]:
                    pattern = pattern + sprite_pos_l[4][cycle_num-161]

            elif cycle_num <= cycles_2[5]:
                    pattern = pattern + sprite_pos_l[5][cycle_num-201]

            #print(cycle_num)
            #print(pattern)

    for p in range(0, 240, 40): ### taking string of length 40 ------------------------------------------------------------
        #print(p)
        pattern_l.append(pattern[p:p+40])
    #print((pattern_l))
    final_pat = '\n'.join(pattern_l) ### appending all elements of pattern_l by '\n' ----------------------------------------
    print(final_pat)
    #print(type(final_pat))

    #print(pattern_l)
    #print(len(pattern_l[1]))