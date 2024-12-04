from multiprocessing import Process
import os
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

    processes = []
    num_processes = os.cpu_count()

    # create processes
    process_loop = 0
    for i in range(8):
        process_loop += 1
        print("\nPROCESS #", process_loop)
        p = Process(target=square_numbers())
        p.start()
        processes.append(p)

    # start
    # for p in processes:


    # join
    for p in processes:
        p.join()

    print('End Processes')