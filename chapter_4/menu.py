import sys
import chapter_4

class ActionError(Exception):
	pass

class Menu():
	def __init__(self):
		self.authenticator = chapter_4.auth
		self.authorizor = chapter_4.authorizor
		self.choices = {'1':self.add_user,
						'2':self.log_in,
						'3':self.add_per,
						'4':self.give_per,
						'5':self.check,
						'6':self.quit}

	def display(self):
		print('===========================')
		print('''
			1 - Add User
			2 - Log in
			3 - Add permission
			4 - Give permission
			5 - Check permission
			6 - Quit
			''')

	def run(self):
		while True:
			self.display()
			action = input('What do U wanna do ?? ')
			if not self.choices[action]:
				raise ActionError('Action doesnt exist !!!')
			else:
				self.choices[action]()

	def add_user(self):
		username = input('User name: ')
		pw = input('Password: ')
		self.authenticator.add_user(username, pw)

	def log_in(self):
		username = input('User name: ')
		pw = input('Password: ')
		self.authenticator.log_in(username, pw)

	def add_per(self):
		permission = input('Permission: ')
		self.authorizor.add_permission(permission)

	def give_per(self):
		permission = input('Permission: ')
		username = input('User name: ')
		self.authorzor.give_permission(permission, username)

	def check(self):
		permission = input('Permission: ')
		username = input('User name: ')
		self.authorzor.check_permission(username, permission)

	def quit(self):
		print('Thank U :)')
		sys.exit(0)


m = Menu()
if __name__ == '__main__':
	m.run()








