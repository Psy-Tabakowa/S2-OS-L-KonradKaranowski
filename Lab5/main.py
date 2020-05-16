from task_manager import TaskManager
from config import Config


def main():
    task_manager = TaskManager(Config.NUMBER_OF_PROCESSES,
                               Config.NUMBER_OF_CPUS,
                               Config.RANGE_PROCESSES_LOAD)
    task_manager.execute_all()


if __name__ == '__main__':
    main()
