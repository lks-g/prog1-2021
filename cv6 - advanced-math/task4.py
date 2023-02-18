def poradie_najvacsieho():
  poradie = 1
  poradie_najv = 1
  najvacsie = int(input("Enter a number: "))
  while True:
    cislo = int(input("Enter a number: "))
    poradie += 1
    if cislo > najvacsie:
      najvacsie = cislo
      poradie_najv = poradie
    if cislo == 0:
      return poradie_najv

print(poradie_najvacsieho())