from solution import sum_of_divisors
import unittest


class sum_of_divisors_tests(unittest.TestCase):
    def test0(self):
        self.assertEqual(15, sum_of_divisors(8))

    def test1(self):
        self.assertEqual(8, sum_of_divisors(7))

    def test2(self):
        self.assertEqual(1, sum_of_divisors(1))

    def test3(self):
        self.assertEqual(2340, sum_of_divisors(1000))


if __name__ == '__main__':
    unittest.main()
