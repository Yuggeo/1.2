x = list(input())

def funct(x):
    c=0
    for y in x:
        c += int(y)
    return c

print(funct(x))