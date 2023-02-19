def p_roz(t):
    return len(set(t))

print(p_roz([1, 2, 2, 4, 5, 4]))        # 4
print(p_roz([5,5,5,5,2]))               # 2  
print(p_roz([1,2,3,4,5,6,6,7,8,9,10]))  # 10