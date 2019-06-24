################# Liskov Substitution Principle #################################

#   You should always be able to substitute a parent class with its derived class
#   without any undesirable behaviour.
#  
#   if S is a subtype of T, then objects of type T in a program may be replaced 
#   with objects of type S without altering any of the desirable properties of that program.
#   Practically, the derived class should always extend its parent class, 
#   without changing its behaviour at all.

#################################################################################


class Rectangle(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def __str__(self):
        return 'Width: {}, height: {}'.format(self._width, self._height)

    @property
    def area(self):
        return self._height * self._width

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    got = rc.area
    print('Expected area: {}, got area: {}'.format(expected, got))

rc = Rectangle(10, 12)
print(rc)
use_it(rc)

print('\n')

sq = Square(5)
use_it(sq)

