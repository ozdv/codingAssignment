# Your program should accept the max value, N, as a command line argument,
# and run benchmark tests for each algorithm in parallel.
# For example, if your program is written in Java the Sieve of Eratosthenes testing should run in one thread,
# and the Brute Force testing should run concurrently in a separate thread.
# Finally, your program should report the results of the benchmarking to the screen and exit.
# At a minimum the measured execution time of each algorithm should be printed.

# We are looking for you to:
    # Use unit tests to show the correctness of your implementation
    # Add any applicable documentation
    # Note any assumptions that you make
    # Include instructions on how to run your program
    # Use git for version control

############################################################################################################################

import math
import threading
import time
from multiprocessing import Process, cpu_count


def main():
    '''main function'''

    # sterilize inputs to ensure program doesn't break
    max_value = 0
    while max_value < 2:
        try:
            max_value = int(input('Please enter an max value: '))
        except ValueError:
            print('Please enter a valid integer greater than 1')
            continue
        if max_value < 2:
            print('Please enter a valid integer greater than 1')

    # start time of performance tracker, subtract from functional counters to get run time
    start_time = time.perf_counter()

    brute_force = threading.Thread(target=brute_force_generate_prime, args=(max_value,))
    sieve_eratosthenes = threading.Thread(target=sieve_eratosthenes_generate_prime, args=(max_value,))
    brute_force.start()
    sieve_eratosthenes.start()
    brute_force.join()
    sieve_eratosthenes.join()


def brute_force_generate_prime(max):
    '''returns all prime numbers up to a given max integer'''
    start_time = time.perf_counter()

    i = 2
    prime_int_array = []

    while i <= max:
        is_prime = True
        for x in range(2, int(math.sqrt(i) + 1)):
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            prime_int_array.append(i)
        i += 1

    print('Brute Force execution time: ', time.perf_counter() - start_time, 'seconds')
    return prime_int_array


def sieve_eratosthenes_generate_prime(max):
    '''returns all prime numbers up to a given max integer using Sieve of Eratosthenes method'''
    start_time = time.perf_counter()

    truth_array = [True for i in range(max+1)]
    prime_int_array = []
    counter = 2

    # calculate whether to mark truth_array[counter] or not, i.e. determines if value is prime
    while counter * counter <= max:
        if truth_array[counter] is True:
            for i in range(counter * counter, max+1, counter):
                truth_array[i] = False
        counter += 1

    # traverse truth_array and generate list of all primes
    for counter in range(2, max+1):
        if truth_array[counter]:
            prime_int_array.append(counter)

    print('Sieve Eratosthenes execution time: ', time.perf_counter() - start_time, 'seconds')
    return prime_int_array


# this line is to resolve potential issues with running python on windows
if __name__ == '__main__':
    main()
