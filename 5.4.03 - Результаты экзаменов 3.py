def print_results(volumes):
    for i in sorted(volumes, key=lambda x: (-x[1], x[0].lower())):
        print(i[0], i[1])


marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]

print_results(marks)

marks = [('English', 88), ('Science', 90), ('Maths', 88),
         ('Physics', 93), ('History', 78), ('French', 78),
         ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
print_results(marks)

print()

marks = [('english', 100), ('Science', 100), ('maths', 100),
         ('Physics', 100), ('history', 100), ('Music', 100)]
print_results(marks)