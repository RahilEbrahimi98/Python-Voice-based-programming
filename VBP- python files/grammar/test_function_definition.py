import unittest

from function_definition import FunctionDefinition


class TestFunctionDefinition(unittest.TestCase):
    def test_return_function(self):
        self.assertEqual(
            FunctionDefinition('define function first func parameters end of parameters'.split()).code,
            'def first_func():')
        self.assertEqual(
            FunctionDefinition('define function second func parameters name next age end of parameters'.split()).code,
            'def second_func(name, age):')


if __name__ == '__main__':
    unittest.main()