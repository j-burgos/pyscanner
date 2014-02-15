from structs import Token

lang_name = 'Javascript'

whitespace = ["\t", "\r"]

lexic = { 

	# regexp for line comments and block comments
	'comment'	: Token("\\/\\/.*|\\/\\*(.|[\r\n])*?\\*\\/",	"COMMENTTOKEN",	is_regexp=True) ,

	# regexp for strings
	'string'	: Token("\"(.|[\r\n])*?\"|\'(.|[\r\n])*?\'",	"STRINGTOKEN",	is_regexp=True) ,

	'identifier'	: Token("[\$|a-zA-Z|_]([0-9|a-zA-Z|_|\$])*","IDENTIFIERTOKEN"		,is_regexp=True) ,
	'real' 			: Token("[0-9]+\.[0-9]+",					"REALTOKEN"			,is_regexp=True) ,
	'integer'		: Token("[0-9]+",							"INTEGERTOKEN"			,is_regexp=True) ,
	
	'keywords'	: [ Token("break", 		"BREAKTOKEN"),
					Token("case", 		"CASETOKEN"),
					Token("catch", 		"CATCHTOKEN"),
					Token("continue", 	"CONTINUETOKEN"),
					Token("default", 	"DEFAULTTOKEN"),
					Token("delete", 	"DELETETOKEN"),
					Token("do", 		"DOTOKEN"),
					Token("else", 		"ELSETOKEN"),
					Token("for", 		"FORTOKEN"),
					Token("finally", 	"FINALLYTOKEN"),
					Token("function", 	"FUNCTIONTOKEN"),
					Token("if", 		"IFTOKEN"),
					Token("in", 		"INTOKEN"),
					Token("instanceof", "INSTANCEOFTOKEN"),
					Token("new", 		"NEWTOKEN"),
					Token("return", 	"RETURNTOKEN"),
					Token("switch", 	"SWITCHTOKEN"),
					Token("this", 		"THISTOKEN"),
					Token("throw", 		"THROWTOKEN"),
					Token("try", 		"TRYTOKEN"),
					Token("typeof", 	"TYPEOFTOKEN"),
					Token("var",		"VARTOKEN") ,
					Token("void", 		"VOIDTOKEN"),
					Token("while", 		"WHILETOKEN"),
					Token("with", 		"WITHTOKEN") ] ,

	'symbols' 	: [ Token("++",			"INCREMENTTOKEN"),
					Token("--",			"DECREMENTTOKEN"),
					Token("+",			"ADDTOKEN"),
					Token("-",			"SUBSTRACTTOKEN"),
					Token("*",			"MULTIPLYTOKEN"),
					Token("/",			"DIVIDETOKEN"),
					Token("%",			"MODULETOKEN"),
					Token("?",			"CONDITIONALTOKEN"),
					Token("<=",			"LESSEQUALTOKEN"),
					Token(">=",			"GREATEREQUALTOKEN"),
					Token("<",			"LESSTOKEN"),
					Token(">",			"GREATERTOKEN"),
					Token("===",		"STRICTCOMPARETOKEN"),
					Token("==",			"COMPARETOKEN"),
					Token("=",			"ASIGNATIONTOKEN"),
					Token("!=",			"NOTEQUALTOKEN"),
					Token("&&",			"ANDTOKEN"),
					Token("||",			"ORTOKEN"),
					Token("{",			"OPENCURLYBRACKETTOKEN"), 
					Token("}",			"CLOSECURLYBRACKETTOKEN"),
					Token("(",			"OPENPARENTHESISTOKEN"),
					Token(")",			"CLOSEPARENTHESISTOKEN"),
					Token("[",			"OPENSQUAREBRACKETTOKEN"),
					Token("]",			"CLOSESQUAREBRACKETTOKEN"),
					Token(".",			"DOTTOKEN"),
					Token(",",			"COMATOKEN"),
					Token(":",			"COLONTOKEN"),
					Token(";",			"SEMICOLONTOKEN") ],

}
