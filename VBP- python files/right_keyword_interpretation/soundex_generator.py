import fuzzy

soundex = fuzzy.Soundex(4)

list = ['def', 'is', 'variable', 'string', 'integer', 'float', 'list', 'Dictionary', 'define', 'function', 'parameters',
        'end', 'of', 'parameters', 'next', 'if', 'condition', 'equal', 'less', 'greater', 'than', 'or ', 'return',
        "call", 'operation', 'add', 'subtract', 'multiply', 'divide', 'by', 'to', 'from', 'remove', 'line']


def soundex_generator(list):
    """
    This function gets a list of words, and return list of their soundex. soundex shows how a word should pronounce.
        Args:
            list: list fo string that each string contains just one word.
        Returns:
            list of soundex.
    """
    keywords_soundex = []
    for i in list:
        sound = soundex(i)
        keywords_soundex.append((i, 0.5, sound))
    return keywords_soundex


print(soundex_generator(list))
