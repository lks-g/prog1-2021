def pohyb_veze(x1,y1,x2,y2):
    if x1 == x2 and y1 == y2:
        return False
    elif x1 == x2:
        return True
    elif y1 == y2:
        return True
    else:
        return False

a = pohyb_veze(1,1,4,1)
print(a)