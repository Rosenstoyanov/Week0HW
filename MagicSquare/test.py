from solution import magic_square
import unittest


class magic_square_test(unittest.TestCase):
    def test0(self):
        self.assertEqual(False, magic_square([[1,2,3], [4,5,6], [7,8,9]]))

    def test1(self):
        self.assertEqual(True, magic_square([[4,9,2], [3,5,7], [8,1,6]]))

    def test2(self):
        self.assertEqual(True, magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))


if __name__ == '__main__':
    unittest.main()
