import speech_recognition as sr
from word2number import w2n
import unittest


class GoogleRecognizerTest(unittest.TestCase):
    def setUp(self):
        self.r = sr.Recognizer()
        file = sr.AudioFile('assets/file.wav')
        with file as source:
            self.audio = self.r.record(source)
        self.result = self.r.recognize_google(self.audio).split()

    def test_dictionary(self):
        self.assertEqual("dictionary", self.result[0])

    def test_list(self):
        self.assertEqual("list", self.result[1])

    def test_is(self):
        self.assertEqual("is", self.result[2])

    def test_float(self):
        self.assertEqual("float", self.result[3])


class SphinxRecognizerTest(unittest.TestCase):
    def setUp(self):
        self.r = sr.Recognizer()
        file = sr.AudioFile('assets/file.wav')
        with file as source:
            self.audio = self.r.record(source)
        self.result = self.r.recognize_sphinx(self.audio).split()

    def test_dictionary(self):
        self.assertEqual("dictionary", self.result[0])

    def test_list(self):
        self.assertEqual("list", self.result[1])

    def test_is(self):
        self.assertEqual("is", self.result[2])

    def test_float(self):
        self.assertEqual("float", self.result[3])


class WordToNumberTest(unittest.TestCase):
    def test_decimal(self):
        self.assertEqual(w2n.word_to_num('two point three'), 2.3)
        self.assertEqual(w2n.word_to_num('two point zero three'), 2.03)

    def test_integer(self):
        self.assertEqual(w2n.word_to_num('two'), 2)
        self.assertEqual(w2n.word_to_num('two million three thousand nine hundred and eighty four'), 2003984)
        self.assertEqual(w2n.word_to_num('one hundred thirty-five'), 135)
        self.assertEqual(w2n.word_to_num('one hundred thirty five'), 135)
