'''
 How many characters need to be processed before the first start-of-packet marker is detected?
 for e.g.: mjqjpqmgbljsphdztnvjfqwrcgsmlb
 The first time a marker appears is after the seventh character arrives. 

'''

### define a function that returns the number of processed characters 
### before the first start-of-packet marker is detected
def processed_unique_char(string_list, part):
    #l = []

    ### PART 1. ---------------------------------------------------------------------------------------
    if part == 1:
        for i, x in enumerate(string_list):
            l = string_list[i:i+4]
            #print(l)
            if len(set(l)) == len(l):
                #print(l)
                return i+4
                        
            else:
                l = []
            
    ### PART 2. ------------------------------------------------------------------------------------------
    if part == 2:
        for i, x in enumerate(string_list):
            l = string_list[i:i+14]
            if len(set(l)) == len(l):
                #print(l)
                return i+14
                        
            else:
                l = []



"""
example lists:
#str_list = ['n','f','d','d','s','a','w','x']
#str_list = ['n','f','d','d','j','z','j','j','j','m','r', 'h','i']
#str_list = ['b','v','w','b','j','p','l','b']
#print(processed_unique_char(str_list, 1))
"""


with open('day06.txt', 'rt') as myfile:
    line = myfile.read()
    #print(type(line)) ### nfddjzjjjmr...
    line = list(line)
    #print(line) ### ['n', 'f', 'd', 'd', 'j', 'z', 'j', 'j', 'j', ... ]

    print('Please enter the part you want to run 1/2: ')
    PART = int(input())
    print(processed_unique_char(line, PART))
    #print(unique_14_index(line))

