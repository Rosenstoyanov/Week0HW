from solution import prime_factorization
import unittest


class prime_factorization_test(unittest.TestCase):
    def test0(self):
        self.assertEqual([(2, 1), (5, 1)], prime_factorization(10))

    def test1(self):
        self.assertEqual([(2, 1), (7, 1)], prime_factorization(14))

    def test2(self):
        self.assertEqual([(2, 2), (89, 1)], prime_factorization(356))

    def test3(self):
        self.assertEqual([(89, 1)], prime_factorization(89))

    def test4(self):
        self.assertEqual([(2, 3), (5, 3)], prime_factorization(1000))

if __name__ == '__main__':
    unittest.main()
