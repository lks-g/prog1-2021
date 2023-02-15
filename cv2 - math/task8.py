# 8
def grid(n):
    for i in range(n):
        for j in range(n):
            print('+', end=' ')
            print('- '*4, end='')
        print('+')
        for k in range(4):
            for i in range(n):
                print("|", end=' ')
                print(" "*8, end='')
            print("|")
    for i in range(n):
        print('+', end=' ')
        print('- '*4, end='')
    print('+')
a = 2 
grid(a)