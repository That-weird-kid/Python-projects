import random
numDivisibles = []
def func(number):
    numDivisibles.clear()
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            numDivisibles.append(i)
        if numDivisibles == []:
            return False
        return True
        print(numdivisibles)
a = random.choice(range(1,101))
print(a)    
inputt = input("is it a prime  y/n:")
print(func(a))
if inputt == n:
    if a == False:
        print("bravo")
    else:
        print(numDivisibles)
if inputt:
    
