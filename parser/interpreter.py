import json

def load_ast(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def interpret(ast: dict):
    env = {}
    for node in ast.get("body", []):
        if node["type"] == "LetDeclaration":
            name = node["name"]
            value = evaluate(node["value"])
            env[name] = value
        elif node["type"] == "CallExpression":
            if node["name"] == "print":
                arg_name = node["args"][0]["name"]
                print(env.get(arg_name, "undefined"))

def evaluate(expr: dict):
    if expr["type"] == "Literal":
        val = expr["value"]
        try:
            return int(val)
        except ValueError:
            return val
    return None

def load_core_library(path):
    slib = {}
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip().startswith("func"):
                name = line.split("(")[0].replace("func", "").strip()
                slib[name] = {"signature": line.strip()}
    return slib

# تحميل المكتبة
builtins = load_core_library("../stdlib/core.slib")

if __name__ == "__main__":
    ast = load_ast("ast_samples/main_ast.json")
    interpret(ast)

