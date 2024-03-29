##### Dependency Inversion Principle ####
#     High Level modules should not depend on Low level ones, use abstractions
######################################################

from enum import Enum
from abc import abstractmethod, ABC


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # Low level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

    # def __str__(self):
    #     return ''.join(self.relations)


class Research:  # High level module
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

# print(relationships)


Research(relationships)


#####################################################

class Manager(object):
    def __init__(self):
        self.developers = []
        self.testers = []
        self.designers = []

    def addDevelopers(self, dev):
        self.developers.append(dev)

    def addDesigners(self, designer):
        self.designers.append(designer)

    def addTester(self, tester):
        self.testers.append(tester)


class Developer(object):
    def __init__(self):
        print("Developer added")


class Designer(object):
    def __init__(self):
        print("Designer added")


class Tester(object):
    def __init__(self):
        print("Tester added")


if __name__ == "__main__":
    obj = Manager()
    obj.addDevelopers(Developer())
    obj.addDesigners(Designer())
    obj.addTester(Tester())


#################### Using Abstraction #######################

class Employee(object):
    def work(self):
        pass


class Manager1(object):
    def __init__(self):
        self.employees = []

    def addEmp(self, emp):
        self.employees.append(emp)


class Developer1(Employee):
    def __init__(self):
        print("Developer added")


class Designer1(Employee):
    def __init__(self):
        print("Designer added")


class Tester1(Employee):
    def __init__(self):
        print("Tester added")


objM = Manager1()
objM.addEmp(Developer1())
objM.addEmp(Designer1())
objM.addEmp(Tester1())
