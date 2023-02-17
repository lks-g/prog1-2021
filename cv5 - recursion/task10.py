def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

print(gcd(30, 20))  # 10
print(gcd(8, 12))   # 4