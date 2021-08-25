import unittest

from function_call import FunctionCall


class TestFunctionCall(unittest.TestCase):
    def test_return_function(self):
        self.assertEqual(
            FunctionCall('function call first func parameters end of parameters'.split()).code,
            'first_func()')
        self.assertEqual(
            FunctionCall('function call second func parameters name next age end of parameters'.split()).code,
            'second_func(name, age)')


if __name__ == '__main__':
    unittest.main()