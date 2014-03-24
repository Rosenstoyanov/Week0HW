from source import sevens_in_a_row
import unittest


class sevens_test(unittest.TestCase):
    def test0(self):
        self.assertTrue(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))

    def test1(self):
        self.assertFalse(sevens_in_a_row([1, 7, 1, 7, 7], 4))

    def test2(self):
        self.assertTrue(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))

    def test3(self):
        self.assertTrue(sevens_in_a_row([7, 2, 1, 6, 2], 1))


if __name__ == '__main__':
    unittest.main()
