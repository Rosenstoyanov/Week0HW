from solution import is_number_balanced
import unittest


class is_number_balanced_tests(unittest.TestCase):
    def test0(self):
        self.assertTrue(is_number_balanced(9))

    def test1(self):
        self.assertTrue(is_number_balanced(11))

    def test2(self):
        self.assertFalse(is_number_balanced(13))

    def test3(self):
        self.assertTrue(is_number_balanced(121))

    def test4(self):
        self.assertTrue(is_number_balanced(4518))

    def test5(self):
        self.assertFalse(is_number_balanced(28471))

    def test6(self):
        self.assertTrue(is_number_balanced(1238033))


if __name__ == '__main__':
    unittest.main()
