import random as r
import math as m


list = [x for x in range(1,101)]

random_list = r.sample(list,20)

print('Evens:')
for i in random_list:
    if (i % 2 == 0):
        print(i,end=', ')


print()

print('Odds')
for j in random_list:
    if (j % 2 != 0):
        print(j,end=', ')


sum = 0
for i in random_list:
    sum += i


print('\n\nEnd sum:',sum)

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

primes  = []
for num in random_list:
    if isPrime(num):
        primes.append(num)


print('\nMax Prime: ', max(primes))