def is_anagram(word1, word2):
     return sorted(word1) == sorted(word2)

print(is_anagram("race", "care")) # True
print(is_anagram("car", "cake"))  # False 