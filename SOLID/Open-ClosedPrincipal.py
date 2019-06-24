from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product(object):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter(object):
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, color, size):
        for p in products:
            if p.size == size and p.color == color:
                yield p


# Enterprise Patterns: Specification

class Specification(object):
    def is_satisfied(self, item):
        pass


class Filter(object):
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print('Green products: (Old way): ')
for p in pf.filter_by_color(products, Color.GREEN):
    # print(f'{p.name} - is Green ')
    print('{} - is Green'.format(p.name))

bf = BetterFilter()
green = ColorSpecification(Color.GREEN)
print('\nGreen products (new): ')
for p in bf.filter(products, green):
    print(f'{p.name} - is Green')
