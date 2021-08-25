import functools

import inflect


class IfCondition:

    def __init__(self, command):
        self.variable_types = ['integer', 'float', 'string']   # dictionary and list need to be added
        self.compare_types = ['equal to', 'not equal to', 'less than', 'greater than', 'less than or equal to',
                              'greater than or ', 'equal to']
        if command[0] == 'else':
            self.command = command[3:]
            self.else_if = 1
        else:
            self.command = command[2:]
            self.else_if = 0
        self.is_keyword_index = self.find_is_keyword_index()
        self.first_part = self.dynamicOrNot(self.command, 'first_part')
        self.compare_type = self.find_compare_type()
        self.second_part = self.dynamicOrNot(self.command, 'second_part')
        self.code = self.generate_code()

    @staticmethod
    def convert_to_snake_case(name: list) -> str:
        """
        This function gives a list a words, and concatenates them in snake case format.
            Args:
                name: The list of words which will be converted to snake case.
            Returns:
                The snake case format of the input list of words.
        """
        snake_case_name = functools.reduce(lambda first, second: f'{first}_{second}', name)
        return str(snake_case_name)

    def dynamicOrNot(self, command, part):
        """
        This function checks if we are uding a dynamic variable or not
            Args:
                part: a string that shows if we are working on the first part of the if statement or second part.
            Returns:
                first or second part of if condition
        """
        if command[0] == 'variable':
            variable = self.find_name(part)
            return variable

        else:
            variable_type = self.find_type()
            return self.find_value(variable_type, part)

    def find_name(self, part) -> str:
        """
        This function finds the name of the dynamic variable.
            Returns:
                The exact name of the variable.
        """
        if part == 'first_part':
            end_of_name_index = self.is_keyword_index
        else:
            end_of_name_index = len(self.command)

        this_name = self.convert_to_snake_case(self.command[1:end_of_name_index])
        return this_name
    def find_type(self) -> str:
        """
        This function finds the variable which will be declared.
            Returns:
                The type of variable of the variable declaration command.
        """
        variable_type = self.command[0]
        return variable_type

    def find_value(self , variable_type, part) -> str:
        """
        This function finds the value of the variable which has to be declared based on the type.
            Returns:
                The exact value of the variable.
        """
        value = None
        if variable_type == 'integer':
            value = self.command[1]
        elif variable_type == 'float':
            value = f'{self.command[1]}'
        elif variable_type == 'string':
            if part == 'first_part':
                end_of_string = self.is_keyword_index
            else:
                end_of_string = len(self.command)
            value = self.parse_string(self.command[1: end_of_string])
        return value

    @staticmethod
    def parse_string(input_string: list) -> str:
        """
        This function gives a list a words, and concatenates them and creates a string.
            Args:
                input_string: The list of words which will be converted to string.
            Returns:
                The string format of the input list of words.
        """
        if 'letters' in input_string and len(input_string) - 1 != input_string.index('letters'):
            for index, word in enumerate(input_string[:len(input_string) - 1]):
                if word == 'letters':
                    number_value = input_string[index + 1]
                    if 57 >= ord(number_value[0]) >= 10:
                        input_string[index + 1] = inflect.engine().number_to_words(int(number_value))
                        input_string.pop(index)
        value = str(functools.reduce(lambda first, second: f'{first} {second}', input_string))
        return f'\'{value}\''

    def find_is_keyword_index(self) -> int:
        """
        This function finds the index of the *is* keyword, which is followed by compare_types.
            Returns:
                The exact index of the *is* keyword.
        """
        is_keyword_indices = [index for index, value in enumerate(self.command) if value == 'is']
        is_keyword_index = filter(lambda index: index if self.command[index + 1: index+3] or self.command[index + 1: index+4]
                                                         in [compare_type.split() for
                                                        compare_type in self.compare_types] else 0, is_keyword_indices)
        return list(is_keyword_index)[0]

    def find_compare_type(self) -> str:
        """
        This function finds the compare type that has been declared
            Returns:
                right python format of that compare type.
        """
        is_keyword_index = self.is_keyword_index
        compare_type = ''
        if " ".join(self.command[is_keyword_index + 1: is_keyword_index + 3]) == 'equal to':
            compare_type = '=='
            self.command = self.command[is_keyword_index + 3:]
        elif " ".join(self.command[is_keyword_index + 1: is_keyword_index + 4]) == 'not equal to':
            compare_type = '!='
            self.command = self.command[is_keyword_index + 4:]
        elif " ".join(self.command[is_keyword_index + 1: is_keyword_index + 6]) == 'less than or equal to':
            compare_type = '<='
            self.command = self.command[is_keyword_index + 6:]
        elif " ".join(self.command[is_keyword_index + 1: is_keyword_index + 6]) == 'greater than or equal to':
            compare_type = '>='
            self.command = self.command[is_keyword_index + 6:]
        elif " ".join(self.command[is_keyword_index + 1: is_keyword_index + 3]) == 'less than':
            compare_type = '<'
            self.command = self.command[is_keyword_index + 3:]
        elif " ".join(self.command[is_keyword_index + 1: is_keyword_index + 3]) == 'greater than':
            compare_type = '>'
            self.command = self.command[is_keyword_index + 3:]

        return compare_type


    def generate_code(self):
        """
        This function generates the final code of the input command.
            Returns:
                The exact code of the function definition command.
        """
        if self.else_if == 0:
            code = f'if {self.first_part} {self.compare_type} {self.second_part}:'
        else:
            code = f'elif {self.first_part} {self.compare_type} {self.second_part}:'
        return code


