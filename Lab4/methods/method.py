import abc
from typing import *


class Method(abc.ABC):

    def __init__(self, pages: int, processes):
        self.pages = pages
        self.processes = processes

    @abc.abstractmethod
    def get_name(self) -> str: pass

    @abc.abstractmethod
    def execute(self) -> List[int]: pass
