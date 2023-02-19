def rotate_letter(letter, n):
    if letter.isupper():
        a = ord('A')
        
    elif letter.islower():
        a = ord('a')
        
    else:
        return letter

    c = ord(letter) - a
    i = (c + n) % 26 + a
    return chr(i)

def rotate_word(word, n):
    res = ''
    for letter in word:
        res+=rotate_letter(letter, n)
    return res

if __name__ == '__main__':
    print(rotate_word('cheer', 7))   # jolly
    print(rotate_word('melon', -10)) # cubed
    print(rotate_word('sleep', 9))   # bunny