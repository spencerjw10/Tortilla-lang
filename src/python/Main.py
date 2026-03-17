from Lexer import tokenize
import AST

code = '''
int jim = tom(10)
forEach i in 77:
end
i += [1, 2, 3]
int bob[0] -= timmothy.rad
'''
tokens = tokenize(code)
tree = AST.Parse(AST.i, tokens, AST.states)
print(tree.parsePrgm())