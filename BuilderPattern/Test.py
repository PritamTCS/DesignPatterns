from director import Director
from ConcreteClass import MyComputerBuilderConcrete

if __name__ == "__main__":
    computer_builder = Director(MyComputerBuilderConcrete)
    computer_builder.build_computer()
    computer = computer_builder.get_computer()
    computer.display()
