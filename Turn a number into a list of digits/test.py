from solution import number_to_list
import unittest


class BasicTestCase(unittest.TestCase):
    def test0(self):
        self.assertEqual([1, 2, 3], number_to_list(123))

    def test1(self):
        self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))

    def test2(self):
        self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))


if __name__ == '__main__':
    unittest.main()
