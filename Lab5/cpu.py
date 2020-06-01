from process import Process


from typing import *


class CPU:
    """
    Class representing single core in multi-core computer

    Parameters:
    :param self.__cpu_load: total cpu load, at the beginning 0
    """

    def __init__(self):
        self.__processes = []
        self.__cpu_load = 0

    @property
    def cpu_load(self) -> float:
        return self.__cpu_load

    def add_process(self, process):
        self.__processes.append(process)

    def __calculate_load(self):
        self.__cpu_load = sum([process.load for process in self.__processes])

    def __remove_finished_processes(self):
        for process in self.__processes:
            if process.is_finished:
                self.__processes.remove(process)

    def update_processes(self):
        for process in self.__processes:
            process.tick()
        self.__remove_finished_processes()
        self.__calculate_load()
        return self.__cpu_load

    def __repr__(self):
        return f'Cpu with load: {self.cpu_load}'
