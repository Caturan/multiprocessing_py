import multiprocessing, time 

def square_list(numbers):
    print("Square list")
    for n in numbers:
        time.sleep(4)
        print('Square ' + str(n*n))

def calculate_cubes(numbers):
    print("Cubes")
    for n in numbers:
        time.sleep(4)
        print('Cubes ' + str(n*n*n))


if __name__ == "__main__":
    arr = [1,2,3,4]

    p1 = multiprocessing.Process(target=square_list, args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cubes, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()