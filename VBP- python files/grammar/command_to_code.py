from builtins import Exception

from grammar.if_condition import IfCondition
from grammar.function_definition import FunctionDefinition
from grammar.variable_declaration import VariableDeclaration
from grammar.return_function import ReturnFunction
from grammar.function_call import FunctionCall
from grammar.else_condition import ElseCondition

class CommandToCode:

    def __init__(self):
        self.variable_types = ['integer', 'float', 'string', 'list', 'dictionary', 'variable', 'operation']
        self.compare_types = ['equal to', 'not equal to', 'less than', 'greater than', 'less than or equal to',
                              'greater than or ']

    def set_command(self, command: list):
        """
        This function sets the command variable.
            Args:
                command: The list of words which will be converted to code.
        """
        self.command = command

    def remove_command(self):
        """
        This function deletes the current command.
        """
        self.command = None

    def variable_error_check(self):
        """
        This function checks the correctness of variable declaration commands.
        """
        if len(self.command) < 5:
            raise Exception("The Format Is Wrong")
        is_index, point_index = -1, -1
        for index, item in enumerate(self.command):
            if item == 'is' and self.command[index + 1] in self.variable_types:
                is_index = index
            if item == 'point':
                point_index = index
        if is_index == -1:
            raise Exception("Is Keyword Not Found")
        if self.command[is_index + 1] not in self.variable_types:
            raise Exception("Variable Type Is Unacceptable")
        if self.command[is_index + 1] == 'integer':
            if not self.command[is_index + 2].isdigit():
                raise Exception("The Value Is Not Number")
        if self.command[is_index + 1] == 'operation':
            if is_index + 2 > len(self.command) - 1:
                raise Exception("Operation Type Not Defined")
            if self.command[is_index + 2] == 'add':
                if is_index + 3 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[is_index + 3] not in ['integer', 'float', 'string', 'list', 'variable']:
                    raise Exception("Variable Type is Unacceptable")

                if self.command[is_index + 3] == 'integer':
                    if not self.command[is_index + 4].isdigit():
                        raise Exception("The Value Is Not Number")

                if 'to' not in self.command[is_index + 2:]:
                    raise Exception("To keyword not found")
                for index, item in enumerate(self.command):
                    if item == 'to':
                        to_index = index
                if to_index + 1 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[to_index + 1] not in ['integer', 'float', 'string', 'list', 'variable']:
                    raise Exception("Variable Type is Unacceptable")
                if to_index + 2 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[to_index + 1] == 'integer':
                    if not self.command[to_index + 2].isdigit():
                        raise Exception("The Value Is Not Number")
            elif self.command[is_index + 2] == 'subtract':
                if is_index + 3 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[is_index + 3] not in ['integer', 'float', 'string', 'list', 'variable']:
                    raise Exception("Variable Type is Unacceptable")
                if self.command[is_index + 3] == 'integer':
                    if not self.command[is_index + 4].isdigit():
                        raise Exception("The Value Is Not Number")

                if 'from' not in self.command[is_index + 2:]:
                    raise Exception("From keyword not found")
                for index, item in enumerate(self.command):
                    if item == 'from':
                        from_index = index
                if from_index + 1 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[from_index + 1] not in ['integer', 'float', 'string', 'list', 'variable']:
                    raise Exception("Variable Type is Unacceptable")
                if from_index + 2 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[from_index + 1] == 'integer':
                    if not self.command[from_index + 2].isdigit():
                        raise Exception("The Value Is Not Number")
            elif self.command[is_index + 2] == 'multiply' or self.command[is_index + 2] == 'divide':
                if is_index + 3 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[is_index + 3] not in ['integer', 'float', 'string', 'list', 'variable']:
                    raise Exception("Variable Type is Unacceptable")
                if self.command[is_index + 3] == 'integer':
                    if not self.command[is_index + 4].isdigit():
                        raise Exception("The Value Is Not Number")

                if 'by' not in self.command[is_index + 2:]:
                    raise Exception("By keyword not found")
                for index, item in enumerate(self.command):
                    if item == 'by':
                        by_index = index
                if by_index + 1 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[by_index + 1] not in ['integer', 'float', 'string', 'list', 'variable']:
                    raise Exception("Variable Type is Unacceptable")
                if by_index + 2 > len(self.command) - 1:
                    raise Exception("wrong format")
                if self.command[by_index + 1] == 'integer':
                    if not self.command[by_index + 2].isdigit():
                        raise Exception("The Value Is Not Number")
            else:
                raise Exception("Operation Type Is Unacceptable")


    def return_error_check(self):
        """
        This function checks the correctness of return commands.
        """
        if len(self.command) < 3:
            raise Exception("The Format Is Wrong")
        if self.command[1] not in self.variable_types + ['variable']:
            raise Exception("Variable Type Is Wrong")
        if self.command[1] != 'variable':
            this_command = self.command
            self.command = ['variable', '_', 'is'] + self.command[1:]
            self.variable_error_check()
            self.command = this_command

    def function_call_error_check(self):
        """
        This function checks the correctness of function call commands.
        """
        if len(self.command) < 9:
            raise Exception("The Format Is Wrong")
        if 'parameters' not in self.command:
            raise Exception("Argument Parameters Is Missed")
        if self.command[-1] != 'parameters':
            raise Exception("End of Parameters Not Found")
        if self.command[-2] != 'of':
            raise Exception("End of Parameters Not Found")
        if self.command[-3] != 'end':
            raise Exception("End of Parameters Not Found")

    def if_condition_error_check(self):
        if self.command[0] == 'else':
            self.command = self.command[1:]
        if len(self.command) < 9:
            raise Exception("The Format Is Wrong")
        if self.command[2] not in ['variable', 'integer', 'float', 'string']:
            raise Exception("Variable Type Is Wrong")
        if self.command[2] == 'integer':
            if not self.command[3].isdigit():
                raise Exception("The Value Is Not Number")
            if self.command[4] != 'is':
                raise Exception("The Format Is Wrong")
        if self.command[2] == 'float':
            if self.command[4] != 'is':
                raise Exception("The Format Is Wrong")
        is_index = -1
        for index, value in enumerate(self.command):
            if value == 'is':
                if self.command[index + 1: index + 3] in [compare_type.split() for compare_type in self.compare_types]\
                        or self.command[index + 1: index + 4] in [compare_type.split() for compare_type in self.compare_types]:
                    is_index = index
        if is_index == -1:
            raise Exception("Compare Type Is Wrong")
        if " ".join(self.command[is_index + 1: is_index + 3]) in ['equal to', 'less than', 'greater than']:
            second_var_index = is_index + 3
        elif " ".join(self.command[is_index + 1: is_index + 4]) == 'not equal to':
            second_var_index = is_index + 4
        elif " ".join(self.command[is_index + 1: is_index + 6]) in ['less than or equal to', 'greater than or equal to']:
            second_var_index = is_index + 6
        if self.command[second_var_index] not in ['variable', 'integer', 'float', 'string']:
            raise Exception("Variable Type Is Wrong")
        if self.command[second_var_index] == 'integer':
            if not self.command[second_var_index + 1].isdigit():
                raise Exception("The Value Is Not Number")

    def else_condition_error_check(self):
        if len(self.command) != 2:
            raise Exception("The Format Is Wrong")

    def define_function_error_check(self):
        if len(self.command) < 7:
            raise Exception("The Format Is Wrong")
        parametrs_index = -1
        for index, value in enumerate(self.command[:-3]):
            if value == 'parameters':
                parametrs_index = index
        if parametrs_index == -1:
            raise Exception("Parameters keyword not found")
        if self.command[parametrs_index + 1] == 'next':
            raise Exception("The Format Is Wrong")
        for index, value in enumerate(self.command[parametrs_index + 1:-3]):
            if value == 'next':
                if index == len(self.command[parametrs_index + 1:-3]) - 1:
                    raise Exception("The Format Is Wrong")
        if not self.command[-1] == 'parameters' and self.command[-2] == 'of' and self.command[-3] == 'end':
            raise Exception("end of parameters not defined")



    def generate_code(self) -> str:
        """
        This function, based on the command, generates the final code of the input command.
            Returns:
                The code of the input command.
        """
        if self.command is None:
            return 'Command has not been assigned.'
        elif self.command[0] == 'variable':
            self.variable_error_check()
            return VariableDeclaration(self.command).code
        elif self.command[0] == 'return':
            self.return_error_check()
            return ReturnFunction(self.command).code
        elif self.command[0] == 'function' and self.command[1] == 'call':
            self.function_call_error_check()
            return FunctionCall(self.command).code
        elif self.command[0] == 'if' and self.command[1] == 'condition':
            self.if_condition_error_check()
            return IfCondition(self.command).code
        elif self.command[0] == 'else' and self.command[1] == 'if' and self.command[2] == 'condition':
            self.if_condition_error_check()
            self.command.insert(0, 'else')
            return IfCondition(self.command).code
        elif self.command[0] == 'else' and self.command[1] == 'condition':
            self.else_condition_error_check()
            return ElseCondition(self.command).code
        elif self.command[0] == 'define' and self.command[1] == 'function':
            self.define_function_error_check()
            return FunctionDefinition(self.command).code
        elif self.command[0] == 'end' and self.command[1] == 'of' and \
                (self.command[2] == 'function' or self.command[2] == 'if' or self.command[2] == 'else'):
            return ''
        else:
            raise Exception("Invalid Format")
