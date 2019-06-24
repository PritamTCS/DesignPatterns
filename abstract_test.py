from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def print_in(self):
        print('Inside print_in')

    
    def print_out(self):
        print('Inside print_out')

class Implement(Test):
    pass
    # def print_in(self):
    #     print('Inside Implement print_in')
    
obj = Implement()


obj.print_in()
obj.print_out()