# 10
def geom(a, d):
    print(a * d)

a, q, n = map(int,input("Enter 3 numbers: ").split())

for i in range(n):
    geom(a, q**i)