"""
Funkcia vypočíta kumulatívny súčet (medzisúčet) čísel zo zoznamu t.
  t: zoznam čísel.
  total: premenná do ktorej sa zapíše výsledok.
  res: zoznam do ktorého uložíme výsledný zoznam.
  res.append: pridá zoznam do premennej total.
"""

def c_sum(t):
    total = 0
    res = []
    
    for x in t:
        total += x
        res.append(total)
    return res

print(c_sum([1,2,3]))  # [1, 3, 6]