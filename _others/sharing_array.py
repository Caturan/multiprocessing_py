import multiprocessing

def square_list(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n


if __name__ == "__main__":
    numbers = [1,3,5]
    result = multiprocessing.Array('i',3)  # i is data type integer or double; 3 is the size of array

    p1 = multiprocessing.Process(target=square_list, args=(numbers, result,))

    p1.start()
    p1.join()

    print(result[:])