import random


from algorithms.algorithm import Algorithm
from memory import Memory
from process import Process


class RAND(Algorithm):

    def execute(self) -> None:
        names = self.memory.get_names()
        references = self.process.get_references()
        for name, reference in zip(names, references[:len(names)]):
            self.memory.update_frame(name, reference)
        for reference in references[len(names):]:
            frame_name = random.choice(names)
            self.memory.update_frame(frame_name, reference)

    def get_name(self) -> str:
        return 'RAND algorithm'
