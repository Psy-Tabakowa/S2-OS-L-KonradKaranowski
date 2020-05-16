from methods import Method
from typing import *


class EqualAllocationMethod(Method):

    def execute(self) -> List[int]:
        per_process = int(self.pages / len(self.processes))
        return [per_process for _ in range(len(self.processes))]

    @staticmethod
    def get_name(self) -> str:
        return 'Equal'
