from multiprocessing import Process
import os
import time

def square_numbers():
    for index in range(100):
        value = index * index
        print(value)
        time.sleep(0.01)

if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()

    # create processes
    process_loop = 0
    for i in range(num_processes):
        process_loop += 1
        print("\nPROCESS #", process_loop)
        p = Process(target=square_numbers())
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()

    print('End Processes')