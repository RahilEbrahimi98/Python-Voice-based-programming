#save the file in this path before running : "C:/Users/NAME/AppData/Roaming/Sublime Text 3/Packages/User"
import sublime
import sublime_plugin


class myCommand(sublime_plugin.TextCommand):
	def run(self , edit):
		f = open("C:/Users/Rahil/AppData/Roaming/Sublime Text 3/Packages/User/myFile.txt", "a")
		f.write("Hi \n")
		f.close()
		f = open("C:/Users/Rahil/AppData/Roaming/Sublime Text 3/Packages/User/myFile.txt", "r")
		text = f.read()
		print(text)
		

