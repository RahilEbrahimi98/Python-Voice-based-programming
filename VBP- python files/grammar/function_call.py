import functools
from grammar.variable_declaration import VariableDeclaration


class FunctionCall:

    def __init__(self, command):
        self.variable_types = ['integer', 'float', 'string', 'list', 'dictionary']
        self.command = command
        self.name = self.find_name()
        self.parameters = self.find_parameters()
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

    def find_name(self) -> str:
        """
        This function finds the name of the function which has to be defined.
            Returns:
                The exact name of the function.
        """
        end_of_name_index = self.command.index('parameters')
        this_name = self.convert_to_snake_case(self.command[2:end_of_name_index])
        return this_name

    def end_of_parameters_check(self, index: int) -> bool:
        """
        This function, in the parameters declaration, checks
        whether this index of the list is the last index of the parameters declaration or not.
            Args:
                index: The specified index that should be checked.
            Returns:
                If the index is the last index returns true, Otherwise returns false.
        """
        if self.command[index] == 'end' and self.command[index+1] == 'of' and self.command[index+2] == 'parameters':
            if index + 2 == len(self.command) - 1:
                return True
        return False

    def find_parameters(self) -> list:
        """
        This function finds the parameters of the function which has to be defined.
            Returns:
                The exact names of the parameters in  a list.
        """
        this_index = self.command.index('parameters') + 1
        this_parameters, this_parameter, variable_type = [], [], 0
        if self.command[this_index] == "end" and self.command[this_index + 1] == "of" and self.command[
            this_index + 2] == "parameters":
            return this_parameters
        while True:
            if self.command[this_index] == 'next' or self.end_of_parameters_check(this_index):
                if variable_type == 0:
                    this_parameters.append(self.convert_to_snake_case(this_parameter))
                elif variable_type == 1:
                    temp_command = VariableDeclaration(['variable', '_', 'is'] + this_parameter)
                    this_parameters.append(
                        functools.reduce(lambda first, second: f'{first} {second}', (temp_command.code.split())[2:]))
                if self.end_of_parameters_check(this_index):
                    break
                this_parameter = []
            else:
                if self.command[this_index] == 'variable':
                    variable_type = 0
                elif self.command[this_index] in self.variable_types:
                    this_parameter.append(self.command[this_index])
                    variable_type = 1
                else:
                    this_parameter.append(self.command[this_index])

            this_index += 1
        return this_parameters

    def generate_code(self):
        """
        This function generates the final code of the input command.
            Returns:
                The exact code of the function definition command.
        """
        if self.parameters !=[]:
            this_parameters = functools.reduce(lambda first, second: f'{first}, {second}', self.parameters)
            this_code = f'{self.name}({this_parameters[:len(this_parameters)]})'
        else:
            this_code = f'{self.name}()'
        return this_code
