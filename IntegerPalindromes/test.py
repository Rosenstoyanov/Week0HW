from solution import is_int_palindrome
import unittest


class is_int_palindrome_tests(unittest.TestCase):
    def test0(self):
        self.assertTrue(is_int_palindrome(1))

    def test1(self):
        self.assertFalse(is_int_palindrome(42))

    def test2(self):
        self.assertTrue(is_int_palindrome(100001))

    def test3(self):
        self.assertTrue(is_int_palindrome(999))

    def test4(self):
        self.assertFalse(is_int_palindrome(123))


if __name__ == '__main__':
    unittest.main()
