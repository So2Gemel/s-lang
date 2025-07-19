import json

def tokenize(code: str) -> list:
    """
    تحويل الكود إلى سلسلة من الرموز (tokens)
    """
    tokens = code.replace("(", " ( ").replace(")", " ) ").split()
    return tokens

def parse_tokens(tokens: list) -> dict:
    """
    بناء شجرة AST من الرموز، بشكل بدائي للتجربة
    """
    ast = {
        "type": "Program",
        "body": []
    }
    i = 0
    while i < len(tokens):
        if tokens[i] == "let":
            var_name = tokens[i+1]
            var_type = tokens[i+3]
            var_value = tokens[i+5]
            ast["body"].append({
                "type": "LetDeclaration",
                "name": var_name,
                "datatype": var_type,
                "value": {
                    "type": "Literal",
                    "value": var_value
                }
            })
            i += 6
        elif tokens[i] == "print":
            ast["body"].append({
                "type": "CallExpression",
                "name": "print",
                "args": [{
                    "type": "Variable",
                    "name": tokens[i+1]
                }]
            })
            i += 2
        else:
            i += 1
    return ast

def save_ast(ast: dict, path: str):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(ast, file, indent=4, ensure_ascii=False)

def parse_and_save(code: str, path: str):
    tokens = tokenize(code)
    ast = parse_tokens(tokens)
    save_ast(ast, path)

if __name__ == "__main__":
    sample_code = "let x: int = 5; print x"
    parse_and_save(sample_code, "ast_samples/main_ast.json")
