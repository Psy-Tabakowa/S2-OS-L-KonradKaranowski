from matplotlib import pyplot as plt


from components.access_to_processor_.cpu import CPU
from components.access_to_processor_.algorithms import FCFS, SJF2, SJF, RoundRobin


ALGORITHMS = [
    FCFS,
    SJF,
    SJF2,
    RoundRobin
]


def execute(num_of_processes, phase_len_min, phase_len_max):
    """
    Execute processes and return parameters to plot
    :param num_of_processes:
    :param phase_len_min:
    :param phase_len_max:
    :return:
    """
    cpu = CPU()
    cpu.init_processes(num_of_processes, (phase_len_min, phase_len_max))
    names, times = cpu.execute_all(ALGORITHMS)
    return names, times

