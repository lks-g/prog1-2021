def dlzka_podpostupnosti():
  dlzka = 1
  cislo = None
  najdlhsia_dlzka = 1
  predosle_cislo = int(input("Enter a number: "))
  while cislo != 0:
    cislo = int(input("Enter a number: "))
    if cislo == predosle_cislo:
      dlzka += 1
    else:
      if dlzka > najdlhsia_dlzka:
        najdlhsia_dlzka = dlzka
        dlzka = 1
    predosle_cislo = cislo
  return najdlhsia_dlzka

print(dlzka_podpostupnosti())