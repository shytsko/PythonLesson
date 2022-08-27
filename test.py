from threading import Thread, current_thread
import random
from time import sleep
from queue import Queue


def PrintTask(q: Queue):
    while True:
        msg = q.get()
        print(msg)
        q.task_done()


def Task(arg, q: Queue):
    q.put(f"Start thread {current_thread().name}")
    for i in range(arg):
        sleep(random.random()*10)
        q.put(f"Thread {current_thread().name}: {arg=}, {i=}")
    q.put(f"Stop thread {current_thread().name}")


threads = []
q = Queue()

pr = Thread(target=PrintTask, name="PrintTask", args=(q,))
pr.setDaemon(True)
pr.start()


threads.append(Thread(target=Task, name="Task1", args=(3, q)))
threads.append(Thread(target=Task, name="Task2", args=(4, q)))
threads.append(Thread(target=Task, name="Task3", args=(2, q)))
threads.append(Thread(target=Task, name="Task4", args=(5, q)))

for t in threads:
    t.start()

for t in threads:
    t.join()

q.put("All task stop")

q.join()
