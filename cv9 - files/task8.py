import time

def versionone():
  lst = []
  with open("words.txt", "r") as txt:
    for line in txt:
      lst.append(0)

def versiontwo():
  lst = []
  with open("words.txt", "r") as txt:
    for line in txt:
      lst = lst + [0]

t1 = time.perf_counter()
versionone()
t2 = time.perf_counter()
versiontwo()
t3 = time.perf_counter()

print(f"Cas s append() {t2-t1}s. \nCas s t = t + [x] {t3-t2}s.")