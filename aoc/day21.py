"""
Each monkey is given a job: either to yell a specific number or to yell the result of a math operation.
Part 1: Job is to work out the number the monkey named root will yell before the monkeys figure 
it out themselves.

root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32

"""

### defining a recursive function to run over all equations -----------------------------------------------
def root_monkey_call(monkey_name):

    val = dic[monkey_name].split()
    #print(dic[monkey_name].split())
    if len(val) != 1: ### mathematical operation of two variables like: ['pppw', '+', 'sjmn'] -------------
        num1, num2 = root_monkey_call(val[0]), root_monkey_call(val[2])
        #print(num1, num2)
        #print(type(num1), type(num2))
        equation = num1 + val[1] + num2
        #print(equation)
        return str(eval(equation)) ### type(eval(equation)) == int (or float for / operation) ------------- 
        
    
    return val[0]



with open('day21.txt', 'rt') as myfile:
    lines = myfile.read().split('\n')

    #print(lines) ### ['root: pppw + sjmn', 'dbpl: 5', ...] ------------------------------------------------

    dic = {} ### converting this list into a dictionary ---------------------------------------------------- 

    for l in lines:
        #print(l.split(": "))  ### ['root', 'pppw + sjmn'] -------------------------------------------------
        monkey, equation = l.split(': ')
        #print(monkey, equation)
        dic[monkey] = equation

    #print(dic) ### {'root': 'pppw + sjmn', 'dbpl': '5', ...} ----------------------------------------------
    #print(dic['root'])

    #print(dic['root'].split())

    if dic['root'].isdigit != True: 
        #part = int(input())
        #if part == 1:
        num = root_monkey_call('root')

        
    ### type(num) == str
    ### type(eval(num)) == float
    ### type(int(eval(num))) == int
    print(int(eval(num)))