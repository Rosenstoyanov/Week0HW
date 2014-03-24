from solution import count_vowels
import unittest


class count_vowels_test(unittest.TestCase):
    def test0(self):
        self.assertEqual(2, count_vowels("Python"))

    def test1(self):
        self.assertEqual(8, count_vowels("Theistareykjarbunga"))

    def test2(self):
        self.assertEqual(0, count_vowels("grrrrgh!"))

    def test3(self):
        self.assertEqual(22, count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test4(self):
        self.assertEqual(8, count_vowels("A nice day to code!"))


if __name__ == '__main__':
    unittest.main()
