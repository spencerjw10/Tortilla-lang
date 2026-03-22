#AST Nodes
class Node:
        def __init__(self, lin, colum):
            self.line = lin
            self.col = colum
#operator = op /str
#expression = expr# /node
#number lit = num /#
#string lit = stri /str
#bool lit = boo /tf
#var name = name /str
#array = extra /array
#node type spec = kind /str
#code block = block /array
#another node = recur /node
#addon bool = add /bool
#data type = dt /str

#[op, expr1]
class UnOpNode(Node):
    def __init__(self, op, expr1, lin, colum):
        super().__init__(lin, colum)
        self.op = op
        self.expr1 = expr1
#expr1, op, expr2
class BinOpNode(Node):
    def __init__(self, expr1, op, expr2, lin, colum):
        super().__init__(lin, colum)
        self.expr1 = expr1
        self.op = op
        self.expr2 = expr2
#num|str|bool, kind
class BasicNode(Node):
    def __init__(self, num, kind, lin, colum):
        super().__init__(lin, colum)
        self.num = num
        sekf.kind = kind
#name, extra1
class VarNode(Node):
    def __init__(self, name, extra1, lin, colum):
        super().__init__(lin, colum)
        self.name = name
        self.extra1 = extra1
#kind, expr1
class AccNode(Node):
    def __init__(self, kind, expr1, lin, colum):
        super().__init__(lin, colum)
        self.kind = kind
        self.expr1 = expr1
#expr1
class GroupNode(Node):
    def __init__(self, expr1, lin, colum):
        super().__init__(lin, colum)
        self.expr1 = expr1
#expr1, block
class WhileNode(Node):
    def __init__(self, expr1, block, lin, colum):
        super().__init__(lin, colum)
        self.expr1 = expr1
        self.block = block
#expr1, expr2, expr3, block
class ForNode(Node):
    def __init__(self, expr1, expr2, expr3, block, lin, colum):
        super().__init__(lin, colum)
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.block = block
#name, expr1, block
class ForENode(Node):
    def __init__(self, name, expr1, block, lin, colum):
        super().__init__(lin, colum)
        self.name = name
        self.expr1 = expr1
        self.block = block
#expr1, block, recur
class IfelNode(Node):
    def __init__(self, expr1, block, recur, lin, colum):
        super().__init__(lin, colum)
        self.expr1 = expr1
        self.block = block
        self.recur = recur
#expr1, extra1
class SwitchNode(Node):
    def __init__(self, expr1, extra1, lin, colum):
        super().__init__(lin, colum)
        self.expr1 = expr1
        self.extra1 = extra1
#expr1, extra1, block, recur
class CaseNode(Node):
    def __init__(self, expr1, extra1, block, recur, lin, colum):
        super().__init__(lin, colum)
        self.expr1 = expr1
        self.extra1 = extra1
        self.block = block
        self.recur = recur
#block, recur
class DefaultNode(Node):
    def __init__(self, block, recur, lin, colum):
        super().__init__(lin, colum)
        self.block = block
        self.recur = recur
#kind, extra1
class ListNode(Node):
    def __init__(self, kind, extra1, lin, colum):
        super().__init__(lin, colum)
        self.kind = kind
        self.extra1 = extra1
#kind, name, expr1
class AssignNode(Node):
    def __init__(self, kind, name, expr1, lin, colum):
        super().__init__(lin, colum)
        self.kind = kind
        self.name = name
        self.expr1 = expr1
#extra1
class ArgsNode(Node):
    def __init__(self, extra1, lin, colum):
        super().__init__(lin, colum)
        self.extra1 = extra1
#kind, add, name, extra1, block, dt
class FuncNode(Node):
    def __init__(self, kind, add, name, extra1, block, dt, lin, colum):
        super().__init__(lin, colum)
        self.kind = kind
        self.add = add
        self.name = name
        self.extra1 = extra1
        self.block = block
        self.dt = dt
#name, extra1, extra2
class CallNode(Node):
    def __init__(self, name, extra1, extra2, lin, colum):
        super().__init__(lin, colum)
        self.name = name
        self.extra1 = extra1
        self.extra2 = extra2
