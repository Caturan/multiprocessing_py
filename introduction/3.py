
"""
Shared Memory
    Data can be stored in a shared memory map using Value or Array. 
"""

from multiprocessing import Process, Value, Array 

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

def main():
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num,arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])


"""
Server Process
    A manager object returned by Manager() controls a server process which hold Python objects and allow other processes to manipulate them using proxies. 
    A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array. 
"""
from multiprocessing import Process, Manager

def f1(d,l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

def main1():
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(20))

        p = Process(target=f1, args=(d,l))
        p.start()
        p.join()

        print(d)
        print(l)
"""
    Server process managers are more flexible than using shared memory objects because they can be made to support arbitrary object types. 
    Also, a single manager can be shared by processes on different computers over a network. They are, however, slower than using shared memory. 
"""


if __name__ == '__main__':
    main()
    print()

    main1()