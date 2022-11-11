import math
import time


def main():
    '''main function'''

    max_value = 0
    while max_value < 2:
        try:
            max_value = int(input('Please enter an max value: '))
        except ValueError:
            print('Please enter a valid integer greater than 1')
            continue
        if max_value < 2:
            print('Please enter a valid integer greater than 1')

    print(brute_force_generate_prime(max_value))
    print(sieve_eratosthenes_generate_prime(max_value))


def brute_force_generate_prime(max):
    '''returns all prime numbers up to a given max integer'''
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

    return prime_int_array


def sieve_eratosthenes_generate_prime(max):
    '''returns all prime numbers up to a given max integer using Sieve of Eratosthenes method'''

    non_prime_array = []
    prime_int_array = []

    for i in range(2, max+1):
        if i not in non_prime_array:
            prime_int_array.append(i)
            for j in range(i*i, max+1, i):
                non_prime_array.append(j)
    return prime_int_array


main()
