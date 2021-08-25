import unittest

from right_keyword_interpretation.keyword_recognition import keyword_recognition
from right_keyword_interpretation.right_keyword import right_keyword
from right_keyword_interpretation.soundex_generator import soundex_generator

test_answer = [('def', 0.5, 'D1'), ('is', 0.5, 'I2'), ('variable', 0.5, 'V614'), ('string', 0.5, 'S365'),
               ('integer', 0.5, 'I532'), ('float', 0.5, 'F432'), ('list', 0.5, 'L232'), ('Dictionary', 0.5, 'D235')]
test_case_soundex = ['def', 'is', 'variable', 'string', 'integer', 'float', 'list', 'Dictionary']


class TestRightKeywordInterpretation(unittest.TestCase):

    def test_soundex_generator(self):
        self.assertEqual(
            soundex_generator(test_case_soundex), test_answer)

    def test_right_keyword(self):
        self.assertEqual(right_keyword("Valuable", [('variable', 0.5, 'V614')]), "variable")
        self.assertEqual(right_keyword("action", [('condition', 0.5, 'C535')]), "condition")
        self.assertEqual(right_keyword("Greta", [('greater', 0.5, 'G636')]), "greater")

    def test_keyword_recognition(self):
        self.assertEqual(keyword_recognition("Valuable dog is integer 2"),
                         ["variable", "dog", "is", "integer", "2"])

        self.assertEqual(keyword_recognition('define Pension hello world Pyramids name end of parameters'),
                         ['define', 'function', 'hello', 'world', 'parameters', 'name', 'end', 'of', 'parameters'])

        self.assertEqual(keyword_recognition("if condition Valuable temp number equal to integer 22"),
                         ["if", "condition", "variable", "temp", "number", "equal", "to", "integer", "22"])

        self.assertEqual(keyword_recognition("if condition integer 22 Greta than or equal to integer 22"),
                         ["if", "condition", "integer", "22", "greater", "than", "or", "equal", "to", "integer", "22"])

        self.assertEqual(keyword_recognition("if action integer 20 less than integer 22"),
                         ["if", "condition", "integer", "20", "less", "than", "integer", "22"])

        self.assertEqual(keyword_recognition("end of Finches"),
                         ["end", "of", "function"])

        self.assertEqual(keyword_recognition("end of Pension"),
                         ["end", "of", "function"])

        self.assertEqual(keyword_recognition("return Valuable hello word"),
                         ["return", "variable", "hello", "word"])

        self.assertEqual(
            keyword_recognition("function call hello world Pyramids Valuable name next integer 22 end of parameters"),
            ["function", "call", "hello", "world", "parameters", "variable", "name", "next", "integer", "22", "end",
             "of", "parameters"])

        self.assertEqual(
            keyword_recognition("Valuable my first var is operation add string my string to string 2"),
            ["variable", "my", "first", "var", "is", "operation", "add", "string", "my", "string", "to",
             "string", "2"])

        self.assertEqual(
            keyword_recognition("remove Lean 33"),
            ["remove", "line", "33"])


if __name__ == '__main__':
    unittest.main()
