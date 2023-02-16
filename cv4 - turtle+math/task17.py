def pohyb_strelca(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")
  
  if abs(x1 - x2) == abs(y1 - y2):
    return True
  return False

print(pohyb_strelca(4, 4, 5, 5))  # True
print(pohyb_strelca(4, 4, 5, 4))  # False