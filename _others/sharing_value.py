import multiprocessing

def share_value(v):
    v.value = 3.14
    

if __name__ == "__main__":
    
    v = multiprocessing.Value('d', 0.0)

    p = multiprocessing.Process(target=share_value, args=(v,))

    p.start()
    p.join()

    print(v.value)