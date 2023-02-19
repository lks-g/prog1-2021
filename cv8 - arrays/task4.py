def is_sorted(t):    
    return t == sorted(t)

print(is_sorted([1, 2, 2]))     # True
print(is_sorted(["b", "a"]))    # False