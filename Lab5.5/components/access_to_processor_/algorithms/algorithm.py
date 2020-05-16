import abc
import random


class Algorithm(abc.ABC):
    """
    Abstract class of algorithm
    """

    def __init__(self, processes):
        self.processes = processes
        self.times_to_wait = []
        self.num_of_processes = len(processes)
        self.total_time = 0

    @abc.abstractmethod
    def execute(self): pass

    @abc.abstractmethod
    def get_name(self): pass

    def divide_to_batches(self, batch_size=None) -> None:
        """
        Create batches
        :param batch_size: size of additional process batch
        :return:
        """
        if not batch_size:
            batch_size = round(len(self.processes) / 2)
        # divide to two batches
        self.additional_processes = self.processes[batch_size:]
        self.processes = self.processes[:batch_size]
        # shuffle additional processes
        random.shuffle(self.additional_processes)

    def add_random(self) -> None:
        """
        Add new process if possible
        :return:
        """
        try:
            self.processes.append(self.additional_processes[0])
            self.additional_processes = self.additional_processes[1:]
        except:
            pass

    def update_time(self, execute_time) -> None:
        """
        Update time_to_wait for all not active and not finished processes
        :param execute_time: time of executing the process
        :return:
        """
        self.total_time += execute_time
        for process in self.processes:
            if not process.is_finished and not process.is_active:
                # update list of times
                self.times_to_wait.append(execute_time)

    def show_progress(self, active_process, exec_time) -> None:
        """
        Shows progress during the executing the process
        :param active_process: active process to show
        :param exec_time: time of executing the process
        :return:
        """
        pass

    def summary(self) -> float:
        """
        Show summary
        :return: mean time
        """
        mean_time = sum(self.times_to_wait)\
                    / self.num_of_processes
        return mean_time
