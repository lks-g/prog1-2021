def druhe_max(n):
    a = input()
    b = input()
    c1 = int(a)
    c2 = int(b)

    if c1 > c2:
        max1 = c1
        max2 = c2
    else:
        max1 = c2
        max2 = c1
    for i in range(n-2):
        vstup = input()
        cislo = int(vstup)
        if cislo > max1:
            max2 = max1
            max1 = cislo
        elif cislo > max2:
            max2 = cislo
    return max2

a = druhe_max(8)
print(a)