#extra1
class AwaitNode(Node):
    def __init__(self, extra1, lin, colum):
        super().__init__(lin, colum)
        self.extra1 = extra1
#extra1
class ImportNode(Node):
    def __init__(self, extra1, lin, colum):
        super().__init__(lin, colum)
        self.extra1 = extra1


#Parser
i = 0
nodes = []
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
'''Error types
3 End of Script
4 Expected WORD
5 Missing Operator
6 Unkown Operator
7 Unkown Data Type
'''
class Parse:
    def __init__(self, tokens):
        self.nodes = []
        self.tokens = tokens
        self.i = 0

    def peek(self):
        if self.i == len(self.tokens):
            #e3
            return False
        print("hi")
        return self.tokens[self.i]
    def consume(self):
        self.i += 1
        if self.i - 1 == len(self.tokens):
            #e3
            return None
        return self.tokens[self. i - 1]
    def expect(self, val):
        if self.i == len(self.tokens):
            #e3
            return None
        if self.peek().val != val:
            #4
            return None
        return self.consume()
    def pratt(self, minBP):
        tok = self.consume()
        left = 0
        if tok.kind in ("Int", "Float", "Str", "Bool"):
            left = BasicNode(tok.val, toke.kind, tok.line, tok.col)
        elif tok.kind == "Variable":
            left = self.parseVar()
        elif tok.val in ("not", "BitNot", "Minus"):
            right = self.pratt(90)
            left = UnOpNode(tok.val, right, tok.line, tok.col)
        elif tok.val == "Lpar":
            elems = []
            commas = False
            while True:
                curAdd = self.pratt(0)
                elems.append([curAdd, curAdd])
                if self.peek() and self.peek().val == "Rpar":
                    self.consume()
                    break
                commas = True
                self.consume()
            if not commas:
                left = GroupNode(elems[0], tok.line, tok.col)
            else:
                left = ListNode("Set", elems, tok.line, tok.col)
        elif tok.val == "Lbrc":
            elems = []
            while True:
                curAdd = self.pratt(0)
                elems.append([curAdd, curAdd])
                if self.peek() and (self.peek().val == "Rbrc"):
                    self.consume()
                    break
                self.consume()
            left = ListNode("Array", elems, tok.line, tok.col)
        elif tok.val == "Lbrkt":
            elems = []
            while True:
                curElem = self.pratt(0)
                curKey = None
                if self.peek() and (self.peek().val == "Rbrkt"):
                    self.consume()
                    break
                if self.peek() and (self.peek().val == "Then"):
                    self.consume()
                    curKey = self.pratt(0)
                elems.append([curElem, curKey])
                self.consume()
            left = ListNode("Dict", elems, tok.line, tok.col)
        while True:
            op = self.peek()
            if op is None:
                #5
                break
            elif op.val not in BPChart:
                #6
                break
            bp = BPChart[op.val]
            if bp <= minBP:
                break
            self.consume()
            right = self.pratt(bp)
            left = BinOpNode(left, op.val, right, op.line, op.col)
        return left
    def parsePrgm(self):
        print("hi")
        while self.i < len(self.tokens):
            self.nodes.append(self.parseState())
        return self.nodes
    #Start on
    def parseState(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        if self.peek().val == 'if':
            self.consume()
            return self.parseIfel()
        if self.peek().val == 'switch':
            self.consume()
            return self.parseSwitch()
        if self.peek().val == 'while':
            self.consume()
            return self.parseWhile()
        if self.peek().val == 'for':
            self.consume()
            return self.parseFor()
        if self.peek().val == 'forEach':
            self.consume()
            return self.parseForE()
        if self.peek().val in DT:
            return self.parseAssign()
        if self.peek().val == 'return':
            self.consume()
            return self.pratt(0)
        if self.peek().val == 'await':
            self.consume()
            vals = [self.consume()]
            while self.peek() and self.peek().val == "Comma":
                vals.append(self.consume())
            return AwaitNode(vals, line, col)
        if self.peek().val == 'import':
            self.consume()
            extra = [self.consume()]
            if self.peek() and self.peek().val == 'spec':
                self.consume()
                extra.append(self.consume())
            return ImportNode(extra, line, col)
        if self.peek().val in ("func", "class"):
            return self.parseFunc()
        return self.pratt(0)
    #start on
    def parseFunc(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        concur = False
        kind = self.consume()
        if self.peek() and self.peek() == "async":
            concur = True
            self.consume()
        name = self.consume()
        self.expect("Lpar")
        args = self.parseArgs()
        self.expect("Rpar")
        returnDataType = self.consume()
        self.expect("Lbrkt")
        code = self.parseBlock(["Rbrkt"])
        self.consume()
        return FuncNode(kind, concur, name, args, code, returnDataType, line, col)
    #start after
    def parseBlock(self, end):
        blockStates = []
        while self.peek() and self.peek().val not in end:
            blockStates.append(self.parseState())
        return blockStates
    #start after
    def parseWhile(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        expr = self.pratt(0)
        self.expect("Then")
        block = self.parseBlock(["end"])
        return WhileNode(expr, block, line, col)
    #start after
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
    #start after
    def parseForE(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        var = self.consume()
        self.expect("in")
        expr = self.pratt(0)
        self.expect("Then")
        block = self.parseBlock(["end"])
        return ForENode(var, expr, block, line, col)
    #start after
    def parseIfel(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        after = None
        expr = self.pratt(0)
        self.expect("Then")
        block = self.parseBlock(["end", "elif", "else"])
        if self.peek() and self.peek().val == "elif":
            self.consume()
            after = self.parseIfel()
        elif self.peek() and self.peek().val == "else":
            self.consume()
            after = self.parseBlock(["end"])
        else:
            self.expect("end")
        return IfelNode(expr, block, after, line, col)
    #start after
    def parseSwitch(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        expr = self.pratt(0)
        self.expect("Then")
        cases = self.parseCase()
        self.expect("end")
        return SwitchNode(expr, cases, line, col)
    #start on
    def parseCase(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        also = []
        after = None
        if self.peek().val == "case":
            self.consume()
            expr = self.pratt(0)
            self.expect("Then")
            if self.peek().val == "also":
                self.consume()
                self.parseAlso(also)
            else:
                self.expect("default")
                self.expect("Then")
            block = self.parseBlock(["case", "end", "default"])
            if self.peek().val in ["case", "default"]:
                after = self.parseCase()
            return CaseNode(expr, also, block, after, line, col)
        elif self.peek().val == "default":
            self.consume()
            self.expect("Then")
            block = self.parseBlock(["case", "end"])
            if self.peek().val == "case":
                after = self.parseCase()
            return DefaultNode(block, after, line, col)
        return None
    #start after
    def parseAlso(self, alsos):
        alsos.append(self.pratt(0))
        self.expect("Then")
        if self.peek().val == "also":
            self.consume()
            self.parseAlso(alsos)
        return alsos
    #start on
    def parseAssign(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        kind = self.consume()
        val = self.parseVar()
        self.expect("Assign")
        expr = self.pratt(0)
        return AssignNode(kind, val, expr, line, col)
    #start on
    def parseVar(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        name = self.tokens[self.i].val
        self.consume()
        if self.peek() and self.peek().val == "Then":
            self.consume()
            return self.parseCall(name)
        extra = []
        cur = self.peek()
        if self.peek() is None:
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
    #start after
    def parseArgs(self):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        args = []
        if self.peek().val not in DT:
            #7
            return None
        dt = self.consume()
        var = self.consume()
        args.append([dt, var])
        while self.peek().val == "Comma":
            self.consume()
            if self.peek().val not in DT:
                #7
                return None
            dt = self.consume()
            var = self.consume()
            args.append([dt, var])
        return ArgsNode(args, line, col)
    #start after
    def parseCall(self, name):
        line = self.tokens[self.i].line
        col = self.tokens[self.i].col
        name = name
        types = []
        args = []
        self.expect("Lbrc")
        types.append(self.consume())
        while self.peek().val == "Comma":
            self.consume()
            types.append(self.consume())
        self.expect("Rbrc")
        self.expect("Lpar")
        args.append(self.consume())
        while self.peek().val == "Comma":
            self.consume()
            args.append(self.consume())
        self.expect("Rpar")
        return CallNode(name, types, args, line, col)

#Hoister
class Hoist:
    def __init__(self, states):
        self.states = states

    def walkPrgm(self):
        obob = 2