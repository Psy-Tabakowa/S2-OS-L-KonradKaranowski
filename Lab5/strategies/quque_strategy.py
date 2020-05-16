from typing import *


from strategies.strategy import Strategy
from config import Config


class QueueStrategy(Strategy):

    def assign_process(self, process) -> Tuple[bool, int]:
        steps = 0
        for cpu in self.cpus:
            load = cpu.cpu_load
            if load + process.load <= Config.FIRST_VALUE_P:
                steps += 1
                cpu.add_process(process)
                break
        else:
            return self.second_chance(process, steps)
        return True, steps

    @staticmethod
    def get_name() -> str:
        return 'Queue algorithm'
