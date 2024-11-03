from typing import List, Optional


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    '''Находит первый дубль в списке'''
    L = [x for x in words if words.count(x) > 1]
    D = {}
    for char in L:
        count = 0
        for i in range(len(L[count:])):
            if char != L[i]:
                count += 1
            else:
                D[char] = count
    result = sorted(D, key=lambda x: x[1])
    if result:
        return result[0]
    return None


print(get_first_repeated_word.__doc__)
print(get_first_repeated_word.__annotations__)
print(get_first_repeated_word(['hello', 'hi', 'hello']))

print('-' * 40)

print(get_first_repeated_word.__doc__)
print(get_first_repeated_word.__annotations__)
print(get_first_repeated_word(['hello', 'hi', 'Hello']))

print('-' * 40)

print(get_first_repeated_word(['ab', 'ca', 'bc', 'ab']))

print('-' * 40)

print(get_first_repeated_word(['ab', 'ca', 'bc', 'Ab', 'cA', 'aB', 'bc']))

print('-' * 40)

print(get_first_repeated_word(['ab', 'ca', 'bc', 'ca', 'ab', 'bc']))