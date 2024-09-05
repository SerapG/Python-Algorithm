# Big O Notation -> O() #
# Time Complexity - Space Complexity #

import math
def bigon(n):
    for i in range(0, n):
        print(i)
bigon(5)
def bigon2(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i, j)
bigon2(5)
def bigon3(n):
    for i in range(0, n):
        for k in range(0, n):
            for j in range(0, n):
                print(i, k, j)
bigon3(5)

def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)
logn(8)