import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):

    def test_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

    def test_non_primes(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

if __name__ == "__main__":
    unittest.main()
