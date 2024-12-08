def double_odd_numbers(numbers: list[int]) -> list[int]:
    def is_odd(number: int) -> bool:
        return number % 2 == 1

    def double(number: int) -> int:
        return number * 2

    return [double(number) for number in numbers if is_odd(number)]


print(double_odd_numbers([1, 2, 3, 4, 5]))
