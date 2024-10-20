def is_pangram(string: str) -> bool:
    return len(set([char.lower() for char in string if char.isalpha()])) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog."))
print(is_pangram("Obviously not a pangram"))