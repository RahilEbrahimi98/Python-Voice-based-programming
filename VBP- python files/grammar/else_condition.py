
class ElseCondition:

    def __init__(self, command):
        self.command = command
        self.code = self.generate_code()

    def generate_code(self):
        code = ''
        if self.command[0] == 'else' and self.command[1] == 'condition' and len(self.command) == 2:
            code = f'else:'
        return code
