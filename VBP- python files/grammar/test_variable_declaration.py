import unittest

from variable_declaration import VariableDeclaration


class TestVariableDeclaration(unittest.TestCase):

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
        self.assertEqual(VariableDeclaration('variable my first dict is dictionary string age integer 21 then float 3.6'
                                             ' list string sina next integer 5 end of list end of dictionary'.split()).code,
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


if __name__ == '__main__':
    unittest.main()

