"""
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122

The digits are 2, 1, 0, minus (written -), and double-minus (written =). 
Minus is worth -1, and double-minus is worth -2."
"""

def to_decimal(snafu):
    digits = len(snafu)
    num = 0
    
    for i in range(digits):
        #print('num is: ',num)
        if l[i] == '-':
            num += 5**(digits-(i+1)) * -1  
            continue
        if l[i] == '=':
            num += 5**(digits-(i+1)) * -2
            continue
        num +=  5**(digits-(i+1)) * int(l[i])
    return num

def to_snafu(decimal):
    SNAFU = []

    five_base = []

    while decimal > 0:
        r = decimal % 5
        decimal = decimal // 5

        five_base.append(r)
    #print(five_base)
    #five_base.reverse()
    #print(five_base)

    for index, i in enumerate(five_base):
        if i <= 2:
            SNAFU.append(str(i))
        elif i == 3:
            SNAFU.append('=')
            five_base[index+1] += 1 
        elif i == 4:
            SNAFU.append('-')
            five_base[index+1] += 1
        elif i == 5:
            SNAFU.append('0')
            five_base[index+1] += 1
        #print(five_base)
    

    SNAFU.reverse()
    SNAFU = ''.join(SNAFU)
    return (SNAFU)



with open('day25.txt', 'rt') as myfile:
    lines = myfile.read().split('\n')
    #print(lines) ### ['1=0-12100-==', '12=2=21=2-1=1122', '1=-1112=-12', ...] ------------------------------

    numbers = []
    num = 0
    for l in lines:
        #print((l))
        digits = len(l)
        #print(digits)
        #num = 0
        num += to_decimal(l)
            #print(num)

    #print(num)

    #SNAFU = []

    print(to_snafu(num))


