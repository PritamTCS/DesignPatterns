class Computer(object):
    # def __init__(self, case, mainboard, cpu, memory, hard_drive):
    #     self.case = case
    #     self.mainboard = mainboard
    #     self.cpu = cpu
    #     self.memory = memory
    #     self.hard_drive = hard_drive

    def display(self):
        print('Custom Computer: ')
        print('\nCase: {}'.format(self.case))
        print('Mainboard: {}'.format(self.mainboard))
        print('CPU: {}'.format(self.cpu))
        print('Memory: {}'.format(self.memory))
        print('Hard_drive: {}'.format(self.hard_drive))
