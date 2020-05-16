import random
from typing import *
import copy
from matplotlib import pyplot as plt


from process import Process
from memory import LRU


class ExecutionManager:

    def __init__(self, num_of_pages: int):
        self.num_of_pages = num_of_pages

    @staticmethod
    def setup_processes(num_of_processes: int,
                        len_of_processes: int,
                        min_frames: int,
                        max_frames: int) -> List[Process]:
        """
        Setup list of processes
        :param num_of_processes: number of processes in simulation
        :param len_of_processes: length of processes
        :param min_frames: min number of frames for process
        :param max_frames: max number of frames for process
        :return: list of processes
        """
        processes = []
        for _ in range(num_of_processes):
            frames = random.randint(min_frames, max_frames)
            process = Process(len_of_processes, frames)
            processes.append(process)
        return processes

    def execute_all(self, methods, processes: List[Process], plot=True):
        history = []
        names = []
        for Method in methods:
            names.append(Method.get_name(Method))
            alg_history = self.__execute(Method, copy.deepcopy(processes))
            history.append(alg_history)
        if not plot:
            return [sum(series) for series in history]
        self.__plot_results(history, names)

    def __execute(self, Method, processes: List[Process]):
        algorithm_history = []
        pages = self.__calculate_frames(Method, processes)
        for process, page in zip(processes, pages):
            a = LRU(page, process)
            a.execute()
            algorithm_history.append(a.get_deficiencies())
        return algorithm_history

    def __calculate_frames(self, Method, processes):
        method = Method(self.num_of_pages, processes)
        return method.execute()

    def __plot_results(self, history, names):
        for i, (series, name) in enumerate(zip(history, names)):
            global_val = sum(series)
            self.__plot_series(series, global_val, name)

    def __plot_series(self, series, global_val, name):
        plt.title(name)
        names = [f'p{i + 1}:{series[i]}' for i in range(len(series))] + [f'total:{global_val}']
        series += [global_val]
        plt.xticks(rotation='vertical')
        plt.bar(names, series)
        plt.show()

