def is_palindrome(word):
  if len(word) == 0:
    return True
  if word[0] == word[-1]:
    return is_palindrome(word[1: -1])
  return False

print(is_palindrome("noon"))  # True
print(is_palindrome("moon"))  # False