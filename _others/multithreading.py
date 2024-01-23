import time 
import threading

def square_list(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.5)
        print('square', n*n)


def calculate_cubes(numbers):
    print("calculate cube numbers")
    for n in numbers:
        time.sleep(0.5)
        print('cubes', n*n*n)

arr = [1,2,3,4]

t = time.time()
#(square_list(arr))
#(calculate_cubes(arr))

t1 = threading.Thread(target=square_list, args=(arr,))
t2 = threading.Thread(target=calculate_cubes, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(time.time() - t)