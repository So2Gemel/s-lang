import json
import re

def parse_variable(line):
    match = re.match(r'let\s+(\w+):\s*(\w+)\s*=\s*(.+);', line)
    if match:
        return {
            "type": "VariableDeclaration",
            "name": match.group(1),
            "datatype": match.group(2),
            "value": match.group(3).strip('"')
        }

def parse_print(line):
    match = re.match(r'print\("(.+)" \+ (\w+)\);', line)
    if match:
        return {
            "type": "PrintStatement",
            "value": {
                "type": "Concatenation",
                "left": match.group(1),
                "right": match.group(2)
            }
        }

def parse_function(lines):
    header = lines[0].strip()
    body_lines = lines[1:-1]  # exclude brackets
    match = re.match(r'func\s+(\w+)\(\)\s*\{', header)
    if match:
        body = []
        for line in body_lines:
            line = line.strip()
            if line.startswith("let"):
                body.append(parse_variable(line))
            elif line.startswith("print"):
                body.append(parse_print(line))
        return {
            "type": "FunctionDeclaration",
            "name": match.group(1),
            "body": body
        }

def parse_code(code: str):
    lines = code.strip().split('\n')
    ast = []
    if lines[0].startswith("func") and lines[-1] == "}":
        ast.append(parse_function(lines))
    return ast

if __name__ == "__main__":
    example_code = """
func main() {
    let name: string = "So2_gemel";
    print("مرحبًا يا " + name);
}
"""
    ast = parse_code(example_code)
    print("🧠 البناء الشجري (AST):\n")
    print(json.dumps(ast, indent=2, ensure_ascii=False))
