def rotate_letter(letter: str, shift: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_index = alphabet.find(letter)
    new_index = (char_index + shift) % 26
    return alphabet[new_index]


print(rotate_letter.__doc__)
print(rotate_letter.__annotations__)
print(rotate_letter('a', 3))

print()

print(rotate_letter('d', -2))
print(rotate_letter('w', -26))
print(rotate_letter('w', -27))
print(rotate_letter('a', 53))