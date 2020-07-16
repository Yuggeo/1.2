import random
a = random.randint(1, 10)
b = "exit"

while True:
    x = input("number: ")

    if x == b:
        break

    x = int(x)
    if a < x:
        print("too high")
    elif a > x:
        print("too low")
    elif a == x:
        print("correct")
        break
