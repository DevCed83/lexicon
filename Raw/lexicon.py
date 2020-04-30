import tkinter as tk
import time
#from database import Database
#import sqlite3

class Gui(tk.Tk):
	"""docstring for Gui"""
	def __init__(self):
		super(Gui, self).__init__()
		# self.database = Database()
		# self.current_idiom = self.database.get_random()
		self.idiom = tk.StringVar(self)#.set(current_idiom['idiom'])
		self.idiom.set("test")
		self.idiom_label= tk.Label(self, textvariable = self.idiom)
		self.idiom_label.pack()
		self.entry = tk.Entry(self, text = 'Your answer is :')
		self.entry.pack()
		self.button_text = tk.StringVar(self)
		self.button_text.set('Valider')
		self.validate_button = tk.Button(self, textvariable = self.button_text, command = self.verify_answer)
		self.validate_button.pack()
		self.add_idiom_button = tk.Button(self, text = 'Add idiom', command = self.add_entry)
		self.add_idiom_button.pack()

	def verify_answer(self):
		
		
	def add_entry(self):
		print ('adding entry')

if __name__ == "__main__":
	gui = Gui()
	gui.mainloop()