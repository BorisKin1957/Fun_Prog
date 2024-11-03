def rotate_letter(letter: str, shift: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_index = alphabet.find(letter)
    new_index = (char_index + shift) % 26
    return alphabet[new_index]


def caesar_cipher(phrase: str, key: int) -> str:
    '''Шифр Цезаря'''
    result = ''
    for letter in phrase:
        if letter.isalpha():
            result += rotate_letter(letter, key)
        else:
            result += letter
    return result


print(caesar_cipher('lost in the echo', 1))