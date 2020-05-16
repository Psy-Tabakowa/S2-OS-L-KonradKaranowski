import random


class Process:

    def __init__(self, num, phase_len_range):
        self.num = num
        self.time_left = random.randint(*phase_len_range)
        self.is_active = False
        self.time_to_wait = 0
        self.is_finished = False

    def execute(self, exec_time):
        self.time_left -= exec_time
        if not self.time_left:
            self.is_finished = True
        return self.is_finished

    def get_time_to_wait(self):
        return self.time_to_wait

    def __repr__(self):
        return str(self.time_left)
