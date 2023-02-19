def par_zoz(t):
    sum = 0
    for x in t[::2]:
        sum += x
    return sum

print(par_zoz([3, 6, 4, 6, 2])) # 9
print(par_zoz([1, 6, 1, 6, 1])) # 3