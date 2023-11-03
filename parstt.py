import ply.yacc as yacc

def p_expression_plus(p):
	'expression : expression plus term'
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
			
