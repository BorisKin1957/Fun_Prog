def alphabet():
    letter = yield
    while True:
        try:
            if letter in DICTIONARY:
                letter = yield DICTIONARY[letter]
            else:
                DICTIONARY[letter] = 'default'
        except KeyError:
            letter = yield 'default'





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
print(coro.send('apple'))
print(coro.send('banana'))
print(coro.throw(KeyError))
print(coro.send('dog'))
print(coro.send('d'))

print()
coro = alphabet()
next(coro)
for letter in 'qwerty':
    print(coro.send(letter))
    print(coro.throw(KeyError))

