from solution import sum_of_digits_n
import unittest

class pr1Test(unittest.TestCase):
    """docstring for pr1Test"""
    def test_sum_of_digits_n1(self):
        self.assertEqual(43,sum_of_digits_n(1325132435356))

    def test_sum_of_digits_n2(self):
        self.assertEqual(6,sum_of_digits_n(123))

    def test_sum_of_digits_n1(self):
        self.assertEqual(6,sum_of_digits_n(6))
if __name__ == '__main__':
    unittest.main()
