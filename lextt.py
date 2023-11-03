import ply.lex as lex
import ply.yacc as yacc


tokens = (
####'FILTER',
####'SOURCE',
####'TARGET',
	'ASSIGNEMENT',
	'NUMBER',
	'ID',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LPAREN',
	'RPAREN',
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ASSIGNEMENT = r'\='

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)    
	return t

def t_ID(t):
	r'[a-z]+\s*'
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()

data = '''
3 + 4 * 10
a= 21
b=12
+ -20 *2
'''

lexer.input(data)



def p_expression_plus(p):
	'expression : expression PLUS term'
	p[0] = p[1] + p[3]


parser = yacc.yacc()

while True:
	try:
		s = raw_input('calc > ')
	except EOFError:
		break
	if not s: continue
	result = parser.parse(s)
	print(result)
			












