from Lexer import tokenize
import AST

code = '''
func john () null {tomm}
bill{joe,}
'''
tokens = tokenize(code)
tree = AST.Parse(AST.i, tokens, AST.states)
