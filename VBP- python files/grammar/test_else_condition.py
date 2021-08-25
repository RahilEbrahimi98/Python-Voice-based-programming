import unittest

from else_condition import ElseCondition


class TestIfCondition(unittest.TestCase):
    def test_if_condition(self):
        self.assertEqual(
            ElseCondition('else condition'.split()).code, 'else:')

if __name__ == '__main__':
    unittest.main()