
### 1. my_max

def my_max(l):
    max = 0
    for i in l:
        if i > max:
            max = i

    return max

l = list(map(int, input().strip().split()))
largest_number = my_max(l)
print(largest_number)
#print(l)

### 2. process_list

def process_list(l):
    
    for i, x in enumerate(l):
        if x % 2 != 0:
            x = x*2
            l[i] = x
        else:
            x = x/2
            l[i] = x

        if i%7 == 0:
            x = x+i
            l[i] = x

    largest_number = my_max(l)
    print(largest_number)


process_list(l)



### 3. Collatz Conjecture

def collatz(n):
    
    l = [n]

    #print(l)
       #return l.count(n)
    #print(len(l))
    #print(len(set(l)))
    while len(l)==len(set(l)):
        #print(len(l))
        n = n/2 if n%2==0 else n*3 +1
        l.append(n)

    return l[len(l)-1]
        

n = int(input())
print(collatz(n))



### 4. compute pi

def compute_pi(steps):
    num = 0
    for i in range(1, steps+1):
        num = num + (-1)**(i-1)/(2*i -1)

    pi = num * 4
    return pi

steps = int(input())
pi_value = compute_pi(steps)
print(pi_value)



### 5. cube root

def integer_cube_root(n):
    k = 1
    while k**3 < n:
        k = k+1
    return k

n = int(input())
#n, k = map(int, input().split())
small_k = integer_cube_root(n)
print(small_k)



### 6. Encryption

a = input()
a = a.upper()
a = list(a)
for i, x in enumerate(a):
    if ord(x) != 32:
        a[i] = chr(ord(x) + 3)

a = "".join(a)
print(a)

### general encryption funtion

def caeser_encrypt(string, shifts):
    string = list(string.upper())
    for i, x in enumerate(string):
        if ord(x) != 32:
            string[i] = chr(ord(x)+shifts)

    C_encrypt = "".join(string)
    return C_encrypt

shifts, string = input().split(maxsplit=1)
shifts = int(shifts)
encrypt_string = caeser_encrypt(string, shifts)
print(encrypt_string)



### 7. DNA reverse complement

DNA = input()
#DNA = list(DNA)
#rev = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
rev_DNA = list(DNA)
for i, x in enumerate(DNA):
    if x == 'A':
        rev_DNA[i] = 'T'
    elif x == 'T':
        rev_DNA[i] = 'A'
    elif x == 'C':
        rev_DNA[i] = 'G'
    elif x == 'G':
        rev_DNA[i] = 'C'

rev_DNA = "".join(rev_DNA)[::-1]
print(rev_DNA)


### 8. Insertion sort 
def insertion_sort(l):
    for i in range(1, len(l)):
        val = l[i]
        j = i
        while (j > 0) and (l[j - 1] > val):
            l[j] = l[j-1]
            j -= 1

        l[j] = val
    return l

l = list(map(int, input().strip().split()))
sort_list = insertion_sort(l)
print(sort_list)




### 9. Fibonacci numbers

def Fibonacci_num(n):
    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

    return fibonacci

n = int(input())
fib_number = Fibonacci_num(n)
print(fib_number)


