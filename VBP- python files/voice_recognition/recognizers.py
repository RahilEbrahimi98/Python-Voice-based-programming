import speech_recognition

from voice_recognition.exceptions import RecognizerException
from tkinter import messagebox

from word2number import w2n
from word2number.w2n import american_number_system


class SphinxRecognizer(object):
    def __init__(self, noise_adjust_duration=5):
        self.recognizer = speech_recognition.Recognizer()
        self.noise_adjust_duration = noise_adjust_duration
        self.current_result_text = ""

    def recognize(self, no_digits_allowed=False):
        with speech_recognition.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=self.noise_adjust_duration)
            messagebox.showinfo(message="Speak now")
            audio = self.recognizer.listen(source, phrase_time_limit=10)
        try:
            self.current_result_text = self.recognizer.recognize_sphinx(audio)
        except speech_recognition.UnknownValueError:
            raise RecognizerException("Sorry! Could not understand what you said")
        if not no_digits_allowed:
            self.__convert_text_number_to_digit()
        return self.current_result_text

    def __convert_text_number_to_digit(self):
        text = self.current_result_text
        words = text.split()
        length = len(words)
        i = 0
        result_status, result = False, None
        while i < length:
            for j in range(i, length):
                try:
                    self.__is_valid_number_pattern(words[i: j + 1])
                    result = w2n.word_to_num(" ".join(words[i:j + 1]))
                    result_status = True
                    if j == length - 1:
                        text = text.replace(" ".join(words[i:j + 1]), str(result))
                        i = j + 1
                        break
                except ValueError:
                    if result_status:
                        text = text.replace(" ".join(words[i:j]), str(result))
                        result_status = False
                        i = j
                    else:
                        i += 1
                    break

        self.current_result_text = text

    @staticmethod
    def __is_valid_number_pattern(lst):
        for element in lst:
            if element not in american_number_system:
                raise ValueError


class GoogleRecognizer(object):
    def __init__(self, noise_adjust_duration=5):
        self.recognizer = speech_recognition.Recognizer()
        self.noise_adjust_duration = noise_adjust_duration
        self.current_result_text = ""

    def recognize(self):
        with speech_recognition.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=self.noise_adjust_duration)
            messagebox.showinfo(message="Speak now")
            audio = self.recognizer.listen(source, phrase_time_limit=10)
        try:
            self.current_result_text = self.recognizer.recognize_google(audio)
        except speech_recognition.UnknownValueError:
            raise RecognizerException("Sorry! Could not understand what you said")
        except speech_recognition.RequestError:
            raise RecognizerException("Seems like we cannot connect to the internet at this time! Try again later")
        return self.current_result_text
