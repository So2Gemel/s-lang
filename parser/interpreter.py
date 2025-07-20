# interpreter.py — S/S++ Execution Core
import threading
import time
import traceback

class Context:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.classes = {}
        self.stack = []

class ASTNode:
    def __init__(self, type_, value=None, children=None):
        self.type = type_
        self.value = value
        self.children = children or []

class Interpreter:
    def __init__(self):
        self.context = Context()

    def execute(self, node):
        try:
            method = getattr(self, f"exec_{node.type}", self.exec_unknown)
            return method(node)
        except Exception as e:
            print(f"⚠️ Runtime Error: {e}")
            traceback.print_exc()

    def exec_unknown(self, node):
        print(f"🚫 Unknown node type: {node.type}")

    def exec_Print(self, node):
        val = self.evaluate(node.value)
        print(val)

    def exec_Assign(self, node):
        name = node.value
        val = self.evaluate(node.children[0])
        self.context.variables[name] = val

    def exec_If(self, node):
        cond = self.evaluate(node.value)
        if cond:
            for child in node.children:
                self.execute(child)

    def exec_Method(self, node):
        name = node.value
        self.context.functions[name] = node

    def exec_Call(self, node):
        name = node.value
        func = self.context.functions.get(name)
        if not func:
            raise Exception(f"Function '{name}' not found")
        for child in func.children:
            self.execute(child)

    def exec_Class(self, node):
        self.context.classes[node.value] = node

    def exec_Loop(self, node):
        while True:
            for child in node.children:
                self.execute(child)
            time.sleep(0.01)

    def exec_GoBlock(self, node):
        thread = threading.Thread(target=lambda: [self.execute(c) for c in node.children])
        thread.start()

    def exec_SafeBlock(self, node):
        try:
            for child in node.children:
                self.execute(child)
        except Exception as e:
            print(f"🛡️ SafeBlock caught error: {e}")

    def exec_Match(self, node):
        value = self.evaluate(node.value)
        for case in node.children:
            if case.value == value or case.value == "else":
                for child in case.children:
                    self.execute(child)
                break

    def evaluate(self, expr):
        if isinstance(expr, ASTNode):
            if expr.type == "Literal":
                return expr.value
            elif expr.type == "Variable":
                return self.context.variables.get(expr.value, None)
        return expr
