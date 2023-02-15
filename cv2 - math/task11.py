# 11
pole = []

def geo_rad(a, d):
    pole.append(a*d)
    print(sum(pole))

a, d, n = map(int, input("Enter 3 numbers: ").split())

for i in range(n):
    geo_rad(a, d**i)