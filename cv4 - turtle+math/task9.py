import math

def najmen(n):
    b = math.inf
    for i in range(n):
        a = int(input("Add number "))
        if a < b:
            b = a
    print(b)
    return

najmen(4)