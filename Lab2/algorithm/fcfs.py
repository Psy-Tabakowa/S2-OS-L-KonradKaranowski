from typing import List


from algorithm import Algorithm


class FCFS(Algorithm):

    def execute(self) -> (List[int], int):
        """
        Execute FCFS Algorithm
        :return: queue, rewound cylinders
        """
        while True:
            # first execute real_time if they are
            if self.rt_requests:
                to_queue = self.rt_requests[0].block
                self.rt_requests = self.rt_requests[1:]
            # if no real time, execute normal
            elif self.requests:
                to_queue = self.requests[0].block
                self.requests = self.requests[1:]
            # after executing all processes break
            else:
                break
            self.rewound += self.calculate_rewound(to_queue)
            self.queue.append(to_queue)
        return self.queue, self.rewound

    def get_name(self) -> str:
        return "FCFS Algorithm"
