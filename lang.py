from structs import Token

blancos = ["\t", "\r"]


lexico = { \

	'comentario'			: Token("\\/\\*.*\\*\\/"			,"COMENTARIOTOKEN"		,is_regexp=True) ,
	'cadena'				: Token("[\'|\"].*[\'|\"]"			,"CADENATOKEN"			,is_regexp=True) ,
	
	'palabras_reservadas'	: [ Token("catch", 		"CATCHTOKEN", True),
						Token("function", 	"FUNCTIONTOKEN", True),
						Token("try", 		"TRYTOKEN", True),
						Token("var",		"VARTOKEN", True) ] ,

	'simbolos_especiales' : [ Token("++",			"INCREMENTOTOKEN"),
						Token("--",			"DECREMENTOTOKEN"),
						Token("+",			"MASTOKEN"),
						Token("-",			"MENOSTOKEN"),
						Token("*",			"MULTIPLICACIONTOKEN"),
						Token("/",			"DIVISIONTOKEN"),
						Token("<=",			"MENORIGUALTOKEN"),
						Token(">=",			"MAYORIGUALTOKEN"),
						Token("<",			"MENORQUETOKEN"),
						Token(">",			"MAYORQUETOKEN"),
						Token("===",		"COMPARACIONCOMPLETATOKEN"),
						Token("==",			"COMPARACIONTOKEN"),
						Token("=",			"ASIGNACIONTOKEN"),
						Token("!=",			"DIFERENTETOKEN"),
						Token("&&",			"ANDTOKEN"),
						Token("||",			"ORTOKEN"),
						Token("{",			"LLAVEABIERTATOKEN"), 
						Token("}",			"LLAVECERRADATOKEN"),
						Token("(",			"PARENABIERTOTOKEN"),
						Token(")",			"PARENCERRADOTOKEN"),
						Token("[",			"CORCHETEABIERTOTOKEN"),
						Token("]",			"CORCHETECERRADOTOKEN"),
						Token(".",			"PUNTOTOKEN"),
						Token(",",			"COMATOKEN"),
						Token(";",			"PUNTOYCOMATOKEN") ],
	
	'identificador'	: Token("[a-zA-Z]([a-zA-Z0-9|_]*)"	,"IDENTIFICADORTOKEN"	,is_regexp=True) ,
	'real' 			: Token("[0-9]+\.[0-9]+"			,"REALTOKEN"			,is_regexp=True) ,
	'entero'		: Token("[0-9]+"					,"ENTEROTOKEN"			,is_regexp=True) 
}
