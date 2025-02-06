def is_palindrome(word):
    if not word:
        return True
    return word[0].upper() == word[-1].upper() and is_palindrome(word[1:-1])

print(is_palindrome('Hello'))
print(is_palindrome('HeLlO'))
print(is_palindrome('hhhhh'))
print(is_palindrome('abba'))
print(is_palindrome('Racecar'))