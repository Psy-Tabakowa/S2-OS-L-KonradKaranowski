from typing import List


from algorithm import Algorithm
from request import Request


class SSTF(Algorithm):

    def execute(self) -> (List[int], int):
        current = self.rt_requests[0].block
        while True:
            # first execute real_time if they are
            if self.rt_requests:
                self.rt_requests = self.sort_by(self.rt_requests, current)
                current = self.rt_requests[0].block
                self.rt_requests = self.rt_requests[1:]
            # if no real time, execute normal
            elif self.requests:
                self.requests = self.sort_by(self.requests, current)
                current = self.requests[0].block
                self.requests = self.requests[1:]
            # after executing all processes break
            else:
                break
            self.rewound += self.calculate_rewound(current)
            self.queue.append(current)
        return self.queue, self.rewound

    def sort_by(self, requests: List, current: int) -> List[Request]:
        return sorted(requests, key=lambda request: abs(request.block - current))

    def get_name(self) -> str:
        return "SSTF Algorithm"
