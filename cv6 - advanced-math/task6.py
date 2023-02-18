def pocet_rovnych_najv():
  najvacsie = int(input("Enter a number: "))
  pocet_rov = 0
  while True:
    cislo = int(input("Enter a number: "))
    if cislo > najvacsie:
      najvacsie = cislo
      pocet_rov = 0
    if cislo == najvacsie:
      pocet_rov += 1
    if cislo == 0:
      return pocet_rov

print(pocet_rovnych_najv())