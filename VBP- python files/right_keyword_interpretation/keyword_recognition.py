from right_keyword_interpretation.right_keyword import right_keyword

keyword_list = [('variable', 0.5, 'V614'), ('define', 0.5, 'D155'), ('if', 0.5, 'I133'), ('end', 0.5, 'E533'),
                ('return', 0.5, 'R365'), ('function', 0.5, 'F523'), ('remove', 0.5, 'R511')]

variable_declaration = {('is', 0.6, 'I2')}
variable_type = {('string', 0.6, 'S365'),
                 ('integer', 0.6, 'I532'), ('float', 0.6, 'F432'), ('list', 0.6, 'L232'), ('Dictionary', 0.6, 'D235'),
                 ('operation', 0.6, 'O163')}

define_function = [('function', 0.5, 'F523')]
parameters = [('parameters', 0.7, 'P653')]
next_or_end_parameter = [('next', 0.6, 'N233'), ('end', 0.5, 'E533')]
end_of = [('of', 0.5, 'O133')]

if_condition = [('condition', 0.5, 'C535')]
compare = [('equal', 0.5, 'E245'), ('less', 0.5, 'L245'), ('greater', 0.5, 'G636')]
type_condition = [('string', 0.6, 'S365'), ('integer', 0.6, 'I532'), ('float', 0.6, 'F432'), ('variable', 0.5, 'V614')]

end_of_function = [('of', 0.5, 'O133'), ('function', 0.5, 'F523')]

operation_type = [('add', 0.7, 'A363'), ('subtract', 0.7, 'S136'), ('multiply', 0.7, 'M431'), ('divide', 0.7, 'D131')]

math_var = [('string', 0.6, 'S365'), ('integer', 0.6, 'I532'), ('float', 0.6, 'F432'), ('variable', 0.5, 'V614'),
            ('list', 0.6, 'L232')]

operation_conjunction = [('by', 0.5, 'B131'), ('to', 0.5, 'T131'), ('from', 0.5, 'F651')]


