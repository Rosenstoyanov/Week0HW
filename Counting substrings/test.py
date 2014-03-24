from solution import count_substrings
import unittest


class count_substrings_test(unittest.TestCase):
    def test0(self):
        self.assertEqual(2, count_substrings("This is a test string", "is"))

    def test1(self):
        self.assertEqual(2, count_substrings("babababa", "baba"))

    def test2(self):
        self.assertEqual(4, count_substrings("Python is an awesome language to program in!", "o"))

    def test3(self):
        self.assertEqual(0, count_substrings("We have nothing in common!", "really?"))

    def test4(self):
        self.assertEqual(2, count_substrings("This is this and that is this", "this"))

if __name__ == '__main__':
    unittest.main()
