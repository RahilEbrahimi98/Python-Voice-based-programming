import unittest

from function_call import FunctionCall
from variable_declaration import VariableDeclaration
from return_function import ReturnFunction
from if_condition import IfCondition
from function_definition import FunctionDefinition
from else_condition import ElseCondition

class TestCommandToCode(unittest.TestCase):

    def test_return_function(self):
        self.assertEqual(
            FunctionDefinition('define function first func parameters end of parameters'.split()).code,
            'def first_func():')
        self.assertEqual(
            FunctionDefinition(
                'define function second func parameters name next age end of parameters'.split()).code,
            'def second_func(name, age):')

    def test_if_condition(self):
        self.assertEqual(
            IfCondition('if condition variable my first var is equal to string rahil'.split()).code,
            'if my_first_var == \'rahil\':')
        self.assertEqual(
            IfCondition('if condition integer 2 is not equal to variable my first number'.split()).code,
            'if 2 != my_first_number:')
        self.assertEqual(
            IfCondition(
                'if condition variable my second var is greater than or equal to variable my second number'.split()).code,
            'if my_second_var >= my_second_number:')
        self.assertEqual(
            IfCondition('if condition float 5.98 is less than variable my third number'.split()).code,
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
            IfCondition('else if condition float 5.98 is less than variable my third number'.split()).code,
            'elif 5.98 < my_third_number:')

    def test_if_condition(self):
        self.assertEqual(
            ElseCondition('else condition'.split()).code, 'else:')

    def test_return_function(self):
        self.assertEqual(
            FunctionCall('function call first func parameters end of parameters'.split()).code,
            'first_func()')
        self.assertEqual(
            FunctionCall('function call second func parameters name next age end of parameters'.split()).code,
            'second_func(name, age)')

    def test_integer(self):
        self.assertEqual(VariableDeclaration('variable my integer is number is integer 22'.split()).code,
                         'my_integer_is_number = 22')
        self.assertEqual(VariableDeclaration('variable number is integer 223425'.split()).code, 'number = 223425')

    def test_float(self):
        self.assertEqual(VariableDeclaration('variable my floating number is float 7.56'.split()).code,
                         'my_floating_number = 7.56')
        self.assertEqual(VariableDeclaration('variable number is integer 0.0'.split()).code, 'number = 0.0')
        self.assertEqual(VariableDeclaration('variable number is long is integer 0435235.0'.split()).code,
                         'number_is_long = 0435235.0')

    def test_string(self):
        self.assertEqual(
            VariableDeclaration('variable my first string is sentence is string my name is sina'.split()).code,
            'my_first_string_is_sentence = \'my name is sina\'')
        self.assertEqual(VariableDeclaration('variable my second string is string consider the number 42'.split()).code,
                         'my_second_string = \'consider the number 42\'')
        self.assertEqual(VariableDeclaration(
            'variable my third string is string consider the letters number letters 42'.split()).code,
                         'my_third_string = \'consider the letters number forty-two\'')

    def test_list(self):
        self.assertEqual(VariableDeclaration('variable my first list is list integer 5 next float 4.6 next string'
                                             ' sina end of list'.split()).code,
                         'my_first_list = [5, 4.6, \'sina\']')
        self.assertEqual(VariableDeclaration('variable my second list is list string my name next integer 12 next '
                                             'float 43.6 end of list'.split()).code,
                         'my_second_list = [\'my name\', 12, 43.6]')
        self.assertEqual(VariableDeclaration('variable my third list is list list list string inner list end of list '
                                             'end of list end of list'.split()).code,
                         'my_third_list = [[[\'inner list\']]]')

    def test_dictionary(self):
        self.assertEqual(VariableDeclaration('variable my first dict is dictionary string age integer 21 then float 3'
                                             '.6 list string sina next integer 5 end of list end of dictionary'.split()).code,
                         'my_first_dict = {\'age\': 21, 3.6: [\'sina\', 5]}')
        self.assertEqual(VariableDeclaration('variable my second dict is dictionary string age integer 21 then '
                                             'string number list float 4.6 next integer 5 next list list string '
                                             'inner list end of list end of list end of list end  of dictionary'.split()).code,
                         'my_second_dict = {\'age\': 21, \'number\': [4.6, 5, [[\'inner list\']]]}')

    def test_variable(self):
        self.assertEqual(VariableDeclaration('variable my first var is variable my second var'.split()).code,
                         'my_first_var = my_second_var')

    def test_operation(self):
        self.assertEqual(VariableDeclaration('variable my first var is operation add list string my string end of '
                                             'list to list integer 4 end of list'.split()).code,
                         'my_first_var = [\'my string\'] + [4]')
        self.assertEqual(VariableDeclaration('variable my second var is operation subtract variable x from float 1'
                                             '.7'.split()).code,
                         'my_second_var = 1.7 - x')
        self.assertEqual(VariableDeclaration('variable my third var is operation multiply integer 97 by float 87'
                                             '.06'.split()).code,
                         'my_third_var = 97 * 87.06')
        self.assertEqual(VariableDeclaration('variable my forth var is operation divide variable a by variable b'.split()).code,
                         'my_forth_var = a / b')

    def test_return_function(self):
        self.assertEqual(
            ReturnFunction('return variable result'.split()).code,
            'return result')
        self.assertEqual(
            ReturnFunction('return string result is returned'.split()).code,
            'return \'result is returned\'')

if __name__ == '__main__':
    unittest.main()