import abc
import random
from typing import *


class Strategy(abc.ABC):

    def __init__(self, processes, cpus):
        self.processes = processes
        self.cpus = cpus

    def execute(self):
        """
        Execute algorithm
        :return:
        """
        loads = []
        migrations = 0
        processes_active = True
        while self.processes or processes_active:
            if self.processes and random.choice([True, False]):
                process = self.processes[0]
                was_able_to_assign, migration = self.assign_process(process)
                if was_able_to_assign:
                    migrations += migration
                    self.processes = self.processes[1:]
            load, processes_active = self.__update_cpus()
            loads.append(load)
            print(self.cpus)
        return loads, migrations

    @abc.abstractmethod
    def assign_process(self, process): pass

    def second_chance(self, process, steps) -> Tuple[bool, int]:
        """
        Second chance to assign process
        :param process: process
        :param steps: number of steps
        :return:
        """
        new_steps = 0
        for cpu in self.cpus:
            new_steps += 1
            load = cpu.cpu_load
            if load + process.load <= 1:
                cpu.add_process(process)
                return True,  steps + new_steps
        print("Couldn't assign process")
        return False, 0

    def __update_cpus(self):
        """
        Update cpu
        :return:
        """
        load = 0
        processes_active = True
        for cpu in self.cpus:
            load += cpu.update_processes()
        if load == 0:
            processes_active = False
        return load, processes_active

    @abc.abstractmethod
    def get_name(self) -> str: pass
