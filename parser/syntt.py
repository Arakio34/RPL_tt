# Yacc example
import sys

import ply.yacc as yacc
import lextt


class parsertt(object):

	def __init__(self, lexer = None, debug = False, **kwargs):

		if not lexer:
			self._lexer = lextt.lexertt()
		else:
			self._lexer = lexer

		self.tokens = self._lexer.tokens
		self._parser = yacc.yacc(module = self, debug = debug, **kwargs)
		self._debug = debug
		self._IT = {} # IT = Identification Table

	def p_operator(self,p):
		'''expression : expression PLUS term
		 	      | expression MINUS term
		 	      | expression EQUAL term
			      | STRING
			      | term
   		         term : term TIMES factor
		              | term DIVIDE factor
			      | factor
			print : PRINT
		      	      | PRINT expression 
		              | PRINT factor 
		              | PRINT NUMBER '''
		n=0
		for i in p:
			print('p['+str(n)+']=' + str(i))
			n=n+1
		if p[1] == 'print':
			if p[2] is str: 
				print(self._IT[p[2]])
			else:
				print(p[2])
		elif len(p) == 2:
			if p[1] is str:
				self._IT[p[1]] = None
			else:
				p[0] = p[1]
		elif p[2] == '=':
			self._IT[p[1]] = p[3]
		elif p[2] == '+':
			p[0] = p[1] + p[3]
		elif p[2] == '-':
			p[0] = p[1] - p[3]
		elif p[2] == '*':
			p[0] = p[1] * p[3]
		elif p[2] == '/':
			p[0] = p[1] / p[3]


	def p_factor_num(self,p):
		'factor : NUMBER'
		p[0] = p[1]

	def p_factor_expr(self,p):
		'factor : LPAREN expression RPAREN'
		p[0] = p[2]

	def p_error(self,p):
		print("Syntax error in input!")
		print(p)



if __name__=="__main__":

	parser = parsertt()
	path = 'code'
	with open(path) as f:
		for l in f:
			result = parser._parser.parse(l)
