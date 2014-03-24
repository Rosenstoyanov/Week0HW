import unittest
from solution import unique_words_count

class unique_words_count_tests(unittest.TestCase):
    """docstring for unique_words_count_tests"""
    def test0(self):
        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))
    def test1(self):
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))

if __name__ == '__main__':
    unittest.main()
