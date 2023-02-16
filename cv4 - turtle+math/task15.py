def is_black(x, y):
  if x % 2 == 0 and y % 2 == 0:
    return True
  elif x % 2 != 0 and y % 2 != 0:
    return True
  else:
    return False

def rovnaka_farba(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")
  
  if not(is_black(x1, y1) != is_black(x2, y2)):
    return True
  return False

print(rovnaka_farba(1, 1, 2, 6))  # True
print(rovnaka_farba(2, 2, 2, 5))  # False