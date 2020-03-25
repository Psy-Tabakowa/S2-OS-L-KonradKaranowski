from typing import List
import copy
import numpy as np
from matplotlib import pyplot as plt

from request import Request
from algorithm import Algorithm


class Disk:
    """
    Class representing disk
    """

    def __init__(self, blocks: int):
        self.blocks = list(range(1, blocks + 1))

    def setup_requests(self, num_of_requests: int) -> None:
        """
        Create list of requests
        :param num_of_requests number of requests
        :return:
        """
        blocks = np.random.permutation(self.blocks)
        self.requests = [Request(blocks[i]) for i in range(num_of_requests)]

    def __execute(self, algorithm: Algorithm, requests: List[Request]) -> (List[int], int, str):
        """
        Execute algorithm
        :param algorithm: class of algorithm (must inherit 
        :param requests: list of requests
        :return:
        """
        alg = algorithm(requests, self.blocks)
        queue, cylinders = alg.execute()
        name = alg.get_name()
        return list(reversed(queue)), cylinders, name

    def __get_requests_copy(self) -> [Request]:
        """
        Create copy of requests list
        :return: copy list of requests
        """
        return copy.deepcopy(self.requests)

    def execute_all(self, algorithms: List):
        """
        Execute all algorithms
        :param algorithms:
        :return:
        """
        queues = []
        all_cylinders = []
        names = []
        for algorithm in algorithms:
            requests = self.__get_requests_copy()
            queue, cylinders, name = self.__execute(algorithm, requests)
            queues.append(queue)
            all_cylinders.append(cylinders)
            names.append(name)
        self.__plot_all(queues, all_cylinders, names)

    def __plot_all(self, queues, totals, algorithms) -> None:
        """
        Make all plots to compare algorithm
        :param queues: list of queues
        :param totals: list of totals
        :param algorithms: list of algorithms
        :return:
        """
        colors = ['red', 'blue', 'purple', 'green']
        # iterators
        queues = iter(queues)
        totals = iter(totals)
        algorithms = iter(algorithms)
        colors = iter(colors)
        # creating subplots
        fig, ax = plt.subplots(2, 2)
        for i in range(2):
            for j in range(2):
                try:
                    self.__plot_picture(ax, i, j,
                                        next(queues),
                                        next(totals),
                                        next(algorithms),
                                        next(colors))
                except StopIteration:
                    pass
        plt.show()

    def __plot_picture(self, ax, i: int, j: int, queue: List[int],
                       total_cylinders: int, algorithm: str, color: str) -> None:
        """
        Plots visualisation of disk management
        :param ax: axis of subplot
        :param i: i of ax
        :param j: j of ax
        :param queue: queue of blocks that are used currently
        :param total_cylinders: total cylinders rewound
        :param algorithm: name of algorithm
        :param color: color of plot
        :return:
        """
        x = list(range(1, self.blocks[-1] + 1))
        ax[i, j].set_title(f'{algorithm}, total rewound: {total_cylinders}')
        ax[i, j].plot(queue, x, marker='x', color=color)
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
