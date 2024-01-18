
""" 
    Multiprocessing is a package that supports spawning processes using an API similar to threading mudole. 
    The multiprocessing package offers both local and remote concurrecy, effectively side-stepping the Global Interpreter Lock by using subprocesses intead of threads. 
"""

# The basic example of data parallelism using Pool:
from multiprocessing import Pool

def f1(x):
    return x*x

def main1():
    with Pool(5) as p:  # Pool(5) is the worker process number
        print(p.map(f1, [1,2,3]))



"""
The Process class:
    In multiprocessing, processes are spawned by creating a Process object and then calling its start() method. 
    Process follows the API threading.Thread. 
"""

from multiprocessing import Process

def f2(name):
    print('hello', name)

def main2():
    p = Process(target=f2, args=('bob',))
    p.start()
    p.join()

# To show the individual process IDs involved, here is an expanded example: 
from multiprocessing import Process
import os 

def info(title):
    print(title)
    print('module name:',__name__)
    print('parent process:', os.getppid())
    print('process id', os.getpid())

def f3(name):
    info('function f3')
    print('hello', name)

def main3():
    info('main line')
    p = Process(target=f3, args=('bob',))
    p.start()
    p.join()



if __name__ == '__main__':
    main1()  
    print()
    main2()
    print()
    main3()
