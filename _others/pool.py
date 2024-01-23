from multiprocessing import Pool
import time 

def f(n):
    sum = 0
    for n in range(1000):
        sum += n*n 
    return sum 

if __name__ == "__main__":
    
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(100000))
    p.close()
    p.join()

    print("Pool took: ", time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print("Serial processes ", time.time()-t2)