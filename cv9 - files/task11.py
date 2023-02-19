from task9 import *

def is_interlock(words, il_word):
  return (in_bisect(words, il_word[::2]) and
          in_bisect(words, il_word[1::2]))

def is_triple_interlock(words, il_word):
  return (in_bisect(words, il_word[::3]) and
          in_bisect(words, il_word[1::3]) and
          in_bisect(words, il_word[2::3]))

words = []
with open("words.txt", "r") as txt:
  for line in txt:
    words.append(line.strip())
 
print("Kazdy interlock z words.txt:")
for word in words:
  if is_interlock(words, word):
    print(f"  {word} je interlock {word[::2]} a {word[1::2]}")
     
print("Kazdy trojnasobny interlock:")
for word in words:
  if is_triple_interlock(words, word):
    print(f"  {word} je interlock {word[::3]}, {word[1::3]} a {word[2::3]}")