from queue import Queue
from threading import Thread

myqueue = Queue()


def task_1(myqueue):
    # craeting variable in task 1
    temp = 7
    myqueue.put(temp)
    print(temp)


def task_2(myqueue):
    # accepting varibel in task 2
    temp = myqueue.get()
    temp += 5
    print(temp)


th1 = Thread(target=task_1, args=(myqueue,))
th2 = Thread(target=task_2, args=(myqueue,))

th1.start()
th2.start()





