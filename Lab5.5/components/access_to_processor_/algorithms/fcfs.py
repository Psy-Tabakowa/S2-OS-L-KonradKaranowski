from .algorithm import Algorithm


class FCFS(Algorithm):

    def execute(self):
        super().execute()
        # execute for each process
        for process in self.processes:
            # start process
            process.is_active = True
            # time for executing the process
            exec_time = process.time_left
            # subtract time_left by executing time
            process.time_left -= exec_time
            # update time
            self.update_time(exec_time)
            # print progress
            self.show_progress(process, exec_time)

    @classmethod
    def get_name(cls):
        return 'FCFS'
