# 12
a0 = 5
r = 0.9
cislo = a0/(1 - r)

print(cislo)
print()

for i in range(100):
    print(a0 * r**i)