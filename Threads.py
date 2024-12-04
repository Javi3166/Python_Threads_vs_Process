import threading
from threading import Thread
import time

def square_numbers():
    for index in range(100):
        value = index * index
        print(value)
        time.sleep(0.01)

if __name__ == '__main__':
    threads = []
    num_threads = 26

    # create threads
    thread_loop = 0
    for i in range(num_threads):
        thread_loop += 1
        print("\nTHREAD #", thread_loop)
        t = Thread(target=square_numbers)
        threads.append(t)

    # start
    for t in threads:
        t.start()

    # join
    for t in threads:
        t.join()

    print('End Threads')