from solution import count_words
import unittest


class count_words_tests(unittest.TestCase):
    def test0(self):
        result = count_words(["apple", "banana", "apple", "pie"])
        self.assertEqual(result, count_words(["apple", "banana", "apple", "pie"]))



if __name__ == '__main__':
    unittest.main()
