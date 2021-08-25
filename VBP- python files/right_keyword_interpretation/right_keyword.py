from libindic.soundex import Soundex
from difflib import SequenceMatcher

keyword_list = [('def', 0.5, 'D1'), ('is', 0.5, 'I2'), ('variable', 0.5, 'V614'), ('string', 0.5, 'S365'),
                ('integer', 0.5, 'I532'), ('float', 0.5, 'F432'), ('list', 0.5, 'L232'), ('Dictionary', 0.5, 'D235')]

soundex = Soundex()


def right_keyword(word, keywords):
    """
    This function gets a word, and find out if engine has misinterpreted this word by checking possible list of keywords.
     It uses pronunciation to compare the word with keywords.
        Args:
            word: a string that contains just one word.
            keywords : list of possible keywords. this list has chosen according to grammar.
        Returns:
            right keyword.
    """
    sound = soundex.soundex(word)
    for i in keywords:
        key_word = i[0]
        key_word_sound = i[2]
        ratio = SequenceMatcher(None, sound, key_word_sound).ratio()
        if ratio >= i[1]:
            return key_word
    return word
