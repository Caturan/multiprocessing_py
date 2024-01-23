import multiprocessing
 
def square_list(numbers,q):
    for n in numbers:
        q.put(n*n)


if __name__ == "__main__":

    numbers = [2,4,6]
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=square_list, args=(numbers,q))

    p1.start()
    p1.join()

    while q.empty() is False:
        print(q.get())