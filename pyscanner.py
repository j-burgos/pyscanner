#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import config
import lang
import re

print "PyScanner v0.2 \n"

if len(sys.argv) < 2:
	print "Usage: python pyscanner.py <filepath> \n"
	exit()

print "Running analysis for language: {} \n".format(lang.lang_name)

lexic = lang.lexic
filepath = sys.argv[1]

valid_tokens = []

rules = [rule for rule in (lexic.get(definition) for definition in lexic)]
for rule in rules:
	if type(rule) is list:
		tokens = [token for token in rule]
		for token in tokens:
			valid_tokens.append(token)
	else:
		valid_tokens.append(rule)

valid_regexps = [token.regexpstr for token in valid_tokens]
valid_regexp = "|".join(valid_regexps)
invalid_regexp = "(?! " + valid_regexp + ")"
all_regexp = re.compile( "[\n|\r|\r\n|\s]|" + "|".join([valid_regexp, invalid_regexp]))
		
try:
	with open(filepath,'r') as filestream:
		text = filestream.readlines()
		code = "".join(text)

		for match in all_regexp.finditer(code):
			lexem = match.group(0)
			
			if lexem == "" and match.start() != len(code):
				print "Null token: {}".format(code[match.start()])

			for rule in valid_tokens:
				if rule.regexp.match(lexem):
					if config.TOKENIZE_COMMENTS == False and rule.token == "COMMENTTOKEN":
						break	
					else:
						print "{} -> {}".format(lexem.replace("\n",""),rule.token)
						break

except IOError as e:
	print "ERROR: Could not find or open the file: {}".format(sys.argv[0])
	exit()

except Exception as e:
	print "ERROR: Unexpected error: {}".format(repr(e))
	exit()