import multiprocessing


result = []

def square_list(numbers):
    global result
    for n in numbers:
        print('square', n*n)
        result.append(n*n)
    print("within a process: result" ,result)

if __name__ == "__main__":
    arr = [1,2,3,4]
    p1 = multiprocessing.Process(target=square_list, args=(arr,))

    p1.start()
    p1.join()

    print('result', result)

    """
        Every process has its own address space(virtual memory). Thus program variables are not shared between two processes. 
        We need to use interprocess communication (IPC) techniques if we want to share data between two processes. 

        Difference between thread and process:
        The benefit of multiprocessing is that error or memory leak in one process wont hurt execution of another process. 
    """
    