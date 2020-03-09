from cpu import CPU
from algorithms import FCFS, SJF, SJF2, RoundRobin


ALGORITHMS = [
    FCFS,
    SJF,
    SJF2,
    RoundRobin
]


def main():
    cpu = CPU()
    cpu.init_processes(num_of_processes=30)
    cpu.execute_all(ALGORITHMS)


if __name__ == '__main__':
    main()
