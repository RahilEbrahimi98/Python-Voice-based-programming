

## sublime plugin report
			    
 In sublime text 3 we can create a plugin using this path:  
  

    tools>>developer>>new plugin

Then we just need to write our code in `run(self , edit)` function which is itself in `ExampleCommand(sublime_plugin.TextCommand)` class by default. Finally you can run the code using `view.run_command('example')` command. Instead of "example" you can write whatever your class name is but use it starting with  lowercase. If like the example above, there is "Command" prefix in the class name, don't write that :  
  

    Class_nameCommand -> view.run_command('class_name')

