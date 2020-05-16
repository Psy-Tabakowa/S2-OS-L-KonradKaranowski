class Process:
    """
    Class of process, has random requirements
    """

    def __init__(self, load: float, time_of_execution: int):
        """
        :param load: (float) float in range (0, 0.4]
        :param time_of_execution: (int) time of execution in quants of time
        """
        self.__load = load
        self.__time_left = time_of_execution
        self.__is_active = False
        self.__is_finished = False

    def start(self) -> None:
        """
        Activate process
        :return:
        """
        self.__is_active = True

    @property
    def load(self) -> float:
        return self.__load

    @load.setter
    def load(self, new):
        self.__load += new

    @property
    def time_left(self):
        return self.__time_left

    @property
    def is_finished(self):
        return self.__is_finished

    @property
    def is_active(self):
        return self.__is_active

    def tick(self):
        """
        Decrease time by one second and if it's finished, set it as inactive
        :return:
        """
        self.__time_left -= 1
        if self.__time_left <= 0:
            self.__is_active = False
            self.__is_finished = True

    def __repr__(self):
        return f'Process with load: {self.__load} and time_left: {self.__time_left}'
