from execution_manager import ExecutionManager
from config import Config
from methods import EqualAllocationMethod, ProportionalAllocateMethod,\
    DumbMethod, SphereAllocationMethod


METHODS = [
    EqualAllocationMethod,
    ProportionalAllocateMethod,
    DumbMethod,
    SphereAllocationMethod
]


def main():
    manager = ExecutionManager(Config.AVAILABLE_PAGES)
    processes = manager.setup_processes(Config.NUM_OF_PROCESSES,
                                        Config.LEN_OF_PROCESSES,
                                        Config.MIN_FRAMES,
                                        Config.MAX_FRAMES)
    manager.execute_all(METHODS, processes)


if __name__ == '__main__':
    main()
