def len_raz(t):
    pocet = 0
    for x in t:
        if t.count(x) == 1:
            pocet += 1
    return pocet

print(len_raz([1, 2, 3, 3, 4, 4, 5, 5,6])) # 3