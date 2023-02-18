def stvorce_do(n):
  if n <= 0:
    return None
  counter = 0
  while counter ** 2 < n:
    print(counter ** 2)
    counter += 1

stvorce_do(10)