"""
--- Day 1: Calorie Counting ---
test data example: ----------

elf 1:
1000
2000
3000

elf 2:
4000

elf 3:
5000
6000

elf 4:
7000
8000
9000

elf 5:
10000
"""

#PART 1. ------------------------------------------------------------------------------------------------

### defining a function for calculating number of calories carried by each elf -----------------------------

def total_cal(filename):
    l = []  ### for storing each calorie carried by an elf -----------------------------------------------
    count = []  ### storing sum over all calories carried by each elf ------------------------------------
    with open(filename, 'rt') as myfile:
        for lines in myfile.readlines():
            print(lines)
            
            ### condition for appending all calories carried by an elf --------------------------------------
            if lines != '\n':  
                lines = (lines.strip())
                l.append(int(lines))
                #print(l)

            ### if next elf started, we will sum the calories carried by previous elf and initialize new list
            ### for next elf -------------------------------------------------------------------------------
            else:
                count.append(sum(l))
                l = []

        return max(count) ### returning the maximum calories carried by an elf ------------------------------


print('Part 1: ', total_cal('day01.txt'))


### PART 2. -----------------------------------------------------------------------------------------
### defining a function for calculating the sum of top 3 calories carried by 3 elves ---------------------

def Top_3_cal(filename):
    l = []
    count = []
    with open(filename, 'rt') as myfile:
        for lines in myfile.readlines():
            #print(lines)
            if lines != '\n':
                lines = (lines.strip())
                l.append(int(lines))
                #print(l)

            else:
                count.append(sum(l))
                l = []
        
        i = 0 ### for initializing while loop ----------------------------------------------
        top_3 = 0
        while i < 3:
            #print(i)
            top_3 += max(count) ### adding max value in the list of count to top_3 ------------------
            count.remove(max(count)) ### removing that value from the list --------------------------
            i += 1 ### again takin max in the updated list ------------------------------------------
                    ### running this for 3 times to get top 3 ---------------------------------------


        return top_3

print('Part 2: ', Top_3_cal('day01.txt'))
