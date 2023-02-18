def tretie_najvacsie_zadane(n):
  if n == 1:
    return int(input("Enter a number: "))

  tretie_najvacsie = None
  druhe_najvacsie = None
  najvacsie = None

  for _ in range(n):
    cislo = int(input("Enter a number: "))
    if najvacsie:
      if najvacsie < cislo:
        tretie_najvacsie = druhe_najvacsie
        druhe_najvacsie = najvacsie
        najvacsie = cislo
      else:
        if druhe_najvacsie:
          if druhe_najvacsie < cislo:
            tretie_najvacsie = druhe_najvacsie
            druhe_najvacsie = cislo
          else:
            if tretie_najvacsie:
              if tretie_najvacsie < cislo:
                tretie_najvacsie = cislo
            else:
              tretie_najvacsie = cislo
        else:
          druhe_najvacsie = cislo
    else:
      najvacsie = cislo
  return tretie_najvacsie

print(tretie_najvacsie_zadane(4))

## Ver. 2
def tretie_najvacsie_zadane_v2(n):
  cisla = []
  for _ in range(n):
    cislo = int(input("Enter a number: "))
    cisla.append(cislo)
  cisla.sort()
  return cisla[n - 3]

print(tretie_najvacsie_zadane_v2(4))