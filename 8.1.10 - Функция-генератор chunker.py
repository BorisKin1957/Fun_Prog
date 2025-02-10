def chunker(iterable, lenght):
    while iterable:
        yield iterable[:lenght]
        iterable = iterable[lenght:]

text = '''Python 3.12 is the latest stable release of the Python programming language, with a mix of changes to the language and the standard library.'''

for chunk in chunker(text, 7):
    print(chunk)

for chunk in chunker(range(56), 9):
    print(list(chunk))