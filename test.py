# entries = []
# count = 0
# text = "Hello World"

# entries.append(f'{count}:{text}')
# print(entries)

## DECORATORS ##


from enum import Enum


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))


foo("Hi")


def test_decorator(func):
    def wrapped_func(x):
        func(x)
    return wrapped_func


@test_decorator
def foo_test(x):
    print('Hi ', str(x))


foo_test('Pritam')


def test_without_dec(func):
    def wrapped_func(x):
        func(x)
    return wrapped_func


def foo_test2(y):
    print('Hello ', y)


test = test_without_dec(foo_test2)
test('World !!')

######## ENUMS #################


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


for color in Color:
    print(f'{color.name} : {color.value}')


def Test():
    arr = [x for x in range(10, 16)]
    for i in arr:
        yield i


a = Test()
print(next(a))
print(next(a))
for i in a:
    print(i)
