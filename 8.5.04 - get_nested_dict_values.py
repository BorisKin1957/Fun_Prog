def get_nested_dict_values(lib):
    for key, value in lib.items():
        if isinstance(value, dict):
            yield from get_nested_dict_values(value)
        else:
            yield value
            
data = {
    "name": "Alice",
    "info": {
        "age": 25,
        "skills": ["Python", "Data Analysis"],
        "details": {
            "hobbies": ["reading", "gaming"],
            "city": "London"
        }
    }
}

for value in get_nested_dict_values(data):
    print(value)

data = {
    "Иванов": {"математика": 85, "физика": 90},
    "Сидорова": {"математика": 92, "химия": 88},
    "Гиппиус": {"Литература": 78, "поэзия": 80}
}
for value in get_nested_dict_values(data):
    print(value)