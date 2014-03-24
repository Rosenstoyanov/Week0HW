from solution import list_to_number
import unittest


class list_to_number_test(unittest.TestCase):
    def test0(self):
        self.assertEqual(123, list_to_number([1,2,3]))

    def test1(self):
        self.assertEqual(99999, list_to_number([9,9,9,9,9]))

    def test2(self):
        self.assertEqual(123023, list_to_number([1,2,3,0,2,3]))


if __name__ == '__main__':
    unittest.main()

