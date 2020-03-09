from collections import deque


from .algorithm import Algorithm


class RoundRobin(Algorithm):

    def __init__(self, processes):
        super().__init__(processes)
        # use deck collection for rotating
        self.processes = deque(self.processes)

    def execute(self, time_=10):
        """
        Executing process
        :param time_: quantum of time
        :return:
        """
        super().execute()
        while self.processes:
            process = self.processes[0]
            process.is_active = True
            # choose execute time
            if process.time_left < time_:
                exec_time = process.time_left
            else:
                exec_time = time_
            # execute process
            process.time_left -= exec_time
            self.update_time(exec_time)
            self.show_progress(process, exec_time)
            # finish process if no time left
            if process.time_left == 0:
                process.is_finished = False
                self.processes.remove(process)
            process.is_active = False
            self.processes.rotate(-1)


    @classmethod
    def get_name(cls):
        return 'RoundRobin'
