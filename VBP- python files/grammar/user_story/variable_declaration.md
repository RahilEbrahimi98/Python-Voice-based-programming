# Variable Declaration
### Overall Format:
In order to declare any variable in python, user has to say the following format:

    variable {name_of_the_variable} is {type_of_the_variable} {value_of_the_variable}

 for example:

    variable my name is string sina

and the code which will be generated is:

    my_name = 'sina'

### Descriptions:
the name of the variable will be generated in `snake_case` format, based on the PEP-8 convention.
For the type of the variable, 6 options are available:

|Type of The Variable| Keyword    |
|--------------------|------------|
| Integer Number     | integer    |
| Floating Number    | float      |
| Strings            | string     |
| Lists              | list       |
| Dictionaries       | Dictionary |
| Variable           | variable   |

And the format of the value of the variable is dependent on the type of the variable:

 - **Integer Number:**
 The user has to say the number, exactly.
  - **Floating Number**:
 At first, the user has to say the integer part of the number, and after that, for separating the integer part from the decimal part, the word *point* has to be said by the user, and finally the decimal part.
  - **Strings**:
 The exact string has to be said, word by word. If there is a number in the string, the number will be interpreted as digits, but if you want to use letters instead of digits, the word *letters* has to be said.
  - **Lists**:
 In this case, the user has to say the type of the variable in the list and the value of that and after that, if he/she wants to add other variables, the word *next* has to be said, and at last the words *end of list* has to be said.
  - **Dictionaries**:
 Finally, the user has to say the key and the value, respectively, with the type of them, if he/she wants to add other variables, the word *then* has to be said, and at last the words *end of dictionary* has to be said.
  - **variables**:
 If user wants to set a variable equal to another variable, user has to say the exact name of the second variable.
### Examples:
 - **Integer Number:**
```
Input:
variable my integer number is integer 22
Output:
my_integer_number = 22
```
 - **Floating Number:**
```
Input:
variable my floating number is float 7 point 56
Output:
my_floating_number = 7.56
```
 - **Strings:**
```
Input:
variable my first string is string my name is sina
Output:
my_first_string = 'my name is sina'
```
```
Input:
variable my second string is string consider the number 42
Output:
my_second_string = 'consider the number 42'
```
```
Input:
variable my third string is string consider the number letters 42
Output:
my_third_string = 'consider the number forty-two'
```
 - **Lists:**
```
Input:
variable my list is list integer 5 next float 4 point 6 next string sina end of list
Output:
my_list = [5, 4.6, 'sina']
```
 - **Dictionaries:**
```
Input:
variable my dictionary is dictionary string age integer 21 then float 3 point 6 list string sina next integer 5 end of list end of dictionary
Output:
my_dictionary = {'age': 21, 3.6: ['sina', 5]}
```
 - **Variables:**
```
Input:
variable my first variable is variable my second variable
Output:
my_first_variable = my_second_variable
```
