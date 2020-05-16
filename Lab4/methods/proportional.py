from methods import Method
from typing import *


class ProportionalAllocateMethod(Method):

    def execute(self) -> List[int]:
        sum_vm = sum([p.frames for p in self.processes])
        pages = [int(round(self.pages * p.frames / sum_vm, 0)) for p in self.processes]
        if sum(pages) == self.pages + 1:
            pages[0] += 1
        elif sum(pages) == self.pages - 1:
            pages[0] -= 1
        return pages

    def get_name(self) -> str:
        return 'Proportional'
