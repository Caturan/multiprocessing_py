import multiprocessing, time

def withdraw(balance,lock):
    for n in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1 
        lock.release()

def deposit(balance,lock):
    for n in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

if __name__ == "__main__":
    
    balance = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=withdraw, args=(balance,lock,)) 
    p2 = multiprocessing.Process(target=deposit, args=(balance,lock,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(balance.value)