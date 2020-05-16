from typing import List

from components.access_to_disk_.algorithms.algorithm import Algorithm


class Scan(Algorithm):

    def __init__(self, requests, blocks, side='left'):
        super().__init__(requests, blocks)
        self.side = side

    def execute(self) -> (List[int], int):
        current = self.rt_requests[0].block
        while True:
            # first execute real_time if they are
            if self.rt_requests:
                current = self.rt_requests[0].block
                self.rt_requests = self.rt_requests[1:]
                self.rewound += self.calculate_rewound(current)
                self.queue.append(current)
            # if no real time, execute normal
            elif self.requests:
                right, left = self.sort_right_left(current)
                if self.side == 'left':
                    self.play_sorted(left, right)
                elif self.side == 'right':
                    self.play_sorted(right, left)
                break
            # after executing all processes break
            else:
                break
        return self.queue, self.rewound

    def change_side(self) -> str:
        if self.side == 'right':
            return 'left'
        else:
            return 'right'

    def get_name(self) -> str:
        return "Scan"

    def sort_right_left(self, current) -> (List, List):
        """
        Sort right_left by current element
        :param current: current cylinder
        :return:
        """
        right = [r for r in self.requests if r.block >= current]
        left = [r for r in self.requests if r.block < current]
        right = sorted(right, key=lambda request: request.block)
        left = sorted(left, key=lambda request: request.block)
        return right, left

    def play_sorted(self, first, second) -> None:
        """
        Do job for sorted first and second
        :param first:
        :param second:
        :return:
        """
        for l in reversed(first):
            l = l.block
            self.rewound += self.calculate_rewound(l)
            self.queue.append(l)
        for r in second:
            r = r.block
            self.rewound += self.calculate_rewound(r)
            self.queue.append(r)