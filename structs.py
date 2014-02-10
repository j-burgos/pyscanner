import re

class Token:
	def __init__(self, lexema, token, is_regexp = False):
		if is_regexp:
			self.regexpstr = lexema
		else:
			self.regexpstr = "".join(["\\" + char for char in list(lexema)])
		self.lexema = lexema
		self.token = token
		self.regexp = re.compile(self.regexpstr)

	def __str__(self):
		return "{},{}".format(self.lexema, self.token)
	def __repr__(self):
		return "Lexema:{} | Token:{}".format(self.lexema, self.token)
