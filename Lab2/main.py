from disk import Disk
from algorithm import FCFS, Scan, SSTF, CScan


ALGORITHMS = [
    FCFS,
    SSTF,
    Scan,
    CScan
]


def main():
    # WARNING blocks >= num of requests
    disk = Disk(blocks=30)
    disk.setup_requests(num_of_requests=30)
    disk.execute_all(ALGORITHMS)


if __name__ == '__main__':
    main()
