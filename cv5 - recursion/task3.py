def pocet_parnych(n):
  a = int(input("Enter a number: "))
  if n == 1:
    return 1 if a % 2 == 0 else 0
  if a % 2 == 0:
    return 1 + pocet_parnych(n - 1)
  else:
    return pocet_parnych(n - 1)

print(pocet_parnych(4))