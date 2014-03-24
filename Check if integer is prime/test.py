from solution import is_prime
import unittest

class is_prime_tests(unittest.TestCase):
    def test0(self):
        self.assertFalse(is_prime(1))

    def test1(self):
        self.assertTrue(is_prime(2))

    def test2(self):
        self.assertFalse(is_prime(8))

    def test3(self):

        self.assertTrue(is_prime(11))

    def test4(self):
        self.assertFalse(is_prime(-10))


if __name__ == '__main__':
    unittest.main()
