# Function Definition
### Overall Format:
In order to define any function in python, user has to say the following format:

    define function {name_of_the_function} parameters {name_of_the_parameters} end of parameters
    
 and also between every parameter, the user has to say `next`. 
 for example:

    define function hello world parameters name end of parameters

and the code which will be generated is:

    def hello_world(name):

and after that, the body of the function should be defined. Finally, when the function is finished, the user has to say
`end of function`.

when the function is finished, just before `end of function` keyword, user can return a static or dynamic variable with
the command below:
if he/she wants to return static variable, he/she has to say:

    return {type of variable} {value of that}
    
for example:

    return string hello world
    
and the output will be:

    return 'hello world'
    
and, finally, he/she wants to return dynamic variable, he/she has to say:

    return variable {name of variable}
    
for example:

    return variable hello world
    
and the output will be:

    return hello_world
    
for function calls, user has to follow the format below:
    
    function call {name_of_the_function} parameters {type_of_variable} {name_of_the_parameters} end of parameters
    
and also between every parameter, the user has to say `next`. 
 for example:

    function call hello world parameters variable name end of parameters

and the code which will be generated is:

    hello_world(name)
    
another example:

    function call hello world parameters string name end of parameters

and the code which will be generated is:

    hello_world('name')