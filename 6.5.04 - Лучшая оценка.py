def get_info_marks(students: list[str], *args: list[list[int]]) -> dict[str, int]:
    '''лучшую оценку для каждого студента и составить из этих данных словарь, где ключ - имя студента, значение - лучшая оценка.'''
    return dict(zip(students, map(max, zip(*args))))


math = [90, 76, 94]
history = [78, 79, 90]
students = ["Marie", "Michael", "Marge"]

print(get_info_marks(students, math, history))

math = [90, 76, 94]
history = [78, 79, 90]
geography = [95, 80, 92]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, geography, history))

math = [90, 76, 94]
history = [78, 79, 90]
geography = [95, 80, 92]
music = [93, 98, 100]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, geography, history, music))