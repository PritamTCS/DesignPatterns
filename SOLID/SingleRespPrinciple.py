# Journal's primary responsiblity is to record entries
# So persistence(saving to a file) can be taken out to a separate class
## This is called Single Responsibililty Principle ##


class Journal(object):
    def __init__(self):
        self.count = 0
        self.entries = []

    def add_entry(self, text):
        # self.entries.append(f'{self.count}:{text}')
        self.entries.append('{}:{}'.format(self.count, text))
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistenceManager(object):
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('Hello India')
j.add_entry('Good Morning!!')
# print('Journal entries: \n{}'.format(j))
# print(f'Journal entries: \n{j}')

file = r'/home/pritam/Desktop/designPatterns/SOLID/text'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
