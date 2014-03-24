from solution import nth_fib_lists
import unittest


class nth_fib_lists_test(unittest.TestCase):
    def test0(self):
        self.assertEqual([1], nth_fib_lists([1], [2], 1))

    def test1(self):
        self.assertEqual([2], nth_fib_lists([1], [2], 2))

    def test2(self):
        self.assertEqual([1, 2, 1, 3], nth_fib_lists([1, 2], [1, 3], 3))

    def test3(self):
        self.assertEqual([1, 2, 3, 1, 2, 3], nth_fib_lists([], [1, 2, 3], 4))

    def test4(self):
        self.assertEqual([], nth_fib_lists([], [], 100))


if __name__ == '__main__':
    unittest.main()
