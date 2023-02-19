"""
Funkcia vráti prvý a posledný element zo zoznamu.
    t: zoznam.
    return: vráti nový list.
"""

def middle(t):
    return t[1:-1]

print(middle([1, 2, 3, 4])) # [2, 3]