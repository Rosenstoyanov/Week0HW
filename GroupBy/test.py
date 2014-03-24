from solution import groupby
import unittest


class nth_fib_lists_test(unittest.TestCase):
    def test0(self):
        self.assertEqual({0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}, groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))


if __name__ == '__main__':
    unittest.main()
