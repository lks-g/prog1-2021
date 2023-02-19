"""
Funkcia spočíta všetky čísla v zozname a vráti ich do premennej total.
    t: zoznam zoznamu čísel
    total: spolu / Total
    return: totálny výsledok
"""
def nested_sum(t):
    total = 0
    for i in t:
        total += sum(i)
    return total

print(nested_sum([[1,2], [3], [4,5,6]]))  # 21