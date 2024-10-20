correct = ['a','e', 'i', 'o', 'u']

def translate_to_robber_lang(string: str) -> str:
    result = []
    for char in string:
        if char.isalpha() and char.lower() not in correct:
            new = char + 'o' + char
            result.append(new)
        else:
            result.append(char)
    return ''.join(result)

print(translate_to_robber_lang("This is kinda fun"))
print(translate_to_robber_lang("I Think YoU Might BE righT!"))