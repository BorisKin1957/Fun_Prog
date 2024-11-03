def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    '''Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)'''
    if abs(shift)  > len(tpl):
        shift = shift % len(tpl)
    if shift >= 0:
        tpl = tpl[-shift:] + tpl[:-shift]
    else:
        tpl = tpl[abs(shift):] + tpl[:abs(shift)]
    return tpl

print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate((1, 2, 3, 4, 5, 6, 7), 2))

print()

print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate((1, 2, 3, 4, 5, 6, 7), -3))

print()

print(rotate((1, 2, 3, 4, 5, 6, 7), -10))

print()

print(rotate((1, 2, 3, 4, 5, 6, 7), 21))