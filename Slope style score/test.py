from solution import slope_style_score
import unittest


class slope_style_score_tests(unittest.TestCase):
    def test0(self):
        self.assertEqual(94.67, round(slope_style_score([94, 95, 95, 95, 90]),2))

    def test1(self):
        self.assertEqual(80.0, slope_style_score([60, 70, 80, 90, 100]))

    def test2(self):
        self.assertEqual(93.5, slope_style_score([96, 95.5, 93, 89, 92]))


if __name__ == '__main__':
    unittest.main()
