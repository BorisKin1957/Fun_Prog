def is_table_free(number: int) -> bool:
    global tables
    return  not tables[number]


def get_free_tables():
    return [key for key in tables.keys() if not tables[key]]

tables = {
  1: 'Andrey',
  2: None,
  3: None,
  4: None,
  5: 'Vasiliy',
  6: None,
  7: None,
  8: 'Stas',
  9: None,
}

print(get_free_tables())
print(is_table_free(1))
print(is_table_free(2))
