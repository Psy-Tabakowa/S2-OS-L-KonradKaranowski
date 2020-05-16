from _collections import deque


from components.page_replacement.algorithms.algorithm import Algorithm


class ALRU(Algorithm):

    def execute(self) -> None:
        names = self.setup_names()
        references = self.process.get_references()
        for name, reference in zip(names, references[:len(names)]):
            name.change_byte()
            self.memory.update_frame(name.name, reference)
        frame_name = names[0]
        for reference in references[len(names):]:
            self.memory.update_frame(frame_name.name, reference)
            # rotate at the end of queue
            names.rotate(-1)
            for _ in range(len(names)):
                if names[0].byte:
                    frame_name = names[0]
                    frame_name.change_byte()
                    break
                else:
                    names[0].change_byte()
                    names.rotate(-1)

    def get_name(self) -> str:
        return 'ALRU'

    def setup_names(self):
        names = [Name(name=name) for name in self.memory.get_names()]
        return deque(names)


class Name:

    def __init__(self, name: str):
        self.name = name
        self.byte = False

    def get_name(self):
        return self.name

    def get_byte(self):
        return self.byte

    def change_byte(self):
        if self.byte:
            self.byte = False
        else:
            self.byte = True

    def __repr__(self):
        return f'Name object: {self.name}, byte: {self.byte}'
