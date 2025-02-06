def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    return int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)


def convert_to_rgb(values: list[str]) -> list[tuple[int, int, int]]:
    return list(map(lambda x: (int(x[1:3], 16), int(x[3:5], 16), int(x[5:], 16)), colors))

print(from_hex_to_rgb('#B22222'))
print(from_hex_to_rgb('#FFFFFF'))
print(from_hex_to_rgb('#000000'))
print(from_hex_to_rgb('#87CEEB'))
print(from_hex_to_rgb('#191970'))

print()

colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50']
print(convert_to_rgb(colors))