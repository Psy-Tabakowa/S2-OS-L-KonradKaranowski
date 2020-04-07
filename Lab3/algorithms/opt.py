from typing import List


from algorithms.algorithm import Algorithm
from process import Process
from memory import Memory


class OPT(Algorithm):

    def execute(self) -> None:
        names = self.memory.get_names()
        references = self.process.get_references()
        for name, reference in zip(names, references[:len(names)]):
            self.memory.update_frame(name, reference)
        for i, reference in enumerate(references[len(names):], len(names) + 1):
            name = self.calculate_optimal(self.memory, references, names, i)
            self.memory.update_frame(name, reference)

    def calculate_optimal(self, memory: Memory, references: List[int],
                          names: List[str], cursor: int) -> str:
        values = []
        # for each frame
        for name in names:
            value = memory.get_value(name, cursor - 2)
            for i, ref in enumerate(references[cursor - 1:], cursor):
                if ref == value:
                    adb = (name, i - cursor)
                    values.append(adb)
                    break
            else:
                adb = (name, len(references[cursor:]) + 1)
                values.append(adb)
        values.sort(key=lambda s: s[1], reverse=True)
        return values[0][0]

    def get_name(self) -> str:
        return 'OPT algorithm'
