import unittest

from if_condition import IfCondition


class TestIfCondition(unittest.TestCase):
    def test_if_condition(self):
        self.assertEqual(
            IfCondition('if condition variable my first var is equal to string rahil'.split()).code,
            'if my_first_var == \'rahil\':')
        self.assertEqual(
            IfCondition('if condition integer 2 is not equal to variable my first number'.split()).code,
            'if 2 != my_first_number:')
        self.assertEqual(
            IfCondition('if condition variable my second var is greater than or equal to variable my second number'.split()).code,
            'if my_second_var >= my_second_number:')
        self.assertEqual(
            IfCondition('if condition float 5 point 98 is less than variable my third number'.split()).code,
            'if 5.98 < my_third_number:')

    def test_elif_condition(self):
        self.assertEqual(
            IfCondition('else if condition variable my first var is equal to string rahil'.split()).code,
            'elif my_first_var == \'rahil\':')
        self.assertEqual(
            IfCondition('else if condition integer 2 is not equal to variable my first number'.split()).code,
            'elif 2 != my_first_number:')
        self.assertEqual(
            IfCondition('else if condition variable my second var is greater than or equal to variable my second number'.split()).code,
            'elif my_second_var >= my_second_number:')
        self.assertEqual(
            IfCondition('else if condition float 5 point 98 is less than variable my third number'.split()).code,
            'elif 5.98 < my_third_number:')

if __name__ == '__main__':
    unittest.main()