from solution import is_decreasing
import unittest


class is_decreasing_tests(unittest.TestCase):
    def test0(self):
        self.assertTrue(is_decreasing([5,4,3,2,1]))

    def test1(self):
        self.assertFalse(is_decreasing([1,2,3]))

    def test2(self):
        self.assertTrue(is_decreasing([100, 50, 20]))

    def test3(self):
        self.assertFalse(is_decreasing([1,1,1,1]))


if __name__ == '__main__':
    unittest.main()
