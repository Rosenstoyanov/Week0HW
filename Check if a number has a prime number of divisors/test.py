from solution import prime_number_of_divisors
import unittest

class BasicTestCase(unittest.TestCase):
    def test0(self):
        self.assertTrue(prime_number_of_divisors(7))

    def test1(self):
        self.assertFalse(prime_number_of_divisors(8))

    def test2(self):
        self.assertTrue(prime_number_of_divisors(9))

if __name__ == '__main__':
    unittest.main()
