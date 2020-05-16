from .algorithm import Algorithm


class SJF(Algorithm):

    def __init__(self, processes):
        super().__init__(processes)
        self.divide_to_batches()

    def execute(self):
        super().execute()
        while self.processes:
            # sorting items by time left
            self.processes = sorted(self.processes, key=lambda process: process.time_left)
            # choose process
            process = self.processes[0]
            process.is_active = True
            # remove process from processes list
            self.processes = self.processes[1:]
            # execute process
            exec_time = process.time_left
            process.time_left -= exec_time
            process.is_finished = True
            # update time
            self.update_time(exec_time)
            # print progress
            self.show_progress(process, exec_time)
            # add random process
            self.add_random()

    @classmethod
    def get_name(cls):
        return 'SJF_W'
