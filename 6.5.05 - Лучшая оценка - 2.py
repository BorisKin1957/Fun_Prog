def get_info_marks(students, *args):
    result = dict(zip(students, map(lambda x: (max(x), min(x)), zip(*args))))
    return {key: {'best': value[0], 'worst': value[1]} for key, value in result.items()}


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
