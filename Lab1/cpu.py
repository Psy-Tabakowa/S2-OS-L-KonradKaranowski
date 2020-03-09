from matplotlib import pyplot as plt
import copy


from process import Process


class CPU:

    def init_processes(self, num_of_processes, phase_len_range=(5, 20)):
        """
        Initialize processes
        :param num_of_processes: number of processes
        :param phase_len_range: range of phase length
        :return:
        """
        self.processes = [
            Process(num=i, phase_len_range=phase_len_range) for i in range(num_of_processes)
        ]

    def __execute(self, algorithm, processes) -> float:
        """
        Execute specified algorithm
        :param algorithm: class
        :param processes: list of processes
        :return:
        """
        algorithm = algorithm(processes)
        print('-' * 20)
        algorithm.execute()
        print('-' * 20)
        mean_time = algorithm.summary()
        return mean_time

    def execute_all(self, algorithms) -> None:
        """
        Execute all algorithms
        :param algorithms: list of classes
        :return:
        """
        names = []
        times = []
        for Algorithm in algorithms:
            name = Algorithm.get_name()
            print(f'Executing: {name}')
            time = self.__execute(Algorithm, self.return_copy())
            names.append(name)
            times.append(time)
            print('\t')
        self.__plot_results(names, times)

    def return_copy(self) -> [Process]:
        """
        Create copy of list of processes
        :return: list of processes
        """
        new_list = copy.deepcopy(self.processes)
        return new_list

    def __plot_results(self, names, times) -> None:
        """
        Plots statistics using pyplot library
        :param names: names of algorithms
        :param times: list of times to wait
        :return:
        """
        colors = ['red', 'blue', 'green', 'purple']
        plt.bar(names, times, color=colors)
        plt.grid()
        plt.xlabel('Algorithm')
        plt.ylabel('Mean time to wait (time units)')
        plt.show()
