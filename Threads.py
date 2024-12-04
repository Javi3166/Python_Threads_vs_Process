from threading import Thread
# import os
import time

if __name__ == '__main__':
    def square_numbers():
        loop_count = 0
        for index in range(100):
            value = index * index
            print(value)
            loop_count += 1
            print("Loop count: ", loop_count)
            time.sleep(0.01)

    threads = []
    num_threads = 10

    # create threads
    thread_loop = 0
    for i in range(num_threads):
        thread_loop += 1
        print("\nTHREAD #", thread_loop)
        t = Thread(target=square_numbers())
        t.start()
        threads.append(t)

    # start
    # for t in threads:


    # join
    for t in threads:
        t.join()

    print('End Threads')