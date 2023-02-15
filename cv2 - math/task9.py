# 9
def arit(a, d):
    print(a + d)

a, d, n = map(int, input("Enter 3 numbers: ").split())

for i in range(n):
    arit(a, d*i)