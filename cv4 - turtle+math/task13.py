from task11 import *

# 1. cast ulohy
def test_prvociselnosti(a):
  if a < 2:
    raise ValueError("Prvocislo nemoze byt menise ako 2")
  for i in range(2, a):
    if delitelnost(a, i):
      return False
  return True

# 2. cast ulohy
print("Vsetky provocisla mensie ako 50 su:")
for i in range(2, 50):
  if test_prvociselnosti(i):
    print(i)