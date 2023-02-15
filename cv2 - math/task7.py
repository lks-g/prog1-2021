# 7
def vratit_sucet(n):
    s = 0
    for i in range(n):
        s += (i + 1)**2
    return s

a = vratit_sucet(8)
print(a)