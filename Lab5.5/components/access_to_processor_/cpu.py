import copy
from typing import *


from components.access_to_processor_.process import Process


class CPU:

    def init_processes(self, num_of_processes, phase_len_range=(5, 20)):
        """
        Initialize processes
        :param num_of_processes: number of processes
        :param phase_len_range: range of phase length
        :return:
        """
        self.processes = [
            Process(num=i, phase_len_range=phase_len_range) for i in range(num_of_processes)
        ]

    def __execute(self, algorithm, processes) -> float:
        """
        Execute specified algorithm
        :param algorithm: class
        :param processes: list of processes
        :return:
        """
        algorithm = algorithm(processes)
        algorithm.execute()
        mean_time = algorithm.summary()
        return mean_time

    def execute_all(self, algorithms):
        """
        Execute all algorithms
        :param algorithms: list of classes
        :return:
        """
        names = []
        times = []
        for Algorithm in algorithms:
            name = Algorithm.get_name()
            time = self.__execute(Algorithm, self.return_copy())
            names.append(name)
            times.append(time)
        return names, times

    def return_copy(self) -> [Process]:
        """
        Create copy of list of processes
        :return: list of processes
        """
        new_list = copy.deepcopy(self.processes)
        return new_list

