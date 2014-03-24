from solution import is_increasing
import unittest


class is_increasing_tests(unittest.TestCase):
    def test0(self):
        self.assertTrue(is_increasing([1,2,3,4,5]))

    def test1(self):
        self.assertTrue(is_increasing([1]))

    def test2(self):
        self.assertFalse(is_increasing([5,6,-10]))

    def test3(self):
        self.assertFalse(is_increasing([1,1,1,1]))


if __name__ == '__main__':
    unittest.main()
