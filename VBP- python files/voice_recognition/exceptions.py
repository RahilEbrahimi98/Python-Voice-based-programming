class RecognizerException(Exception):
    def __init__(self, message):
        self.message = message
