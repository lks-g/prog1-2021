from task9 import *

def is_reversepair(a, b):
  return a == b[::-1]

words = []
with open("words.txt", "r") as txt:
  for line in txt:
    words.append(line.strip())

print("Vsetky reverse pair:") 
for word in words:
  if in_bisect(words, word[::-1]):
    print(f"  pair: {word}, {word[::-1]}")

# Linearne prehladavanie (Velmi pomale)
# for i in range(len(words)):
#   for j in range(i+1, len(words)):
#     if is_reversepair(words[i], words[j]):
#       print(f"  pair: {words[i]}, {words[j]}")