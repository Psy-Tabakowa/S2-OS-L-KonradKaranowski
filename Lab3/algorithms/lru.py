from typing import List
from _collections import deque


from algorithms.algorithm import Algorithm
from process import Process
from memory import Memory


class LRU(Algorithm):

    def execute(self) -> None:
        recently_used = list()
        names = deque(self.memory.get_names())
        references = self.process.get_references()
        for name, reference in zip(names, references[:len(names)]):
            self.memory.update_frame(name, reference)
            recently_used.append(name)
        for reference in references[len(names):]:
            if self.memory.is_in_memory(reference):
                name = self.get_name_optional(reference, self.memory)
            else:
                name = self.get_optimal(recently_used, names)
            self.memory.update_frame(name, reference)
            recently_used.append(name)

    def get_optimal(self, recently_used_reversed: List[str], names: List[str]) -> str:
        values = list()
        for name in names:
            i = 0
            for rec in reversed(recently_used_reversed):
                if rec == name:
                    apd = (name, i)
                    values.append(apd)
                    break
                i += 1
        values.sort(key=lambda s: s[1])
        return values[-1][0]

    def get_name_optional(self, reference: int, memory: Memory) -> str:
        return memory.get_by_reference(reference)

    def get_name(self) -> str:
        return 'LRU algorithm'
