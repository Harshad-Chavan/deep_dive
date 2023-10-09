from concurrent.futures import ThreadPoolExecutor
from time import sleep


def worker_process():
    print("started worker thread ")
    sleep(2)
    print("worker process end ")


if __name__ == "__main__":

    pool = ThreadPoolExecutor(max_workers=2)

    pool.submit(worker_process)
    pool.submit(worker_process)
    pool.submit(worker_process)

    pool.shutdown(wait=True)

    print("Main thread continues")