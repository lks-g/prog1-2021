def pocet_rovnakych(a,b,c):
    if (a == b and a == c):
        return 3
    elif (a == b or a == c or b == c):
        return 2
    else:
        return 0

a = pocet_rovnakych(1,1,1)
b = pocet_rovnakych(1,2,1)
c = pocet_rovnakych(1,2,3)

print(a)
print(b)
print(c)