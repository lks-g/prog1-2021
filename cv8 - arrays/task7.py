def lr_nb(t):
    count = 0
    index = 1
    
    while index < len(t) -1:
        if (t[index] > t[index - 1]) and (t[index] > t[index + 1]):
            count += 1
        index += 1
    return count

print(lr_nb([1, 5, 2, 3, 20, 4, 25, 5]))  # 3