from solution import what_is_my_sign
import unittest


class what_is_my_sign_tests(unittest.TestCase):
    def test0(self):
        self.assertEqual("Leo", what_is_my_sign(5, 8))

    def test1(self):
        self.assertEqual("Aquarius", what_is_my_sign(29, 1))

    def test2(self):
        self.assertEqual("Cancer", what_is_my_sign(30, 6))

    def test3(self):
        self.assertEqual("Gemini", what_is_my_sign(31, 5))

    def test4(self):
        self.assertEqual("Aquarius", what_is_my_sign(2, 2))

    def test5(self):
        self.assertEqual("Taurus", what_is_my_sign(8, 5))

    def test6(self):
        self.assertEqual("Capricorn", what_is_my_sign(9, 1))


if __name__ == '__main__':
    unittest.main()
