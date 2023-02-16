n = int(input())

def del_5(n):
    a = 0
    for i in range(n):
        b = int(input())
        if b%5 == 0:
            a = a+1
    print(a)
    return 
    
del_5(n)