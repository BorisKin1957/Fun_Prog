def filter_words(wordlist):
    return list(filter(lambda x: x[0] == 'S' or len(x) == 4, wordlist))

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six',
        'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
print(filter_words(days))

words = ['scheme', 'hypnothize', 'exposure', 'Syndrome',
         'Save', 'speculate', 'cane', 'welfare', 'blame', 'core']
print(filter_words(words))