import json

def run_ast(ast_path):
    # قراءة ملف AST
    with open(ast_path, "r", encoding="utf-8") as f:
        ast = json.load(f)

    # تخزين المتغيرات
    variables = {}

    # تنفيذ الشيفرة من خلال AST
    for node in ast:
        if node["type"] == "FunctionDeclaration":
            print(f"🔧 تشغيل الدالة: {node['name']}")
            for stmt in node["body"]:
                if stmt["type"] == "VariableDeclaration":
                    name = stmt["name"]
                    value = stmt["value"]
                    variables[name] = value
                    print(f"📥 حفظ متغير: {name} = {value}")
                elif stmt["type"] == "PrintStatement":
                    val = stmt["value"]
                    if val["type"] == "Concatenation":
                        left = val["left"]
                        right = variables.get(val["right"], "[غير معرّف]")
                        print(f"📢 طباعة: {left}{right}")

if __name__ == "__main__":
    print("🚀 تشغيل Interpreter لملف AST\n")
    run_ast("parser/ast_samples/main_ast.json")
