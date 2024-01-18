
"""
Context start methods
    Depending on the plaform, multiprocessing supports three ways to start a process. 
    These starts methods are: 
    
spawn:
    The parent process starts a fresh Python interpreter process. The child process will only inherit those resources necessary to run the process object's run() method. 
    In particular, unnecessary file descriptors and handles from the parent process will not inherited. 
    Starting a process using this method is rather slow compared to using fork or forkserver.     

fork: 
    The parent process uses os.fork() to fork the Python interpreter.  The child process, when it begins, is effectively identical to the parent process. 
    All resources of the parent are inherited by the child process. 
    Note that safely froking a multithreaded process is problematic. 

forkserver: 
    When the program starts and selects the forkserver start method, a server process is spawned. 
    From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. 

"""


# multiprocessing supports two types of communication channel between processes: 

# Queues
# The Queue class is a near clone of queue.Queue:
from multiprocessing import Process, Queue

def f1(q):
    q.put([42, None, 'hello'])

def main1():
    q = Queue()
    p = Process(target=f1, args=(q,))
    p.start()
    print(q.get())
    p.join()
# Queues are thread and process safe. 


# Pipes
# The Pipe function returns a pair of connection object connected by a pipe which by default is duplex (two-way). 
from multiprocessing import Process, Pipe 
import time 

def f2(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def main2():
    parent_conn, child_conn = Pipe()
    p = Process(target=f2, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
"""
    The two connection objects returned by Pipe() represent the two ends of the pipe. 
    Each connection object has send() and recv() methods. 
    Note that, data in a pipe may become corrupted if two processes(or threads) try to read from or write to the same end of the pipe at the same time.  
"""


"""
    multiprocessing contains equivalents of all the synchronization primitives from threading. 
    For instance one can use a lock to ensure that only one process prints to standard output at a time:
"""
from multiprocessing import Process, Lock 

def f3(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()
    
def main3():
    lock = Lock()

    for num in range(10):
        Process(target=f3, args=(lock, num)).start()




if __name__ == '__main__':
    main1()
    print()
    
    main2()
    print()
    
    main3()
