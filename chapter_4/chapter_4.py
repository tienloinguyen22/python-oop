import hashlib


class User():
	def __init__(self, username, pw):
		self.username = username
		self.password = self._encrypt_pw(pw)
		self.is_logged_in = False

	def _encrypt_pw(self, pw):
		hash_string = (self.username + pw)
		hash_string = hash_string.encode("utf8")
		return hashlib.sha256(hash_string).hexdigest()

	def check_valid_pw(self, pw):
		encrypt = self._encrypt_pw(pw)
		return encrypt == self.password

class AuthException(Exception):
	def __init__(self, username, user=None):
		self.username = username
		self.user = user


#Define all the Exception class
class UsernameAlreadyExist(AuthException):
	pass

class PasswordTooShort(AuthException):
	pass

class InvalidInformation(AuthException):
	pass

class PermissionError(Exception):
	pass

class NotLoggedInError(AuthException):
	pass

class NotPermittedError(AuthException):
	pass


#Back to the workflow :D
class Authenticator():
	def __init__(self):
		self.users = {}

	def add_user(self, username, pw):
		if username in self.users.keys():
			raise UsernameAlreadyExist('This username has already exist. Pls choose another one !!!')
		if len(pw) < 6:
			raise PasswordTooShort('Your password is too short. Password need to be at least 6 chars !!!')
		menu.m.run()
		self.users[username] = User(username, pw)
		print('Create new user successfully :D')

	def log_in(self, username, pw):
		if username not in self.users.keys():
			raise InvalidInformation('Invalid username !!')
		if not self.users[username].check_valid_pw(pw):
			raise InvalidInformation('Invalid password !!!')
		self.users[username].is_logged_in = True
		print('Log in successfully !!!')

class Authorizor():
	def __init__(self, authenticator=None):
		self.authenticator = authenticator
		self.permission_list = {}

	def add_permission(self, permission):
		if permission in self.permission_list.keys():
			raise PermissionError('Permission already exist !!!')
		else:
			self.permission_list[permission] = set()
		print('Add permission successfully !!!')

	def give_permission(self, permission, username):
		if permission not in self.permission_list.keys():
			raise PermissionError('This permission doesnt exist !!!')
		if username not in self.authenticator.users.keys():
			raise InvalidInformation('This username doesnt exist !!!')
		self.permission_list[permission].add(username)
		print('Grant permission successfully !!!')

	def check_permission(self, username, permission):
		if self.authenticator.users[username].is_logged_in == False:
			raise NotLoggedInError('This username hasnt log in in yet !!!')
		if username not in self.permission_list[permission]:
			raise NotPermittedError('Username {} hasnt been given {} permission !!!'.format(username, permission))
		print('Username {} has been given {} permission !!!'.format(username, permission))

auth = Authenticator()
authorizor = Authorizor(auth)
import menu







