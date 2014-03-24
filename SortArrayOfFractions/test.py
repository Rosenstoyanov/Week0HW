from solution import sort_fractions
import unittest


class sort_fractions_test(unittest.TestCase):
    def test0(self):
        self.assertEqual([(1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2)]))

    def test1(self):
        self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2), (1, 3)]))

    def test2(self):
        self.assertEqual([(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)], sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))


if __name__ == '__main__':
    unittest.main()
