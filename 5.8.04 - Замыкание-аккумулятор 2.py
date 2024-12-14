def create_accumulator(result=0):
    def accumulator(n):
        nonlocal result
        result += n
        return result
    return accumulator

summator_1 = create_accumulator(200)
print(summator_1(5))
print(summator_1(7))
print(summator_1(2))

summator_2 = create_accumulator()
print(summator_2(3))
print(summator_2(6))

print()

closure = create_accumulator(300)

print(closure(4))
print(closure(400))
print(closure(4.5))
print(closure(0.5))

closure_2 = create_accumulator()

print(closure_2(0))
print(closure_2(1))
print(closure_2(3))
print(closure_2(7))