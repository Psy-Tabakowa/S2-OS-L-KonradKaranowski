import random
import copy
from typing import *


from strategies.strategy import Strategy
from config import Config


class DualStrategy(Strategy):

    def assign_process(self, process) -> Tuple[bool, int]:
        process_1 = copy.deepcopy(process)
        process_2 = copy.deepcopy(process)
        load = process.load
        process_1.load = load * Config.PROPORTION
        process_2.load = load - process_1.load
        steps = 0
        for _ in range(len(self.cpus)):
            steps += 1
            cpu = random.choice(self.cpus)
            if cpu.cpu_load + process_1.load <= Config.THIRD_VALUE_R:
                cpu.add_process(process_1)
                for _ in range(len(self.cpus)):
                    cpu_2 = random.choice(self.cpus)
                    if cpu_2.cpu_load + process_2.load <= Config.THIRD_VALUE_R:
                        cpu_2.add_process(process_2)
                        break
        else:
            return self.second_chance(process_2, steps)
        return True, steps

    @staticmethod
    def get_name() -> str:
        return 'Dual algorithm'
