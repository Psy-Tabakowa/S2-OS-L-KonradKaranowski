from typing import List


from algorithm import Scan


class CScan(Scan):

    def execute(self) -> (List[int], int):
        return super().execute()

    def get_name(self) -> str:
        return "C-Scan Algorithm"

    def play_sorted(self, first, second) -> None:
        """
        Both are reversed!
        :param first: first part
        :param second: second part
        :return:
        """
        for l in reversed(first):
            l = l.block
            self.rewound += self.calculate_rewound(l)
            self.queue.append(l)
        for r in reversed(second):
            r = r.block
            self.rewound += self.calculate_rewound(r)
            self.queue.append(r)
