x = list(input())

def funct(x):
    ans = None
    if int(x[0]) < int(x[1]):
        ans = x[1]
    if int(x[0]) < int(x[2]):
        ans = x[2]
    ans = int(x[0])
    return ans

print(funct(x))