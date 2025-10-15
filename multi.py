import time
import random
def func(num):
    list = []
    for i in range(6, 15):
        list.append(num * i)
        #if i == 9:
            #continue
    answer = random.choice(list)
    startt = time.time()
    inputt = int(input(f"{num} x {int(answer / num)} = "))
    endd = time.time()
    timee = endd - startt
    return answer, inputt, timee
number = int(input("quelle nombre:"))
while True:
    answerr, inputtt, timee = func(number)
    if inputtt == answerr:
        print("good")
        print(f"Ca pris {timee}")
        
    else:
        print(f"bonne reponse {answerr}")
        print(f"Ça pris {timee:.2f}")

