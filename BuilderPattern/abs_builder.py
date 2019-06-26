from abc import ABC, abstractmethod
from Computer import Computer


class AbstractBuilder(ABC):
    def new_computer(self):
        self._computer = Computer()

    def get_computer(self):
        return self._computer

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass
