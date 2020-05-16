from typing import Dict, List, Tuple


class Memory:

    def __init__(self, num_of_frames: int):
        self.deficiencies = []
        self.cursor = 0
        self.frames = self.__setup_frames(num_of_frames)

    def __setup_frames(self, num_of_frames: int) -> Dict[str, List]:
        """
        Create dict of frames list to manage history easier
        :param num_of_frames: number of frames
        :return: dict with key 'frame' + number and value list
        """
        frames = {f'frame{i + 1}': [] for i in range(num_of_frames)}
        return frames

    def __choose_previous(self, current_history_of_frame: List, idx: int):
        try:
            return current_history_of_frame[idx - 1]
        except IndexError:
            return 0

    def is_in_memory(self, value):
        if self.cursor - 1 >= 0:
            for items in self.frames.values():
                if items[self.cursor - 1] == value:
                    return True
        return False

    def __annotate_deficiency(self, frame: str, cursor_position: int):
        """
        Creates list of deficiencies of frames
        :param frame: name of frame
        :param cursor_position: current cursor position
        :return:
        """
        annotatation = (frame, cursor_position)
        self.deficiencies.append(annotatation)

    def update_frame(self, frame: str, value: int) -> None:
        """
        Update chosen frame and sets values in previous frames
        :param frame: key in dict
        :param value: value to put in frame
        :return:
        """
        if self.is_in_memory(value):
            for c_frame in self.frames.keys():
                self.frames[c_frame].insert(
                    self.cursor,
                    self.__choose_previous(self.frames[c_frame], self.cursor))
        else:
            for c_frame in self.frames.keys():
                # previous element in history
                if c_frame == frame:
                    self.frames[c_frame].insert(self.cursor, value)
                    self.__annotate_deficiency(frame, self.cursor)
                else:
                    self.frames[c_frame].insert(
                        self.cursor,
                        self.__choose_previous(self.frames[c_frame], self.cursor))

        self.cursor += 1

    def get_deficiencies(self) -> List[Tuple[str, int]]:
        """
        Returns list of annotations
        :return:
        """
        sm = sum([df[1] for df in self.deficiencies])
        return sm

    def get_history(self) -> Dict[str, List[int]]:
        """
        Returns history of frame changes
        :return:
        """
        return self.frames

    def get_names(self) -> List[str]:
        """
        Return list of names
        :return:
        """
        return list(self.frames.keys())

    def get_by_reference(self, value: int) -> str:
        """
        Return name of used frame
        :param value: value of frame
        :return:
        """
        for key in self.frames.keys():
            if self.frames[key][self.cursor - 1] == value:
                return key

    def get_value(self, frame: str, idx: int) -> int:
        return self.frames[frame][idx]
