from _collections import deque


from components.page_replacement.algorithms.algorithm import Algorithm


class FIFO(Algorithm):

    def execute(self) -> None:
        names = deque(self.memory.get_names())
        for reference in self.process.get_references():
            frame_name = names[0]
            self.memory.update_frame(frame_name, reference)
            # rotate at the end of queue
            names.rotate(-1)

    def get_name(self) -> str:
        return 'FIFO'
