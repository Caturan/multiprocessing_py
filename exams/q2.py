"""
    Complete the main function to
    satisfy these requirements:
    • Create a list of CheckPrime objects, each
    with a different number (n) to check for
    primality and start them as separate
    processes.
    • It is not allowed that the number of
    processes exceeds the number of cores in    
    the host PC.
    • Balance the load between the cores
    equally, so it is desired that one core
    waits another.

    class CheckPrime(multiprocessing.Process):
        def __init__(self, q: multiprocessing.Queue, n: int):
            super().__init__()
            self.q = q 
            self.n = n 

        @staticmethod
        def is_prime(n: int) -> bool:
            return n > 1 and all(n % i for i in range(2, n))

        def run(self):
            print(f"Checking{self.n}")
            if self.is_prime(self.n):
                self.q.put(self.n)

        def main():
            processes = []
            started_processes = []
            prime_queue = multiprocessing.Queue()
            n = 50 
            .
            .
            . 
            
            primes = []
            while not prime_queue.empty():
                primes.append(prime_queue.get())
            primes.sort()
            print(primes)
"""
import multiprocessing
import time


class CheckPrime(multiprocessing.Process):
    def __init__(self, q: multiprocessing.Queue, n: int):
        super().__init__()
        self.q = q
        self.n = n

    @staticmethod
    def is_prime(n: int) -> bool:
        return n > 1 and all(n % i for i in range(2, n))

    def run(self):
        print(f"Checking {self.n}")
        if self.is_prime(self.n):
            self.q.put(self.n)


def main():
    processes = []
    started_processes = []
    prime_queue = multiprocessing.Queue()
    n = 50
    for i in range(2, n + 1):
        processes.append(CheckPrime(prime_queue, i))
    while len(processes) > 0:
        if len(multiprocessing.active_children()) < multiprocessing.cpu_count():
            p = processes.pop()
            p.start()
            started_processes.append(p)
        else:
            time.sleep(0.1)
    for p in started_processes:
        p.join()
    primes = []
    while not prime_queue.empty():
        primes.append(prime_queue.get())
    primes.sort()
    print(primes)


if __name__ == "__main__":
    main()
