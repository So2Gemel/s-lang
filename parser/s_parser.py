# s_parser.py — Smart Parser for S/S++
import re

class Token:
    def __init__(self, type_, value, line=0):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.type}:{self.value}"

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = {"class", "method", "if", "else", "loop", "match", "case", "return", "go", "safe", "asm"}

    def tokenize(self):
        lines = self.code.split("\n")
        for line_num, line in enumerate(lines):
            parts = re.findall(r"[A-Za-z_]\w*|==|!=|<=|>=|[{}():=+*/<>-]|\".*?\"|\d+", line)
            for part in parts:
                if part in self.keywords:
                    self.tokens.append(Token("KEYWORD", part, line_num))
                elif re.match(r"\d+", part):
                    self.tokens.append(Token("NUMBER", int(part), line_num))
                elif re.match(r"\".*?\"", part):
                    self.tokens.append(Token("STRING", part.strip("\""), line_num))
                elif re.match(r"[A-Za-z_]\w*", part):
                    self.tokens.append(Token("IDENT", part, line_num))
                else:
                    self.tokens.append(Token("SYMBOL", part, line_num))
        return self.tokens

class ASTNode:
    def __init__(self, type_, value=None, children=None):
        self.type = type_
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f"{self.type}({self.value})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def peek(self):
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    def next(self):
        tok = self.peek()
        self.index += 1
        return tok

    def parse(self):
        ast = []
        while self.peek():
            node = self.parse_statement()
            if node:
                ast.append(node)
        return ast

    def parse_statement(self):
        tok = self.peek()
        if tok.type == "KEYWORD":
            if tok.value == "class":
                return self.parse_class()
            elif tok.value == "method":
                return self.parse_method()
            elif tok.value == "if":
                return self.parse_if()
            elif tok.value == "loop":
                return self.parse_loop()
            elif tok.value == "match":
                return self.parse_match()
            elif tok.value == "go":
                return self.parse_go()
            elif tok.value == "safe":
                return self.parse_safe()
            elif tok.value == "asm":
                return self.parse_asm()
        elif tok.type == "IDENT":
            return self.parse_expression()
        return None

    def parse_class(self):
        self.next()  # class
        name = self.next().value
        self.next()  # {
        body = []
        while self.peek().value != "}":
            body.append(self.parse_statement())
        self.next()  # }
        return ASTNode("Class", name, body)

    def parse_method(self):
        self.next()  # method
        name = self.next().value
        self.next()  # (
        args = []
        while self.peek().value != ")":
            args.append(self.next().value)
            if self.peek().value == ",":
                self.next()
        self.next()  # )
        self.next()  # {
        body = []
        while self.peek().value != "}":
            body.append(self.parse_statement())
        self.next()  # }
        return ASTNode("Method", name, body)

    def parse_if(self):
        self.next()  # if
        condition = self.next().value
        self.next()  # {
        body = []
        while self.peek().value != "}":
            body.append(self.parse_statement())
        self.next()  # }
        return ASTNode("If", condition, body)

    def parse_loop(self):
        self.next()  # loop
        self.next()  # {
        body = []
        while self.peek().value != "}":
            body.append(self.parse_statement())
        self.next()  # }
        return ASTNode("Loop", None, body)

    def parse_match(self):
        self.next()  # match
        value = self.next().value
        self.next()  # {
        cases = []
        while self.peek().value != "}":
            self.next()  # case
            case_val = self.next().value
            self.next()  # :
            case_body = [self.parse_statement()]
            cases.append(ASTNode("Case", case_val, case_body))
        self.next()  # }
        return ASTNode("Match", value, cases)

    def parse_go(self):
        self.next()  # go
        self.next()  # {
        body = []
        while self.peek().value != "}":
            body.append(self.parse_statement())
        self.next()  # }
        return ASTNode("GoBlock", None, body)

    def parse_safe(self):
        self.next()  # safe
        self.next()  # {
        body = []
        while self.peek().value != "}":
            body.append(self.parse_statement())
        self.next()  # }
        return ASTNode("SafeBlock", None, body)

    def parse_asm(self):
        self.next()  # asm
        self.next()  # {
        code = []
        while self.peek().value != "}":
            code.append(self.next().value)
        self.next()  # }
        return ASTNode("AsmBlock", " ".join(code))

    def parse_expression(self):
        ident = self.next().value
        return ASTNode("Expression", ident)
