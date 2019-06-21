# entries = []
# count = 0
# text = "Hello World"

# entries.append(f'{count}:{text}')
# print(entries)

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


for color in Color:
    print(color.value)
