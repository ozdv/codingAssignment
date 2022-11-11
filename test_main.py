import unittest
from main import brute_force_generate_prime, sieve_eratosthenes_generate_prime

class PrimesTestCase(unittest.TestCase):
    '''Tests for `primes.py`.'''

    def test_if_both_return_equal_lists(self):
        '''Are both functions returning the same list of primes?'''
        self.assertCountEqual(brute_force_generate_prime(50), sieve_eratosthenes_generate_prime(50))


    def test_if_brute_force_return_primes_up_to_50(self):
        '''Is brute_force returning the correct primes?'''
        expected_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(expected_array, brute_force_generate_prime(50))


    def test_if_sieve_eratosthenes_return_primes_up_to_50(self):
        '''Is sieve_eratosthenes returning the correct primes?'''
        expected_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(expected_array, sieve_eratosthenes_generate_prime(50))

if __name__ == '__main__':
    unittest.main()
