def get_letters(string):
    return list(map(lambda x: (x.upper(), x.lower()), string))

print(get_letters('TykPe'))
print(get_letters('WelLDone'))