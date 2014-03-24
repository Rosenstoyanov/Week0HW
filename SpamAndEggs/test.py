from solution import prepare_meal
import unittest


class prepare_meal_test(unittest.TestCase):
    def test0(self):
        self.assertEqual('eggs', prepare_meal(5))

    def test1(self):
        self.assertEqual('spam and eggs', prepare_meal(15))


if __name__ == '__main__':
    unittest.main()
