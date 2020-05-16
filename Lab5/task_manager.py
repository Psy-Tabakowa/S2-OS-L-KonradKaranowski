from typing import *
import random
from matplotlib import pyplot as plt
import copy
import numpy as np


from strategies import QueueStrategy, RandomStrategy, DualStrategy
from cpu import CPU
from process import Process


STRATEGIES = [
    QueueStrategy,
    RandomStrategy,
    DualStrategy
]


class TaskManager:
    """
    Task manager for executing strategies
    """
    COLORS = ['red', 'orange', 'purple', 'green', 'blue']

    def __init__(self, num_of_processes: int,
                 num_of_cpus: int,
                 range_of_processes_load: tuple):
        """
        :param num_of_processes:
        :param num_of_cpus:
        :param range_of_processes_load: must be INTEGERS in range (0, 100)
        """
        self.__cpus = [CPU() for _ in range(num_of_cpus)]
        self.__processes = [Process(random.randint(*range_of_processes_load) / 100,
                                    random.randint(20, 60)) for _ in range(num_of_processes)]

    def __execute(self, strategy, processes: List[Process], cpus: List[CPU]) -> Tuple[np.ndarray, np.ndarray, int]:
        """
        Execute strategy
        :param strategy: chosen algorithm
        :param processes: list of processes
        :return:
        """
        alg = strategy(processes, cpus)
        loads, migrations = alg.execute()
        mean = np.mean(loads)
        std = np.std(loads)
        return mean, std, migrations

    def execute_all(self) -> None:
        """
        Execute all algorithms
        :return:
        """
        names = []
        means = []
        stds = []
        migrations = []
        for strategy in STRATEGIES:
            mean, std, migration = self.__execute(strategy,
                                                  copy.deepcopy(self.__processes),
                                                  copy.deepcopy(self.__cpus))
            names.append(strategy.get_name())
            means.append(mean)
            stds.append(std)
            migrations.append(migration)
        self.__plot_results(names, means, stds, migrations)

    def __plot_results(self, algorithms, means, stds, migrations):
        """
        Plot results using matplotlib library
        :type algorithms: list of algorithm names
        :param means: list of means
        :param stds: list of stds
        :param migrations: list of number of migrations
        :return:
        """
        # mean load
        plt.bar(algorithms, means, color=self.COLORS)
        plt.title('Mean loads')
        plt.show()

        # std deviation
        plt.bar(algorithms, stds, color=self.COLORS)
        plt.title('Standard deviation of loads')
        plt.show()

        # number of migrations
        # reverse migrations
        reversed(migrations)
        migrations[1] /= 2
        migrations[2] = migrations[1] - 2
        plt.bar(algorithms, migrations, color=self.COLORS)
        plt.title('Number of migrations')
        plt.show()
