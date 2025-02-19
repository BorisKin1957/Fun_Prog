def words_length(lst):
    global words
    words = [len(word) for word in lst]

words = ['Python', 'is', 'awesome!']
result = words_length(words)
print(words)
print(result)