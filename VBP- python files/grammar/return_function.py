import functools
from grammar.variable_declaration import VariableDeclaration


class ReturnFunction:

    def __init__(self, command):
        self.command = command
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

    def generate_dynamic_code(self) -> str:
        """
        This function is a helper function for generating final code for dynamic variables
            Returns:
                The final output of the input command for dynamic variables.
        """
        output = self.convert_to_snake_case(self.command[2:])
        return f'return {output}'

    def generate_static_code(self) -> str:
        """
        This function is a helper function for generating final code for static variables
            Returns:
                The final output of the input command for static variables.
        """
        temp_command = VariableDeclaration(['variable', '_', 'is'] + self.command[1:])
        value = functools.reduce(lambda first, second: f'{first} {second}', (temp_command.code.split())[2:])
        return f'return {value}'

    def generate_code(self) -> str:
        """
        This function gives the input command, and generates the final code.
            Returns:
                The final output of the input command.
        """
        if self.command[1] == 'variable':
            return self.generate_dynamic_code()
        else:
            return self.generate_static_code()

