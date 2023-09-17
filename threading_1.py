from threading import Thread
from time import sleep


def basic_task(list_of_elements):
    for _ in list_of_elements:
        print("thread is processing")
        sleep(1)
        print(f"processed item {_}")
    return


th1 = Thread(target=basic_task, args=([1, 2, 3, 4, 5],))
# th1.start()


class CustomThread(Thread):
    def __init__(self, value):
        Thread.__init__(self)
        self.value = value
        self.new_value = 0

    def run(self) -> None:
        print("in in method")
        for _ in range(0, self.value):
            print("processing")
            sleep(1)
            self.new_value += _
        print("thread Finished")
        return


th2 = CustomThread(10)
print(th2.new_value)
th2.start()
th2.join()
print(th2.new_value)
print("end of main thread")
