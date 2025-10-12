import random

def produit(num):
    list = []
    for i in range(6, 15):
        list.append(num * i)
    print(random.choice(list))
    #return list

    
print (produit(7))
