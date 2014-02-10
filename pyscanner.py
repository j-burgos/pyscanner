#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import lang
import re

print "Scanner de Javascript v0.1 \n"

if len(sys.argv) < 2:
	print "Modo de uso: python pyscanner.py <ruta_archivo>"
	exit()
else:
	pass

tokens_validos = []

definiciones = [obj for obj in (lang.lexico.get(definicion) for definicion in lang.lexico)]
for definicion in definiciones:
	if type(definicion) is list:
		tokens = [token for token in definicion]
		for token in tokens:
			tokens_validos.append(token)
	else:
		tokens_validos.append(definicion)

validos_regexp = re.compile("|".join([token.regexpstr for token in tokens_validos])) 
		
try:
	with open(sys.argv[1],'r') as archivo:
		texto = archivo.readlines()
		codigo = "".join(texto)
		for blanco in lang.blancos:
			codigo = codigo.strip().replace(blanco,"")

		#print [token.regexpstr for token in tokens_validos]
		for match in validos_regexp.finditer(codigo):
			lexema = match.group(0)
			#print match.group()
			for definicion in tokens_validos:
				if definicion.regexp.match(lexema):
					print lexema + " -> " + definicion.token
					break

except IOError as e:
	print "ERROR: No se pudo encontrar o abrir el archivo: {}".format(sys.argv[0])
	exit()
except Exception as e:
	print "ERROR: Ocurrio un problema inesperado: {}".format(repr(e))
	exit()