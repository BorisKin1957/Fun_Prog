def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


print(flatten_dict({"a": 1,
                    "b": {
                        "c": 2,
                        "d": 3,
                        "e": {
                            "f": 4,
                            '6': 100,
                            '5': {"g": 6},
                            "l": 1,
                        }
                    }}))