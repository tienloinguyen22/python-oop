class Document():
	def __init__(self):
		self.characters = []
		self.current_pos = 0
		self.filename = ''

	def forward(self):
		self.current_pos += 1

	def back(self):
		self.current_pos -= 1

	def home(self):
		if self.current_pos == len(self.characters):
			self.current_pos -= 1
		while self.characters[self.current_pos] != '\n':
			self.current_pos -= 1
			if self.current_pos == 0:
				break

	def end(self):
		while self.characters[self.current_pos] != '\n':
			self.current_pos += 1
			if self.current_pos >= len(self.characters):
				break



	@property
	def string(self):
		return ''.join(str(item) for item in self.characters)

	def insert(self, character):
		if isinstance(character, Character):
			self.characters.insert(self.current_pos, character)
			self.current_pos += 1
		else:
			self.characters.insert(self.current_pos, Character(character))
			self.current_pos += 1

	def delete(self):
		self.characters.remove(self.characters[self.current_pos-1])
		self.current_pos -= 1

	def save(self):
		with open(filename, 'w') as f:
			content = ''.join(str(item) for item in self.characters)
			


class Character():
	def __init__(self, character, bold=False, italic=False, underline=False):
		self.character = character
		self.bold = bold
		self.italic = italic
		self.underline = underline

	def __str__(self):
		b = '*' if self.bold else ''
		i = '/' if self.italic else ''
		u = '_' if self.underline else ''
		return b + i + u + self.character




