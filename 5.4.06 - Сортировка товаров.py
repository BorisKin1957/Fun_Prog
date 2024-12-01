def print_goods(models_list):
    result = sorted(models_list, key=lambda x: (list(x.items())[2][1].lower(), -list(x.items())[1][1]))
    for item in result:
        print(f"Производитель: {item['make']}, модель: {item['model']}, цвет: {item['color']}")


models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]
print_goods(models)

print()

models = [{'make': 'Nokia', 'model': 2, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 3, 'color': 'red'},
          {'make': 'Samsung', 'model': 5, 'color': 'Yellow'},
          {'make': 'Apple', 'model': 10, 'color': 'RED'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'BLACK'},
          {'make': 'Honor', 'model': 3, 'color': 'black'},
          {'make': 'Nothing Phone', 'model': 7, 'color': 'Yellow'}]
print_goods(models)