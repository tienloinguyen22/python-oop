import notebook
import sys

class Menu():
	def __init__(self):
		self.nb = notebook.Notebook()
		self.choices = {'1': self.show_notes,
						'2': self.search_notes,
						'3': self.add_notes,
						'4': self.modify_notes,
						'5': self.quit}

	def display(self):
		print('''
			1 - Show notes
			2 - Search notes
			3 - Add notes
			4 - Modify notes
			5 - Quit
			''')

	def run(self):
		while True:
			self.display()
			choice = input('What do U want to do ??\n')
			action = self.choices[choice]
			if action:
				action()
			else:
				print('Your request doesnt exist !!!!')

	def show_notes(self):
		if self.nb.notes:
			for note in self.nb.notes:
				print('ID: {0}, Memo: {1}, Tags: {2}, Create: {3}'.format(note.id, note.memo, note.tags, note.create_date))
		else:
			print('U dont have any note')

	def search_notes(self):
		search_value = input('Enter some keywords: ')
		result = self.nb.search(search_value)
		if result:
			for item in result:
				print('ID: {0}, Memo: {1}, Tags: {2}, Create: {3}'.format(item.id, item.memo, item.tags, item.create_date))
		else:
			print('Nothing match :(')

	def add_notes(self):
		memo = input('Enter memo: ')
		tags = input('Tags: ')
		self.nb.new_note(memo, tags)
		print('Your new memo has been added successfully :D')

	def modify_notes(self):
		id = input('Enter note ID: ')
		new_memo = input('Enter new memo: ')
		new_tags = input('Enter new tags: ')
		if new_memo:
			self.nb.modify_memo(id, new_memo)
		if new_tags:
			self.nb.modify_tags(id, new_tags)
		print('Modify successfully :D')

	def quit(self):
		print("Thank you for using your notebook today.")
		sys.exit(0)

if __name__ == "__main__":
	Menu().run()

