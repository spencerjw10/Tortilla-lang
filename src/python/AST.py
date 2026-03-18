#AST
i = 0
states = []
BPChart = {
        'Assign':   10, 'PlusEql':  10, 'MinusEql': 10, 'TimesEql': 10, 'DivideEql': 10, 'ModEql': 10, 'Inc': 10, 'Dec': 10,
        'and': 20, 'or': 20, 'nor': 20, 'xor': 20,
        'is':  30, 'Less': 30, 'More': 30, 'Lte': 30, 'Gte': 30, 'in':  30, 'has': 30,
        'BitAnd':   40, 'BitOr': 40, 'BitXor': 40,
        'Shl':  50, 'Shr': 50,
        'Plus':   60, 'Minus': 60,
        'Times':   70, 'Divide': 70, 'Mod': 70,
        'Power':  80,
        'Point':   100, 'Lbrc': 100, 'Lpar': 100
    }
DT = [
    "int", "bigInt", "float", "doub", "char", "bool", "str", "array", "dict", "set", "type"
]

class Node:
        def __init__(self, lin, colum):
            self.line = lin
            self.col = colum

class UnOpNode(Node):
        def __init__(self, op, expr, lin, colum):
            super().__init__(lin, colum)
            self.op = op
            self.expr = expr
class BinOpNode(Node):
        def __init__(self, left, op, right, lin, colum):
            super().__init__(lin, colum)
            self.left = left
            self.op = op
            self.right = right
class IntNode(Node):
        def __init__(self, val, lin, colum):
            super().__init__(lin, colum)
            self.val = val
class FloatNode(Node):
        def __init__(self, val, lin, colum):
            super().__init__(lin, colum)
            self.val = val
class StrNode(Node):
        def __init__(self, val, lin, colum):
            super().__init__(lin, colum)
            self.val = val
class BoolNode(Node):
        def __init__(self, val, lin, colum):
            super().__init__(lin, colum)
            self.val = val
class VarNode(Node):
        def __init__(self, name, extra, lin, colum):
            super().__init__(lin, colum)
            self.name = name
            self.extra = extra
class AccNode(Node):
        def __init__(self, kind, val, lin, colum):
            super().__init__(lin, colum)
            self.kind = kind
            self.val = val
class GroupNode(Node):
        def __init__(self, expr, lin, colum):
            super().__init__(lin, colum)
            self.expr = expr
class WhileNode(Node):
        def __init__(self, expr, block, lin, colum):
            super().__init__(lin, colum)
            self.expr = expr
            self.block = block
class ForNode(Node):
        def __init__(self, init, condition, inc, block, lin, colum):
            super().__init__(lin, colum)
            self.init = init
            self.condition = condition
            self.inc = inc
            self.block = block
class ForENode(Node):
        def __init__(self, var, expr, block, lin, colum):
            super().__init__(lin, colum)
            self.var = var
            self.expr = expr
            self.block = block
class IfelNode(Node):
        def __init__(self, expr, block, after, lin, colum):
            super().__init__(lin, colum)
            self.expr = expr
            self.block = block
            self.after = after
class SwitchNode(Node):
        def __init__(self, expr, cases, lin, colum):
            super().__init__(lin, colum)
            self.expr = expr
            self.cases = cases
class CaseNode(Node):
        def __init__(self, expr, also, block, after, lin, colum):
            super().__init__(lin, colum)
            self.expr = expr
            self.also = also
            self.block = block
            self.after = after
class ListNode(Node):
    def __init__(self, kind, val, lin, colum, keys=None):
        super().__init__(lin, colum)
        self.kind = kind
        self.val = val
        self.keys = keys
class AssignNode(Node):
        def __init__(self, kind, val, lin, colum):
            super().__init__(lin, colum)
            self.kind = kind
            self.val = val
class ArgsNode(Node):
    def __init__(self, args, lin, colum):
        super().__init__(lin, colum)
        self.args = args
class FuncNode(Node):
    def __init__(self, kind, concur, name, args, code, returnDataType, lin, colum):
        super().__init__(lin, colum)
        self.kind = kind
        self.concur = concur
        self.name = name
        self.args = args
        self.code = code
        self.returnDataType = returnDataType
class CallNode(Node):
    def __init__(self, name, types, args, lin, colum):
        super().__init__(lin, colum)
        self.name = name
        self.types = types
        self.args = args
class AwaitNode(Node):
    def __init__(self, vals, lin, colum):
        super().__init__(lin, colum)
        self.vals = vals
class ImportNode(Node):
    def __init__(self, vals, lin, colum):
        super().__init__(lin, colum)
        self.vals = vals

