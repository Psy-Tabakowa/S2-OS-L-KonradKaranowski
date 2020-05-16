from typing import List
import random


import numpy as np


class Process:

    def __init__(self, num_of_references: int, num_of_pages: int):
        self.__references = self.__create_requests_string(num_of_references, num_of_pages)
        self.__max_frames = num_of_pages

    def __create_requests_string(self, num_of_references: int, num_of_pages: int) -> List[int]:
        """
        Create list of references to pages
        :param num_of_references: length of array of references
        :param num_of_pages: number of pages in physical memory
        :return:
        """
        # list of pages as random permutation
        # else remove random permutation
        pages_enum = list(np.random.permutation([i + 1 for i in range(num_of_pages)]))
        # first n references must be list of pages in order
        references = pages_enum
        if num_of_pages < num_of_references:
            for i in range(num_of_references - num_of_pages):
                while True:
                    # random reference cannot be the same as previous (that's pointless)
                    random_reference = random.randint(1, num_of_pages)
                    if random_reference != references[num_of_pages + i - 1]:
                        references.append(random_reference)
                        break
        return references[:num_of_references]

    def get_references(self) -> List[int]:
        return self.__references

    def __repr__(self) -> str:
        return f'Process with references: {self.__references}'

    @property
    def frames(self) -> int:
        return self.__max_frames
