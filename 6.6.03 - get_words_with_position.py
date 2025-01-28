def get_words_with_position(words):
    return [(value, index) for index, value in enumerate(words.split(), 1)]

print(get_words_with_position('Куда ты тянешь свои ручки'))
print(get_words_with_position('И тянутся города Я в каждом из них бывал'))