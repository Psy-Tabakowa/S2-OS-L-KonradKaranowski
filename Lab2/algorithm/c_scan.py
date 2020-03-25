from typing import List


from algorithm import Scan


class CScan(Scan):

    def execute(self) -> (List[int], int):
        return super().execute()

    def get_name(self) -> str:
        return "C-Scan Algorithm"

    def play_sorted(self, first, second) -> None:
        super().play_sorted(first, reversed(second))
