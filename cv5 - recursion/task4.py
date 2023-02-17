def biggest(n):
  a = int(input("Enter a number: "))
  if n == 1:
    return a
  
  b = biggest(n - 1)
  return a if a > b else b

print(biggest(3))