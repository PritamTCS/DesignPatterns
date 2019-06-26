from abs_builder import AbstractBuilder


class MyComputerBuilderConcrete(AbstractBuilder):
    def get_case(self):
        self._computer.case = 'CoolerMaster N300'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core - i7 4770'
        self._computer.memory = 'Vengeance 16GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate 2TB'
