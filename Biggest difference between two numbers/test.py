from source import biggest_difference
import unittest


class biggest_difference_test(unittest.TestCase):
    def test0(self):
        self.assertEqual(-1, biggest_difference([1,2]))

    def test1(self):
        self.assertEqual(-4, biggest_difference([1,2,3,4,5]))

    def test2(self):
        self.assertEqual(-9, biggest_difference([-10, -9, -1]))

    def test3(self):
        self.assertEqual(-99, biggest_difference(range(100)))

if __name__ == '__main__':
    unittest.main()
