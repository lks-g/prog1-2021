def delitelnost(a,d):
    if a%d == 0:
        return True
    elif a%d > 0:
        return False

a = delitelnost(5,5)
print(a)

def delitelnost(a,d):
    if(a%d == 0):
        return True
    elif(a%d > 0):
        return False

def delitelnost_12():
    vstup_a = int(input("Zadaj a: "))
    for i in range(1, vstup_a + 1):
        if delitelnost(vstup_a, i):
            print(i)
        
delitelnost_12()