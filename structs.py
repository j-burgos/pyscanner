import re

class Token:
	def __init__(self, lexem, token, is_regexp = False):
		if is_regexp:
			self.regexpstr = lexem
		else:
			# It is a keyword
			if re.match("^\w+$",lexem):
				self.regexpstr = "^" + re.escape(lexem) + "$"
			# It is an especial symbol
			else:
				self.regexpstr = re.escape(lexem)

			#print self.regexpstr

		self.lexema = lexem
		self.token = token
		self.regexp = re.compile(self.regexpstr)

	def __str__(self):
		return "{},{}".format(self.lexema, self.token)

	def __repr__(self):
		return "Lexema:{} | Token:{}".format(self.lexema, self.token)
