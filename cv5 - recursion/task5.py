def je_sucet_parny(n):
  a = int(input("Enter a number: "))
  if n == 1:
    return True if a % 2 == 0 else False

  parita_b = je_sucet_parny(n - 1)
  if not((a % 2 == 0) != parita_b):
    return True
  return False

print(je_sucet_parny(3))