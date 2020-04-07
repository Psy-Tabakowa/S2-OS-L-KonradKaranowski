from _collections import deque


from algorithms.algorithm import Algorithm
from process import Process
from memory import Memory


class FIFO(Algorithm):

    def execute(self) -> None:
        names = deque(self.memory.get_names())
        for reference in self.process.get_references():
            frame_name = names[0]
            self.memory.update_frame(frame_name, reference)
            # rotate at the end of queue
            names.rotate(-1)


    def get_name(self) -> str:
        return 'FIFO algorithm'
