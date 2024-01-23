"""
    The simple code given below, which
    generates two processes, gives an unpredictable
    output. Even if the usage of 'lock=True'
    argument does not solve the problem. Rewrite the
    functions plus_one_by_one and minus_one_by_one
    to solve the problem.

    from multiprocessing import Process, Value
    
    def plus_one_by_one(n: Value, times: int):
        for i in range(times):
            n.value += 1

    def minus_one_by_one(n:Value, times: int):
        for i in range(times):
            n.value -= 1
    
    if __name__ == "__main__":
        number = Value('i', 0, lock=True)
        p1 = Process(target=plus_one_by_one, args=(number,100000,))
        p2 = Process(target=minus_one_by_one, args=(number, 100000,))

        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(number.value)
"""

from multiprocessing import Process, Value, Lock

def plus_one_by_one(n: Value, times: int,lock):
    lock.acquire()
    for i in range(times):
        n.value += 1
    lock.release()

def minus_one_by_one(n:Value, times: int,lock):
    lock.acquire()
    for i in range(times):
        n.value -= 1
    lock.release()

if __name__ == "__main__":
    lock = Lock()
    number = Value('i', 0)
    p1 = Process(target=plus_one_by_one, args=(number,100000,lock))
    p2 = Process(target=minus_one_by_one, args=(number, 100000,lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(number.value)