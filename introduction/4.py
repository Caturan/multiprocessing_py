
"""
Using a pool of workers
    The Pool class represents a pool of worker processes. It has methods which allows tasks to be offloaded to the worker processes in a few different ways. 
"""
from multiprocessing import Pool, TimeoutError
import time 
import os 

def f(x):
    return x*x 

def main():
    # start 4 worker processes
    with Pool(processes=4) as pool:
        print(pool.map(f, range(10)))

        print()

        for i in pool.imap_unordered(f, range(10)):
            print(i)

        print()

        res = pool.apply_async(f, (20,))
        print(res.get(timeout=1))

        print()

        res = pool.apply_async(os.getpid, ())
        print(res.get(timeout=1))

        print()

        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        print()

        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing. TimeoutError")

        print("For the moment, the pool remains available for more work")

    print("Now the pool is closed and no longer available")

if __name__ == "__main__":
    main()