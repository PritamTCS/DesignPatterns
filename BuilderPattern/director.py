class Director(object):
    def __init__(self, builder):
        self._builder = builder

    def build_computer(self):
        self._builder.new_computer(self)
        self._builder.get_case(self)
        self._builder.build_mainboard(self)
        self._builder.install_mainboard(self)
        self._builder.install_hard_drive(self)

    def get_computer(self):
        return self._builder.get_computer(self)
