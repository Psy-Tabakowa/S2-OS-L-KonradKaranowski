from .method import Method
from typing import *


import numpy as np


class SphereAllocationMethod(Method):

    def execute(self) -> List[int]:
        # approximated
        workspace = self.pages // 4
        self.pages -= workspace
        sum_vm = sum([p.frames for p in self.processes])
        pages = [int(round(self.pages * p.frames / sum_vm, 0) + workspace / len(self.processes) * 4 * np.log10(4))
                 for p in self.processes]
        return pages

    def get_name(self) -> str:
        return 'Sphere'
