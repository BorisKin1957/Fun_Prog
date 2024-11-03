def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    '''Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)'''
    L = lst.copy()
    if abs(shift)  > len(L):
        shift = shift % len(L)
    if shift >= 0:
        L = L[-shift:] + L[:-shift]
    else:
        L = L[abs(shift):] + L[:abs(shift)]
    return L

nums = [1, 2, 3, 4]
new_nums = rotate(nums)
print(nums)
print(new_nums)

print()

print(rotate([1, 2, 3, 4, 5, 6], 7))

print()
print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate([1, 2, 3, 4, 5, 6], -3))

print()

print(rotate([1, 2, 3, 4, 5, 6, 7], 21))
