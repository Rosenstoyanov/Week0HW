from solution import calculate_coins
import unittest


class coins_tests(unittest.TestCase):
    def test_coins1(self):
        self.assertEqual({1: 1, 50: 1, 20: 0, 5: 0, 100: 0, 10: 0, 2: 1}, calculate_coins(0.53))

    def test_coins2(self):
        self.assertEqual({1: 0, 50: 1, 20: 2, 5: 0, 100: 8, 10: 0, 2: 2}, calculate_coins(8.94))


if __name__ == '__main__':
    unittest.main()
