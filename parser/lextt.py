import ply.lex as lex
import sys
import ply.yacc as yacc

class lexertt(object):

	tokens = (
		'NUMBER',
		'ID',
		'PLUS',
		'MINUS',
		'TIMES',
		'DIVIDE',
		'LPAREN',
		'RPAREN',
	)
	reserved = ( 'for', 'if', 'while', 'else')

	t_ignore  = ' \t'

	t_PLUS    = r'\+'
	t_MINUS   = r'-'
	t_TIMES   = r'\*'
	t_DIVIDE  = r'/'
	t_LPAREN  = r'\('
	t_RPAREN  = r'\)'


	def __init__(self,**kwargs):
		self._lexer = lex.lex(module=self,**kwargs)
		self._symbol_table = {}

	def t_NUMBER(self,t):
		r'\d+'
		t.value = int(t.value)    
		return t

	def t_ID(self,t):
		r'[a-zA-Z][a-zA-Z_0-9]*\s'
		if t.value in self.reserved:
			t.type = self.reserved[t.value]
		else:
			t.type =  "ID"
		return t


	def t_newline(self,t):
		r'\n+'
		t.lexer.lineno += len(t.value)


	def t_error(self,t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

	def tokenize(self,data):
		token_list = []
		self._lexer.input(data)
		while True:
			tok = self._lexer.token()
			
			if not tok:
				break
			token_list.append(tok)
		return token_list

if __name__ == "__main__":
	data = '''
	3 + 4 * 10
	  + -20 *2
	a = 2
	'''
	lexer = lexertt()
	tokenL=lexer.tokenize(data)
	print(tokenL)

	
