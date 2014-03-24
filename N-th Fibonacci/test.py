from solution import nthFib
import unittest

class FibTest(unittest.TestCase):
    """docstring for FibTest"""
    def test_fib1(self):
        result = nthFib(1)
        self.assertEqual(1,result)

    def test_fib2(self):
        result = nthFib(2)
        self.assertEqual(2,result)

    def test_fib3(self):
        result = nthFib(3)
        self.assertEqual(2,result)

    def test_fib10(self):
        result = nthFib(10)
        self.assertEqual(55,result)
if __name__ == '__main__':
    unittest.main()
