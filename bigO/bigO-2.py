import math
def nlogn(n):
    lim=n
    while n>1:
        n= math.floor(n/2)
        for i in range(1,lim):
            print(i)
nlogn(16)
def nfactorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0, n):
            print(i)
            nfactorial(n-1) # recursive
nfactorial(0)
