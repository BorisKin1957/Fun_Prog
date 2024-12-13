def make_repeater(n: int) -> callable:
    def inner(line: str)-> str:
        return n * line
    return inner

repeat_5 = make_repeater(5)
print(repeat_5('Hello'))
print(repeat_5('World'))

repeat_2 = make_repeater(2)
print(repeat_2('Pizza'))
print(repeat_2('Pasta'))