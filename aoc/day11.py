
"""
Type of data:
Monkey 0:
  Starting items: 91, 54, 70, 61, 64, 64, 60, 85
  Operation: new = old * 13
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 1:
  Starting items: 82
  Operation: new = old + 7
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 3

.
.
.

Each monkey has several attributes:

- Starting items lists:
 your worry level for each item the monkey is currently holding in the order they will be inspected.
-   Operation shows:
 how your worry level changes as that monkey inspects an item. 
 (An operation like new = old * 5 means ->
  that your worry level after the monkey inspected the item is five times 
  whatever your worry level was before inspection.)
-   Test shows how the monkey uses your worry level to decide where to throw an item next.
    -  If true shows what happens with an item if the Test was true.
    -   If false shows what happens with an item if the Test was false.

- PART 1:
After each monkey inspects an item but before it tests your worry level, 
your relief that the monkey's inspection didn't damage the item 
causes your worry level to be divided by three and rounded down to the nearest integer.

Focus on the two most active monkeys if you want any hope of getting your stuff back. 
Count the total number of times each monkey inspects items over 20 rounds:

-> Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
-> Monkey 3 inspected items 105 times.
Multiply them: output

"""

import math


with open('day11.txt', 'rt') as myfile:
    line = myfile.read()
    line = line.splitlines()
    #print(line)

    """
    line = ['Monkey 0:', '  Starting items: 91, 54, 70, 61, 64, 64, 60, 85', '  Operation: new = old * 13', 
           '  Test: divisible by 2', '    If true: throw to monkey 5', '    If false: throw to monkey 2', '',
           'Monkey 1:', ...]
    """

    ### For test data: -----------------------------------------------------------------------------------------------------
    #  Monkey_inspection = {'Monkey0' : 0, 'Monkey1' : 0, 'Monkey2' : 0, 'Monkey3' : 0}
    ### number of inspections done by each monkey --------------------------------------------------------------------------
    #  Monkey_items = {'Monkey0': ['79,', '98'], 'Monkey1': ['54,', '65,', '75,', '74'], 
    #                   'Monkey2': ['79,', '60,', '97'], 'Monkey3': ['74']}
    ### list of items each monkey has --------------------------------------------------------------------------------------
    #### -------------------------------------------------------------------------------------------------------------------

    ### PART 1. -------------------------------------------------------------------------------------------------

    Monkey_items = {}
    Monkey_inspection = {}

    for l in line: ### appending dictionaries Monkey_items and Monkey_inspection -------------------------------------------
        l = l.strip(':').split()

        ### strip the line by ':' then split returns a list of words in l --------------------------------------------------
        #print(l) ### for instance: l = ['Starting', 'items:', '91,', '54,', '70,', '61,', '64,', 
                  ###                   '64,', '60,', '85'] ----------------------------------------------------------------

        if l == []:
            continue

        if l[0] == 'Monkey': ### appending Monkey_inspection -----------------------------------------------------------------
            Mon_num = l[0]+l[1] ### this defines monkey number like monkey 1, monkey 2, ... ----------------------------------
            Monkey_inspection[Mon_num] = 0 ### storing monkey_num as a key and number of inspections as its value -------------
            continue
        elif l[0] == 'Starting': ### appending Monkey_items -------------------------------------------------------------------
            value = l[2:] ### l = ['Starting', 'items:', '91,', '54,', '70,', '61,', '64,', 
                          ###     '64,', '60,', '85'] -------------------------------------------------------------------
            Monkey_items[Mon_num] = l[2:] ### ### storing monkey_num as a key and list of items as its value ------------
    #print(Monkey_items)
    #print(Monkey_inspection)
    #print(Monkey_items.items())

    
    for j in range(20): ### taking 20 rounds --------------------------------------------------------------------------------
        for l in line:
            #print(l)
            l = l.strip(':').split()
            #print(l)

            if l == []:
                continue


            if l[0] == 'Monkey': ### l = ['Monkey', '0']
                    
                Mon_num = l[0] + l[1] ### Monkey number for instance Monkey0 ---------------------------------------------------

                #print("its monkey")
                continue ### go to next line -----------------------------------------------------------------------------------
            elif l[0] == 'Starting': ### ['Starting', 'items:', '91,', '54,', '70,', '61,', '64,', '64,', '60,', '85'] ---------
                #items = l[2:]
                #print("its starting")
                continue ### go to next line ------------------------------------------------------------------------------------
            elif l[0] == 'Operation:': ### ['Operation:', 'new', '=', 'old', '*', '13'] -----------------------------------------
                #print("its operation time")
                op = l[-2] ### op = '*' -------------------------------------------------------------------------------------
                w = l[-1] ### w = '13' ---------------------------------------------------------------------------------------
                #print(w)
                continue ### go to next line --------------------------------------------------------------------------------

            elif l[0] == 'Test:': ### ['Test:', 'divisible', 'by', '2'] -------------------------------------------------------
                    
                if op == '*': ### multiplication -----------------------------------------------------------------------------
                    #print("we are testing now for *")
                    new = [] ### list of numbers after applying the operation op --------------------------------------------
                    tf = [] ### list of true/false: whether a number is divisible by l[-1] = 2 -------------------------------
                    for index, i in enumerate(Monkey_items[Mon_num]): 
                        #print(i)
                        """
                        enumerating over list of items of Monkey
                        for instance: Monkey0: '91,', '54,', '70,', '61,', '64,', '64,', '60,', '85' ----------------------------- 
                        """
                        if type(i) != int:
                            num = [int(x) for x in i.split(',') if x.isdigit()]
                        else: num = [i] ### for the next round as I am storing next item as an integer ----------------------------
                        #print(num, type(i)) 
                        Monkey_inspection[Mon_num] += 1 ### Monkey0 has inspected one item so add 1 ------------------------------
                        #print("running")
                        if w.isdigit() == True: ### w = '13' ---------------------------------------------------------------------
                        #    print((num[0]))
                            new_num = int(num[0]) * int(w)
                                
                        else: ### w = 'old'
                            new_num = int(num[0])**2 
                        
                        ### After each monkey inspects an item but before it tests your worry level ----------------------------
                        
                        new.append(new_num // 3) ### appending it to list of numbers of Monkey0 --------------------------------
                        if (new_num // 3)%int(l[-1]) == 0: ### if divisible then append true -----------------------------------
                #            print(l[-1])
                                
                            tf.append('true')
                        else: tf.append('false') ### else append false -----------------------------------------------------------
                        #print(tf)
                        #print(new)

                ### same steps for op == '+' ----------------------------------------------------------------------------------
                elif op == '+':
                    #print("we are testing now for +")
                    new = []
                    tf = []

                    for index, i in enumerate(Monkey_items[Mon_num]):
                        if type(i) != int:
                            num = [int(x) for x in i.split(',') if x.isdigit()]

                        else: num = [i]
                        #print(num) 
                        Monkey_inspection[Mon_num] += 1
                        #print("running")
                        if w.isdigit() == True:
                #            print((num[0]))
                            new_num = int(num[0]) + int(w)

                    #            print(new_num)

                        else: 
                            new_num = int(num[0])*2
                               
                               
                        
                        new.append(new_num//3)
                        if (new_num//3)%int(l[-1]) == 0:
                #            print(l[-1])
                                
                            tf.append('true')
                        else: tf.append('false')

                                
                continue

            else: ### 
                for v in range(len(tf)): ### iterating over length of tf list ---------------------------------------------------
                    #print(key)
                    #print(val)
                    #print(l[1].split(':')[0])

                    ### ['If', 'true:', 'throw', 'to', 'monkey', '6'] ------------------------------------------------------------
                    ### ['If', 'false:', 'throw', 'to', 'monkey', '0'] -----------------------------------------------------------
                    if tf[v] == l[1].split(':')[0]: ### comparing true vs true and false vs false from a list tf -----------------
                    #    print("throw it")
                #        print(l[-2]+l[-1])
                        mon = l[-2]+l[-1] ### adding last two string ------------------------------------------------------------
                        mon = mon.capitalize() ### monkey6 -> Monkey6
                #        print(mon)
                            


                        #print(Monkey_items[mon])
                        Monkey_items[mon].append(new[v]) ### appending item from new list at index v, to item list of Monkey6 -----
                        #print(Monkey_items)
                        #Monkey_items[Mon_num] = Monkey_items[Mon_num].pop(0)
                        (Monkey_items[Mon_num].pop(0)) ### pop an element from current monkey i.e. Monkey0 -----------------------
 

    print(Monkey_items)
    #print(Monkey_inspection)
    list = [] ### list of numbers that defines how many times each monkey has done inspection of items ---------------------------
    for key, value in Monkey_inspection.items():
        list.append(value) 

    list.sort()
    #print(list)
    print(list[-1] * list[-2])   ### final output -----------------------------------------------------------------------------
    



    ### PART 2. ------------------------------------------------------------------------------------------------------------
    ### item no longer causes your worry level to be divided by three ------------------------------------------------------
    ###perform 10000 rounds of the same ------------------------------------------------------------------------------------
    
    ### using modulo -------------------------------------------------------------------------------------------------------
    ### modulo all worry levels by a certain value -----------------------------------------------------------------------
    
    Monkey_items = {}
    Monkey_inspection = {}

    ### forming a dictionary -----------------------------------------------------------------------------------------------
    for l in line:
        l = l.strip(':').split()
        #print(l)
        if l == []:
            continue

        if l[0] == 'Monkey': ### appending Monkey_inspection -----------------------------------------------------------------
            Mon_num = l[0]+l[1] ### this defines monkey number like monkey 1, monkey 2, ... ----------------------------------
            Monkey_inspection[Mon_num] = 0 ### storing monkey_num as a key and number of inspections as its value -------------
            continue
        elif l[0] == 'Starting': ### appending Monkey_items -------------------------------------------------------------------
            value = l[2:] ### l = ['Starting', 'items:', '91,', '54,', '70,', '61,', '64,', 
                          ###     '64,', '60,', '85'] -------------------------------------------------------------------
            Monkey_items[Mon_num] = l[2:] ### ### storing monkey_num as a key and list of items as its value ------------

    #print(Monkey_items)
    #print(Monkey_inspection)
    #print(Monkey_items.items())
    

    ### taking modulo of test case ---------------------------------------------------------------------------------------
    mod = 1

    for l in line:
        #print(l)
        l = l.strip(':').split()
            #print(l)

        if l == []:
            continue
            #print(l)

        if l[0] == 'Test:':  ### ['Test:', 'divisible', 'by', '2'] -------------------------------------------------------------
            mod *= int(l[-1])
            #print(mod) ### multiply all test factors 2*13*5*3*11*17*7*19 = 9699690 --------------------------------------------

                #mod *= num[0]

    #print(mod)

            
    ### running the model for 10,000 times ----------------------------------------------------------------

    for j in range(10000):
        #print("yes, running", j)
        for l in line:
            #print(l)
            l = l.strip(':').split()
            #print(l)

            if l != []:

                if l[0] == 'Monkey':
                    Mon_num = l[0] + l[1]

                    #print("its monkey")
                    continue
                elif l[0] == 'Starting':
                    #items = l[2:]
                    #print("its starting")
                    continue
                elif l[0] == 'Operation:':
                    #print("its operation time")
                    op = l[-2]
                    w = l[-1]
                    #print(w)
                    continue

                elif l[0] == 'Test:':
                    
                    if op == '*':
                    #    print("we are testing now for *")
                        new = []
                        tf = []
                        for index, i in enumerate(Monkey_items[Mon_num]):
                            if type(i) != int:
                                num = [int(x) for x in i.split(',') if x.isdigit()]
                            else: num = [i]
                            #print(num) 
                            Monkey_inspection[Mon_num] += 1
                    #        print("running")
                            if w.isdigit() == True:
                            #    print((num[0]))
                                new_num = int(num[0]) * int(w)
                                
                            else: 
                                new_num = int(num[0])**2

                            new_num %= mod
                            """
                            if new_num == 0 then new_num is divisible by l[-1]
                            else we need to check the divisibility of new_num by l[-1]
                            """
                                
                            new.append(new_num)
                            #print(l[-1])
                            if new_num%int(l[-1]) == 0:
                    #            print(l[-1])
                                
                                tf.append('true')
                            else: tf.append('false')

                    elif op == '+':
                    #    print("we are testing now for +")
                        new = []
                        tf = []

                        for index, i in enumerate(Monkey_items[Mon_num]):
                            if type(i) != int:
                                num = [int(x) for x in i.split(',') if x.isdigit()]

                            else: num = [i]
                            #print(num) 
                            Monkey_inspection[Mon_num] += 1
                    #        print("running")
                            if w.isdigit() == True:
                    #            print((num[0]))
                                new_num = int(num[0]) + int(w)

                    #            print(new_num)


                            else: 
                                new_num = int(num[0])*2
                            
                            new_num %= mod 
                                

                            new.append(new_num)
                            if new_num%int(l[-1]) == 0:
                    #            print(l[-1])
                                
                                tf.append('true')
                            else: tf.append('false')

                                
                    continue

                else:
                    for v in range(len(tf)):
                        #print(key)
                        #print(val)
                        if tf[v] == l[1].split(':')[0]:
                    #        print("throw it")
                    #        print(l[-2]+l[-1])
                            mon = l[-2]+l[-1]
                            mon = mon.capitalize()
                    #        print(mon)
                            


                            #print(Monkey_items[mon])
                            Monkey_items[mon].append(new[v])
                            #print(Monkey_items)
                            (Monkey_items[Mon_num].pop(0))
                            #print(Monkey_items)
                            #print(Monkey_items[Mon_num].pop(0))
                

    #print(Monkey_items)
    #print(Monkey_inspection)
    list = []
    for key, value in Monkey_inspection.items():
        list.append(value)

    #print(list)


    list.sort()
    #print(list)
    print(list[-1] * list[-2])                   


