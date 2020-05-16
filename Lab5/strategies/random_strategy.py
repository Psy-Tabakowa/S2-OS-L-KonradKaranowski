import random
from typing import *


from strategies.strategy import Strategy
from config import Config


class RandomStrategy(Strategy):

    def assign_process(self, process) -> Tuple[bool, int]:
        print(process.load)
        steps = 0
        for _ in range(len(self.cpus)):
            cpu = random.choice(self.cpus)
            if cpu.cpu_load + process.load <= Config.SECOND_VALUE_P:
                steps += 1
                cpu.add_process(process)
                break
        else:
            return self.second_chance(process, steps)
        return True, steps

    @staticmethod
    def get_name() -> str:
        return 'Random strategy'
