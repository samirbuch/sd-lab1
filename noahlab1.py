import random as r
import math as m

def isPrime(num):
    if (num == 2 or num == 3):
        return True
    limit = m.floor(num**(1/2))
    i = 2
    while (i < limit):
        if num % i == 0:
            return False
        i += 1
    return True

list = [x for x in range(1,101)]

random_list = sorted(r.sample(list,20))



evens = []
odds = []
sum = 0
max_prime = -1
perfect_squares = []
for i in random_list:
    if (i % 2 == 0):
        evens.append(i)
    else:
        odds.append(i)
    
    sum += i

    if isPrime(i) and i > max_prime:
        max_prime = i
    
    if m.floor(i**(1/2)) == i**(1/2):
        perfect_squares.append(i)

print('Evens:', evens)
print('Odds:', odds)
print('Perfect Squares:',perfect_squares)
print('End Sum: ', sum)
print('Max Prime:',max_prime)