def keyword_recognition(string):
    """
    This function gets a string, and find out if there is a keyword that engine misinterpreted  and make it right.
        Args:
            string: string of interpreted words by engine.
        Returns:
            a list of words that user said
    """
    case_0 = -1
    case_1 = -1
    words_list = string.split(" ")
    n = len(words_list)
    answer = []
    index = 0
    while index < n:
        word = words_list[index]
        if case_0 == -1:
            if word == "start":
                answer = answer + [word]
                break

            word = right_keyword(word, keyword_list)
            if word == "variable":
                case_0 = 0

            elif word == 'define':
                answer = answer + [word]
                index = index + 1
                word = words_list[index]
                word = right_keyword(word, define_function)
                if word == 'function':
                    case_0 = 1

            elif word == "if":
                answer = answer + [word]
                index = index + 1
                word = words_list[index]
                word = right_keyword(word, if_condition)
                if word == 'condition':
                    case_0 = 2

            elif word == 'end':
                case_0 = 3

            elif word == 'return':
                case_0 = 4

            elif word == "function":
                answer = answer + [word]
                index = index + 1
                word = words_list[index]
                word = right_keyword(word, [('call', 0.5, 'C465')])
                if word == "call":
                    case_0 = 5

            elif word == 'remove':
                answer = answer + [word]
                index = index + 1
                word = words_list[index]
                word = right_keyword(word, [('line', 0.5, 'L511')])
                if word == "line":
                    case_0 = 7





        elif case_0 == 0:
            if case_1 == -1:
                word = right_keyword(word, variable_declaration)
                if word == "is":
                    case_1 = 0

            elif case_1 == 0:
                word = right_keyword(word, variable_type)
                if word == "operation":
                    case_0 = 6
                    case_1 = -1
                elif word in ['string', 'integer', 'float', 'list', 'Dictionary']:
                    case_1 = 1
            elif case_1 == 1:
                if word == "one":
                    word = 1
                elif word == 'too' or word == "to":
                    word = 2
                elif word == "tree" or word == "free":
                    word = 3
                elif word == 'for':
                    word = 4


        elif case_0 == 1:
            if case_1 == -1:
                word = right_keyword(word, parameters)
                if word == 'parameters':
                    case_1 = 0
            elif case_1 == 0:
                word = right_keyword(word, next_or_end_parameter)
                if word == 'end':
                    answer = answer + [word]
                    index = index + 1
                    word = words_list[index]
                    word = right_keyword(word, end_of)
                    if word != 'of':
                        answer = answer + [word]
                        pass
                    else:  # 'of' has been founded, now 'parameters' has to be found
                        answer = answer + [word]
                        index = index + 1
                        word = words_list[index]
                        word = right_keyword(word, parameters)
                        answer = answer + [word]
                        break

        elif case_0 == 2:
            if case_1 == -1:
                word = right_keyword(word, type_condition)
                if word in ['variable', 'string', 'integer', 'float']:
                    case_1 = 0

            elif case_1 == 0:
                word = right_keyword(word, compare)
                if word in ['equal', 'less', 'greater']:
                    case_1 = 1

            elif case_1 == 1:
                word = right_keyword(word, [('than', 0.7, 'T536')])
                if word == 'than':
                    case_1 = 2
                elif word == 'to':
                    case_1 = 3

            elif case_1 == 2:
                temp_word = right_keyword(word, [('or ', 0.5, 'O636')])
                if temp_word == 'or':
                    answer = answer + [word]
                    index = index + 1
                    word = words_list[index]
                    word = right_keyword(word, [('equal', 0.5, 'E245')])
                    if word == 'equal':
                        answer = answer + [word]
                        index = index + 1
                        word = words_list[index]
                        if word == 'to':
                            case_1 = 3
                else:
                    word = right_keyword(word, type_condition)
                    if word in ['variable', 'string', 'integer', 'float']:
                        case_1 = 4

            elif case_1 == 3:
                word = right_keyword(word, type_condition)
                if word in ['variable', 'string', 'integer', 'float']:
                    case_1 == 4

        elif case_0 == 3:
            word = right_keyword(word, [end_of_function[0]])
            if word == 'of':
                answer = answer + [word]
                index = index + 1
                word = words_list[index]
                word = right_keyword(word, [end_of_function[1]])

        elif case_0 == 4:
            if case_1 == -1:
                word = right_keyword(word, type_condition)
                case_1 = 0

        elif case_0 == 5:
            if case_1 == -1:
                word = right_keyword(word, parameters)
                if word == 'parameters':
                    case_1 = 0
            elif case_1 == 0:
                word = right_keyword(word, type_condition)
                if word == 'end':
                    answer = answer + [word]
                    index = index + 1
                    word = words_list[index]
                    word = right_keyword(word, end_of)
                    if word != 'of':
                        answer = answer + [word]
                        pass
                    else:  # 'of' has been founded, now 'parameters' has to be found
                        answer = answer + [word]
                        index = index + 1
                        word = words_list[index]
                        word = right_keyword(word, parameters)
                        answer = answer + [word]
                        break
                answer = answer + [word]
                index = index + 1
                word = words_list[index]
                word = right_keyword(word, next_or_end_parameter)

        elif case_0 == 6:
            if case_1 == -1:
                word = right_keyword(word, operation_type)
                if word == "at":
                    word = 'add'
                if word in ['add', 'subtract', 'multiply', 'divide']:
                    case_1 = 0
            elif case_1 == 0:
                word = right_keyword(word, math_var)
                if word in ['variable', 'string', 'integer', 'float', 'list']:
                    case_1 = 1
            elif case_1 == 1:
                word = right_keyword(word, operation_conjunction)

                if word == "one":
                    word = 1
                elif word == "tree" or word == "free":
                    word = 3
                elif word == 'for':
                    word = 4

                if word in ['from', 'by', 'to']:
                    case_1 = 2
            elif case_1 == 2:
                word = right_keyword(word, math_var)
                if word in ['variable', 'string', 'integer', 'float', 'list']:
                    case_1 = 3
            elif case_1 == 3:

                if word == "one":
                    word = 1
                elif word == "tree" or word == "free":
                    word = 3
                elif word == 'for':
                    word = 4


        index = index + 1
        answer = answer + [word]

    return answer


# print(keyword_recognition("function call x parameters string x end of parameters"))
