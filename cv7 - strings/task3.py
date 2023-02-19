"""
Funkcia sa pozrie na zadaný parameter
v ktorom ak nájde malé písmeno
vráti true alebo false ak nenájde nič.
"""

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

"""
Iteruje všetky písmená v reťazci, potom sa rozhoduje
o konštantnom "c" či je malé alebo veľké písmeno.
Následovne funkcia vracia hodnotu True.
Táto funkcia nespĺňa cielové podmienky
"""

def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"

"""
Iteruje všetky písmenká v reťazci, potom vytvára premennú
v rámci for-cyklu, kde ukladá boolean hodnotu či je aktualne
písmenko malé alebo veľké. Na konci vráti hodnotu premennej
flag. Na konci funkcia aj tak nespĺňa cielové podmienky lebo vracia
len hodnotu posledného písmenka.
"""

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

"""
Deklaruje premennú "flag" s hodnotou False. Následovne iteruje
všetky písmenká v reťazci a v tele cyklu obnoví hodnotu premennej "flag"
na logický súčet, teda OR hodnoty "flag" a hodnoty písmenka či je malé
alebo veľké. Uplatnuje sa zákon agresivnej jednotky, preto akonáhle
.islower() vráti True, flag sa zmení na True a ostáva v tom stave
až do konca funkcie. To znamená, že táto funkcia spĺňa cielové podmienky.
"""

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

"""
Iteruje všetky písmenká v reťazci až kým sa nájde veľké písmeno,
funkcia vráti hodnotu False, ak sa nenájde žiadne veľké písmeno,
vracia hodnotu True. Táto funkcia nespĺňa cielové podmienky.
"""

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True