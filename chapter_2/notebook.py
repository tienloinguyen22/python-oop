import datetime

id = 0
class Note():
	def __init__(self, memo, tags=''):
		global id
		id += 1
		self.id = id
		self.memo = memo
		self.tags = tags
		self.create_date = datetime.datetime.today()

	def match(self, search_value):
		if search_value in self.memo or search_value in self.tags:
			return True
		else:
			return False

class Notebook:
	def __init__(self):
		self.notes = []

	def search(self, search_value):
		return [note for note in self.notes if note.match(search_value)]

	def new_note(self, memo, tags=''):
		newnote = Note(memo, tags)
		self.notes.append(newnote)

	def modify_memo(self, id, new_memo):
		for note in self.notes:
			if str(note.id) == str(id):
				note.memo = new_memo
				break

	def modify_tags(self, id, new_tags):
		for note in self.notes:
			if str(note.id) == str(id):
				note.tags = new_tags
				break


		

