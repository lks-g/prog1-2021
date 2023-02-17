def delitelost(a, d):
    if a%d == 0:
        return True
    else:
        return False

def test_prvociselnosti(a):
    if a == 2:
        return True
    for i in range(2, a):
        if a%i == 0:
            return False
    return True

def sucet_prvocisel_po(n):
    if n == 2:
        return 0
    else:
        sucet = sucet_prvocisel_po(n-1)
        if test_prvociselnosti(n-1):
            sucet = sucet + n - 1
        return sucet

a = sucet_prvocisel_po(5)
print(a)