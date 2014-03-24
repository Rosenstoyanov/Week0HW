from solution import contains_digit
import unittest


class contains_digit_test(unittest.TestCase):
    def test0(self):
        self.assertFalse(contains_digit(123, 4))

    def test1(self):
        self.assertTrue(contains_digit(42, 2))

    def test2(self):
        self.assertTrue(contains_digit(1000, 0))

    def test3(self):
        self.assertFalse(contains_digit(12346789, 5))


if __name__ == '__main__':
    unittest.main()
