def find_different_indexes(s1, s2):
    result = map(lambda x, y: x != y, s1, s2)
    return [i for i, x in enumerate(result) if x]


print(find_different_indexes('abcd', 'artd'))
print(find_different_indexes('abcd', 'abcd'))
print(find_different_indexes('abracadabra', 'uzrucuduzru'))