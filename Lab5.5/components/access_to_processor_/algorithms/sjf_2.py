from .algorithm import Algorithm


class SJF2(Algorithm):

    def __init__(self, processes):
        super().__init__(processes)
        self.divide_to_batches()

    def execute(self):
        while self.processes:
            # sorting items by time left
            self.processes = sorted(self.processes, key=lambda process: process.time_left)
            # choose process
            process = self.processes[0]
            process.is_active = True
            # execute process
            exec_time = 1
            process.time_left -= exec_time
            if process.time_left == 0:
                process.is_finished = True
                # remove process from processes list
                self.processes = self.processes[1:]
            # update time
            self.update_time(exec_time)
            # deactivate
            process.is_active = False
            # print progress
            # self.show_progress(process, exec_time)
            # add random process
            if self.total_time % 5 == 0:
                self.add_random()

    @classmethod
    def get_name(cls):
        return 'SJF'
