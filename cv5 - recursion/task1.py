def sucet(n):
    if n == 0:
        return n
    else:
        return n + sucet(n - 1)

print(sucet(4))  # 10