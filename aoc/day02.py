"""
--- Rock, Paper, Scissor score ---
test set example:

XYZ is me.
A/X: Rock(1); B/Y: Paper(2); C/Z: Scissor(3)
0: loss, 3: draw, 6: winner
Rock defeats Scissor, Scissor defeats Paper, Paper defeats Rock

A Y
B X
C Z

"""

### PART 1. ----------------------------------------------------------------------------------------
### defining a function for calculating the score ---------------------------------------------------
def RPS(l):
    count = 0

    #print(l) 
    for i in l:
        #print(i)
        #print(len(i))

        i = i.split() ### splitting the string i in list l to get ['A', 'X'] -------------------------------
        #print(i)
        if i[0] == 'A' and i[1] == 'X':
            count += 4
        elif i[0] == 'A' and i[1] == 'Y': 
            ### I won so total score is: Y(2) + win(6) = 8 -------------------------------------------------
            count += 8
        elif i[0] == 'A' and i[1] == 'Z':
            count += 3
        elif i[0] == 'B' and i[1] == 'X':
            count += 1
        elif i[0] == 'B' and i[1] == 'Y':
            count += 5
        elif i[0] == 'B' and i[1] == 'Z':
            count += 9
        elif i[0] == 'C' and i[1] == 'X':
            count += 7
        elif i[0] == 'C' and i[1] == 'Y':
            count += 2
        elif i[0] == 'C' and i[1] == 'Z':
            count += 6

    return count

### PART 2. Rock, Paper, Scissor strategy score -------------------------------------------------
### X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win -----

### oponent chose A (rock) and I chose Y it means I want to end the game with draw so I should 
### choose rock ------------------------------------------------------------------------------------------

### defining a function for playing strategically --------------------------------------------------------- 
def RPS_strat(l):
   
    count = 0
    #print(l)

    for i in l:
           #print(i)
            #print(len(i))
        i = i.split()
            #print(lt)
        if i[0] == 'A' and i[1] == 'X': ### If oponent chose A(rock) and I chose X that mean I should lose
            count += 3                  ### so I will choose scissor. hence the score is: scissor(3) + lose(0)
        elif i[0] == 'A' and i[1] == 'Y':
            count += 4
        elif i[0] == 'A' and i[1] == 'Z':
            count += 8
        elif i[0] == 'B' and i[1] == 'X':
            count += 1
        elif i[0] == 'B' and i[1] == 'Y':
            count += 5
        elif i[0] == 'B' and i[1] == 'Z':
            count += 9
        elif i[0] == 'C' and i[1] == 'X':
            count += 2
        elif i[0] == 'C' and i[1] == 'Y':
            count += 6
        elif i[0] == 'C' and i[1] == 'Z':
            count += 7

    return count

#print(RPS_strat('day02.txt'))



with open('day02.txt', 'rt') as myfile:
        l = myfile.readlines()
        #print(l)                ### ['A X\n', 'A Z\n',...] ----------------------------------------------
        print(RPS(l))
        print(RPS_strat(l))
        