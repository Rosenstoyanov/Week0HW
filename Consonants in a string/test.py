from solution import count_consonants
import unittest


class count_consonants_test(unittest.TestCase):
    def test0(self):
        self.assertEqual(4, count_consonants("Python"))

    def test1(self):
        self.assertEqual(11, count_consonants("Theistareykjarbunga"))

    def test2(self):
        self.assertEqual(7, count_consonants("grrrrgh!"))

    def test3(self):
        self.assertEqual(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test4(self):
        self.assertEqual(6, count_consonants("A nice day to code!"))


if __name__ == '__main__':
    unittest.main()
