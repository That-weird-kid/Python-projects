import random
numDivisibles = []
def func(number):
    numDivisibles.clear()
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            numDivisibles.append(i)
        if numDivisibles == []:
            return True
        return False
        print(numdivisibles)
a = random.choice(range(1,101))
print(a)
b = func(a)
inputt = input("is it a prime  y/n:")
if inputt == "n":
    if b == False:
        print("bravo")
    else:
        print(numDivisibles)
if inputt == "y":
    if b == True:
        print ("bravo")
        print(numDivisibles)
    else:
        print("bad")
        print(numDivisibles)
