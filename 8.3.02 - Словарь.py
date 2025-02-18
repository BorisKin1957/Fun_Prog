def alphabet():
    letter = yield
    while True:
        letter = yield DICTIONARY[letter]


DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
    'e': 'elephant',
    'f': 'fox',
    'g': 'gorilla',
    'h': 'hippo',
    'i': 'iguana',
    'j': 'jaguar',
    'k': 'koala',
    'l': 'llama',
    'm': 'monkey',
    'n': 'newt',
    'o': 'octopus',
    'p': 'parrot',
    'q': 'quail',
    'r': 'rabbit',
    's': 'squirrel',
    't': 'tiger',
    'u': 'unicorn',
    'v': 'viper',
    'w': 'walrus',
    'x': 'xenomorph',
    'y': 'yak',
    'z': 'zebra'
}


coro = alphabet()
next(coro)
print(coro.send('a'))
print(coro.send('b'))
print(coro.send('c'))
print(coro.send('d'))