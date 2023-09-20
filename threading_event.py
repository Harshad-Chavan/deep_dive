from threading import Event, Thread
from time import sleep

event = Event()


def task(event, i):
    event.wait()
    print(f"this is thread {i}")
    sleep(1)
    print(f"{i} thread_finished")


for _ in range(5):
    th = Thread(target=task, args=(event, _))
    th.start()

print("settign event")
sleep(10)
event.set()

print("Main thread has ended")
