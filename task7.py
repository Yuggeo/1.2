x = str(input())
def func(x):
    x = list(x)
    small = 0
    big = 0
    for y in x:
        if y.islower() == True:
            small += 1
        elif y.isupper():
            big += 1
    return (small, big)

print(func(x))
