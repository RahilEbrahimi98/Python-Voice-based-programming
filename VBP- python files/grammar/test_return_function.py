import unittest

from return_function import ReturnFunction


class TestReturnFunction(unittest.TestCase):
    def test_return_function(self):
        self.assertEqual(
            ReturnFunction('return variable result'.split()).code,
            'return result')
        self.assertEqual(
            ReturnFunction('return string result is returned'.split()).code,
            'return \'result is returned\'')


if __name__ == '__main__':
    unittest.main()