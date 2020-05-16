import abc
from typing import List, Dict, Tuple
from components.page_replacement.process import Process


from components.page_replacement.memory import Memory


class Algorithm(abc.ABC):

    def __init__(self, num_of_frames: int, process: Process):
        self.memory = Memory(num_of_frames)
        self.process = process

    @abc.abstractmethod
    def execute(self) -> None: pass

    @abc.abstractmethod
    def get_name(self) -> str: pass

    def get_deficiencies(self) -> List[Tuple[str, int]]:
        """
        Return list of deficiencies
        :return:
        """
        return self.memory.get_deficiencies()

    def get_history(self) -> Dict[str, List[int]]:
        """
        Returns history of frame changes
        :return:
        """
        return self.memory.get_history()