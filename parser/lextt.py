import ply.lex as lex
from ply.lex import TOKEN 
import sys
import ply.yacc as yacc

class lexertt(object):

	tokens = (
		'NUMBER',
		'EQUAL',
		'PRINT',
		'STRING',
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
	t_EQUAL  = r'\='
	t_PRINT  = r'print'
	
	nondigit         = r'([_A-Za-z]+)'


	def __init__(self,**kwargs):
		self._lexer = lex.lex(module=self,**kwargs)
		self._symbol_table = {}

	def t_NUMBER(self,t):
		r'\d+'
		t.value = int(t.value)    
		return t

	def t_whitespace(self,t):
		r'\s+'
		pass

	@TOKEN(nondigit)
	def t_STRING(self,t):
		t.type="STRING"
		t.value= str(t.value)
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
	a = 2
	'''
	lexer = lexertt()
	tokenL=lexer.tokenize(data)
	print(tokenL)

	