class Parse():
    def __init__(self, i, tokens, states):
        self.tokens = tokens
        self.i = 0
        self.states = []

    def peek(self):
        if self.i == len(self.tokens):
            return None
        return self.tokens[self.i]
    def consume(self):
        self.i += 1
        if self.i - 1 == len(self.tokens):
            return None
        return self.tokens[self. i - 1]
    def expect(self, val):
        if self.i == len(self.tokens):
            return None
        if self.tokens[self.i].val != val:
            return None
        return self.consume()
    def pratt(self, minBP):
        tok = self.consume()
        left = 0
        if tok.kind == "Int":
            left = IntNode(tok.val, tok.line, tok.col)
        elif tok.kind == "Float":
            left = FloatNode(tok.val, tok.line, tok.col)
        elif tok.kind == "Str":
            left = StrNode(tok.val, tok.line, tok.col)
        elif tok.kind == "Bool":
            left = BoolNode(tok.val, tok.line, tok.col)
        elif tok.kind == "Variable":
            left = self.parseVar()
        elif tok.val in ("not", "BitNot", "Minus"):
            right = self.pratt(90)
            left = UnOpNode(tok.val, right, tok.line, tok.col)
        elif tok.val == "Lpar":
            elems = []
            commas = False
            while True:
                elems.append(self.pratt(0))
                if self.peek() and (self.peek().val == "Rpar"):
                    self.consume()
                    break
                commas = True
                self.consume()
            if commas == False:
                left = GroupNode(elems[0], tok.line, tok.col)
            else:
                left = ListNode("Set", elems, tok.line, tok.col)
        elif tok.val == "Lbrc":
            elems = []
            while True:
                elems.append(self.pratt(0))
                if self.peek() and (self.peek().val == "Rbrc"):
                    self.consume()
                    break
                self.consume()
            left = ListNode("Array", elems, tok.line, tok.col)
        elif tok.val == "Lbrkt":
            elems = []
            keys = []
            while True:
                elems.append(self.pratt(0))
                if self.peek() and (self.peek().val == "Rbrkt"):
                    self.consume()
                    break
                if self.peek() and (self.peek().val == "Then"):
                    self.consume()
                    keys.append(self.pratt(0))
                else:
                    keys.append(0)
                self.consume()
            left = ListNode("Dict", elems, tok.line, tok.col, keys)
        while True:
            op = self.peek()
            if op is None or op.val not in BPChart:
                break
            bp = BPChart[op.val]
            if bp <= minBP:
                break
            self.consume()
            right = self.pratt(bp)
            left = BinOpNode(left, op.val, right, op.line, op.col)
        return left
    '''
    Import > import + Var [+ from + Var]
    '''
    def parsePrgm(self):
        while self.i < len(self.tokens):
            self.states.append(self.parseState())
        return self.states
    def parseState(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        if self.tokens[self.i].val == 'if':
            self.i += 1
            return self.parseIfel()
        if self.tokens[self.i].val == 'switch':
            self.i += 1
            return self.parseSwitch()
        if self.tokens[self.i].val == 'while':
            self.i += 1
            return self.parseWhile()
        if self.tokens[self.i].val == 'for':
            self.i += 1
            return self.parseFor()
        if self.tokens[self.i].val == 'forEach':
            self.i += 1
            return self.parseForE()
        if self.tokens[self.i].val in DT:
            return self.parseAssign()
        if self.tokens[self.i].val == 'return':
            self.consume()
            return self.pratt(0)
        if self.tokens[self.i].val == 'await':
            self.consume()
            vals = [self.consume()]
            while self.peek() and self.tokens[self.i].val == "Comma":
                vals.append(self.consume())
            return AwaitNode(vals, line, col)
        if self.tokens[self.i].val == 'import':
            self.consume()
            thing = []
            first = self.consume()
            thing.append(first)
            if self.peek() and self.peek().val == 'from':
                self.consume()
                thing.append(self.consume())
            return ImportNode(thing, line, col)
        return self.pratt(0)
    def parseFunc(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        concur = False
        kind = None
        if self.peek() and self.seek() in ["func", "class"]:
            kind = self.seek()
            self.consume()
        if self.peek() and self.peek() == "async":
            concur = True
            self.consume()
        name = self.consume()
        self.expect("Lpar")
        args = self.parseArgs()
        self.expect("Rpar")
        returnDataType = self.consume()
        self.expect("Lbrkt")
        code = self.parseBlock("Rbrkt")
        self.consume()
        return FuncNode(kind, concur, name, args, code, returnDataType, line, col)
    def parseBlock(self, end):
        blockStates = []
        while self.tokens[self.i].val not in end:
            blockStates.append(self.parseState())
        return blockStates
    def parseWhile(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        expr = self.pratt(0)
        self.expect("Then")
        block = self.parseBlock(["end"])
        return WhileNode(expr, block, line, col)
    def parseFor(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        init = self.pratt(0)
        self.expect("Semi")
        condition = self.pratt(0)
        self.expect("Semi")
        inc = self.pratt(0)
        self.expect("Then")
        block = self.parseBlock(["end"])
        return ForNode(init, condition, inc, block, line, col)
    def parseForE(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        var = self.consume()
        self.expect("in")
        expr = self.pratt(0)
        self.expect("Then")
        block = self.parseBlock(["end"])
        return ForENode(var, expr, block, line, col)
    def parseIfel(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        after = None
        expr = self.pratt(0)
        self.expect("Then")
        block = self.parseBlock(["end", "elif", "else"])
        if self.tokens[self.i].val == "elif":
            self.i += 1
            after = self.parseIfel()
        elif self.tokens[self.i].val == "else":
            self.i += 1
            after = self.parseBlock(["end"])
        else:
            self.i += 1
        return IfelNode(expr, block, after, line, col)
    def parseSwitch(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        expr = self.pratt(0)
        self.expect("Then")
        cases = self.parseCase()
        self.expect("end")
        return SwitchNode(expr, cases, line, col)
    def parseCase(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        expr = None
        also = []
        after = None
        if self.tokens[self.i].val == "case":
            self.i += 1
            expr = self.pratt(0)
            self.expect("Then")
            if self.tokens[self.i].val == "also":
                self.parseAlso(also)
            else:
                self.expect("default")
                self.expect("Then")
            block = self.parseBlock(["case", 'end', 'default'])
            if self.tokens[self.i].val in ["case", "default"]:
                after = self.parseCase()
            return CaseNode(expr, also, block, after, line, col)
    def parseAlso(self, alsos):
        self.i += 1
        alsos.append(self.pratt(0))
        self.expect("Then")
        if self.tokens[self.i].val == "also":
            self.parseAlso(alsos)
    def parseAssign(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        kind = self.consume()
        val = self.pratt(0)
        return AssignNode(kind, val, line, col)
    def parseVar(self):
        self.i -= 1
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        name = self.tokens[self.i].val
        self.consume()
        if self.peek() and self.tokens[self.i].val == "Then":
            return self.parseCall(name)
        self.i -= 1
        extra = []
        self.consume()
        cur = self.peek()
        if self.peek() == None:
            return VarNode(name, extra, line, col)
        while cur.val in ['Lbrc', 'Lpar', 'Lbrkt', "Point"]:
            if cur.val == "Point":
                self.consume()
                curVal = self.pratt(0)
                if not self.peek():
                    break
                extra.append(AccNode("Point", curVal, self.tokens[self.i].line, self.tokens[self.i].col))
            elif cur.val == "Lbrc":
                self.consume()
                args = []
                while self.peek() and self.peek().val != "Rbrc":
                    args.append(self.pratt(0))
                    if self.peek() and self.peek().val == "Comma":
                        self.consume()  # consume the comma
                extra.append(AccNode("Lbrc", args, self.tokens[self.i].line, self.tokens[self.i].col))
            elif cur.val == "Lpar":
                self.consume()
                args = []
                pars = 1
                while self.peek() and self.peek().val != "Rpar":
                    args.append(self.pratt(0))
                    if self.peek() and self.peek().val == "Comma":
                        self.consume()
                extra.append(AccNode("Lpar", args, self.tokens[self.i].line, self.tokens[self.i].col))
            elif cur.val == "Lbrkt":
                self.consume()
                args = []
                while self.peek() and self.peek().val != "Rbrkt":
                    args.append(self.pratt(0))
                    if self.peek() and self.peek().val == "Comma":
                        self.consume()  # consume the comma
                extra.append(AccNode("Lbrkt", args, self.tokens[self.i].line, self.tokens[self.i].col))
            cur = self.peek()
            if cur is None:
                break
        return VarNode(name, extra, line, col)
    def parseArgs(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        args = []
        if self.tokens[self.i].val not in DT:
            return None
        dt = self.consume()
        var = self.consume()
        args.append([dt, var])
        while self.tokens[self.i].val == "Comma":
            self.consume()
            if self.tokens[self.i].val not in DT:
                return None
            dt = self.consume()
            var = self.consume()
            args.append([dt, var])
        return ArgsNode(args, line, col)
    def parseCall(self, name):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        name = name
        types = []
        args = []
        self.consume()
        self.expect("Lbrc")
        self.consume()
        var = self.consume()
        types.append(var)
        while self.tokens[self.i].val == "Comma":
            self.consume()
            var = self.consume()
            types.append(var)
        self.expect("Rbrc")
        self.consume()
        self.expect("Lpar")
        self.consume()
        var = self.consume()
        args.append(var)
        while self.tokens[self.i].val == "Comma":
            self.consume()
            var = self.consume()
            args.append(var)
        self.expect("Rpar")
        self.consume()
        return CallNode(name, types, args, line, col)
