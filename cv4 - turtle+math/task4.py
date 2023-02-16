def min_of_three(a,b,c):
    if (a < b and a < c):
        return a
    elif(b < c):
        return b
    else:
        return c

a = min_of_three(7,5,8)
print(a)