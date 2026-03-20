from Lexer import tokenize
import AST

code = '''
func john () null {tomm}
bill{joe,}
'''
tokens = tokenize(code)
tree = Semantic.Parse(Semantic.i, tokens, Semantic.states)
#tree = Semantic.Parse(Semantic.i, tokens, Semantic.states)