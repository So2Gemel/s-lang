import json
import re
import os

def parse_variable(line):
    match = re.match(r'let\s+(\w+):\s*(\w+)\s*=\s*"(.+)";', line)
    if match:
        return {
            "type": "VariableDeclaration",
            "name": match.group(1),
            "datatype": match.group(2),
            "value": match.group(3)
        }
    return None

def parse_print(line):
    match = re.match(r'print\("(.+)" \+ (\w+)\);', line)
    if match:
        return {
            "type": "PrintStatement",
            "value": {
                "type": "Concatenation",
                "left": {
                    "type": "StringLiteral",
                    "value": match.group(1)
                },
                "right": {
                    "type": "Identifier",
                    "name": match.group(2)
                }
            }
        }
    return None

def parse_function(lines):
    header = lines[0].strip()
    body_lines = lines[1:-1]  # استبعاد الأقواس
    match = re.match(r'func\s+(\w+)\(\)\s*\{', header)
    if match:
        body = []
        for line in body_lines:
            line = line.strip()
            if line.startswith("let"):
                node = parse_variable(line)
                if node: body.append(node)
            elif line.startswith("print"):
                node = parse_print(line)
                if node: body.append(node)
        return {
            "type": "FunctionDeclaration",
            "name": match.group(1),
            "args": [],
            "body": body
        }
    return None

def parse_code(code: str):
    lines = code.strip().split('\n')
    ast = []
    if lines[0].startswith("func") and lines[-1] == "}":
        node = parse_function(lines)
        if node: ast.append(node)
    return ast

def save_ast(ast, filename="main_ast.json"):
    folder = "parser/ast_samples"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ast, f, indent=2, ensure_ascii=False)
    print(f"✅ تم حفظ AST في: {path}")

if __name__ == "__main__":
    example_code = """
func main() {
    let name: string = "So2_gemel";
    print("مرحبًا يا " + name);
}
"""
    print("🔍 تحليل الشيفرة بلغة S:\n")
    ast = parse_code
