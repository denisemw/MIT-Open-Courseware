'''count = 0
number = 2
primes = []
while count < 1000:
    cnt = 1
    isPrime = True
    for i in range(2,number):
        if number % i == 0:
            isPrime=False
            break
    if isPrime:
        count +=1
        if count==1000:
            print number
    number +=1
'''
from math import *
number = 2
end = input()
total = 0.0
while number <= end:
    cnt = 1
    isPrime = True
    for i in range(3,number):
        if number % i == 0:
            isPrime=False
            break
    if isPrime:
        total += log(number)
    number +=1
print end
print total
print total/end
