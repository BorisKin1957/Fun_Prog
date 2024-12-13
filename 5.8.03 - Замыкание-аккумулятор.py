def create_accumulator():
    result = 0
    def accumulator(n):
        nonlocal result
        result += n
        return result
    return accumulator

summator_1 = create_accumulator()
print(summator_1(5))
print(summator_1(7))
print(summator_1(2))

summator_2 = create_accumulator()
print(summator_2(3))
print(summator_2(6))