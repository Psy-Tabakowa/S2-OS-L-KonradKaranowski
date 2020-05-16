from components.page_replacement.memory_manager import MemoryManager
from components.page_replacement.algorithms import FIFO, OPT, LRU, ALRU, RAND


ALGORITHMS = [
    FIFO,
    LRU,
    ALRU,
    RAND,
    OPT
]


def execute_page_replecement(num_of_pages, process_length, process_page):
    manager = MemoryManager(num_of_pages)
    manager.setup_processes(process_length, process_page)
    deficiencies, names = manager.execute_all(ALGORITHMS)
    return deficiencies, names
