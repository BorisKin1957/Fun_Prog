DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog'
    }

def alphabet():
    for char, word in DICTIONARY.items():
        yield char, word

g = alphabet()
letter, word = next(g)
print(letter, word)
print(next(g))
print(next(g))