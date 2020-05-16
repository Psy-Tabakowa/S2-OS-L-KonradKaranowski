import abc
from typing import List


from components.access_to_disk_.request import Request


class Algorithm(abc.ABC):
    """
    Abstract algorithm class
    """

    def __init__(self, requests, blocks):
        self.requests, self.rt_requests = self.create_batches(requests)
        self.queue = []
        self.rewound = 0
        self.blocks = max(blocks)

    @abc.abstractmethod
    def execute(self) -> (List[int], int): pass

    @abc.abstractmethod
    def get_name(self) -> str: pass

    def calculate_rewound(self, current) -> int:
        """
        Calculate how much to rewind
        :param current:
        :return:
        """
        try:
            return abs(self.queue[-1] - current)
        except IndexError:
            return 0

    def create_batches(self, requests: List[Request]) -> (List[Request], List[Request]):
        """
        Create list of processes and real-time applications
        :param requests: requests
        :return: normal requests, real-time requests
        """
        n_requests = requests[5:]
        real_time = requests[:5]
        return n_requests, real_time
