from .method import Method
from typing import *
import random
import numpy as np


class DumbMethod(Method):

    def execute(self) -> List[int]:
        delta = 5
        theta = 5
        per_process = int(self.pages / len(self.processes))
        pages = [per_process for _ in range(len(self.processes))]
        #for i, page in enumerate(pages):
        #    if random.randint(0, 1) == 1:
        #        pages += self.processes[i].frames / delta - theta * np.log(len(self.processes))
        return [int(page) for page in pages]

    def get_name(self) -> str:
        return 'SSCBS'
