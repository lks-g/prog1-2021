def pocet_vacsich():
  pocet = 0
  predosle = int(input("Enter a number: "))
  while True:
    cislo = int(input("Enter a number: "))
    if cislo > predosle:
      pocet += 1
    if cislo == 0:
      return pocet
    predosle = cislo

print(pocet_vacsich())