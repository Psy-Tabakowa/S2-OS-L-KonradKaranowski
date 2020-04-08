from algorithms import LRU, ALRU, RAND, OPT, FIFO
from memory_manager import MemoryManager


ALGORITHMS = (
    FIFO,   # problem= Belady's anomaly
    LRU,
    ALRU,
    RAND,
    OPT
)


def main():
    manager = MemoryManager(num_of_pages=6)
    # WARNING! length of process >= num of pages used in process
    # num_of_pages is num of pages used in process, not in memory
    manager.setup_processes(length_of_process=15,
                            num_of_pages=7)
    manager.execute_all(ALGORITHMS)


if __name__ == '__main__':
    main()
