from components.access_to_disk_.disk import Disk
from components.access_to_disk_.algorithms import FCFS, SSTF, Scan, CScan


ALGORITHMS = [
    FCFS,
    SSTF,
    Scan,
    CScan
]


def execute_access_to_disk(blocks, requests):
    disk = Disk(blocks=blocks)
    disk.setup_requests(requests)
    queues, all_cylinders, names = disk.execute_all(ALGORITHMS)
    return queues, all_cylinders, names
