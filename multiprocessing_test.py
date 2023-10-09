import multiprocessing
from time import sleep


def create_message(q):
    print("Creating a message")
    sleep(2)
    mymesg = "this is a upper case string"
    print("pushing the message in the queue")
    q.put(mymesg)
    return


def parse_message(q):
    print("fetching the message from queue")
    sleep(2)
    mesg = q.get()
    print(f"got the message {mesg}")
    parsed_message = mesg.upper()
    print(parsed_message)


if __name__ == "__main__":

    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=create_message, args=(queue,))
    p2 = multiprocessing.Process(target=parse_message, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Ending the main process")
