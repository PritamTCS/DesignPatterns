from abc import ABC, abstractmethod


class Test(ABC):
    @abstractmethod
    def print_in(self):
        print('Inside print_in')

    @abstractmethod
    def print_out(self):
        print('Inside print_out')


class Implement(Test):
    def print_in(self):
        print('Inside Implement print_in')

    def print_out(self):
        print('Inside Implement print out')


obj = Implement()
# obj = Test()
obj.print_in()
obj.print_out()
