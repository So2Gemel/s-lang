class Parser {
  list<string> tokens;
  int index = 0;

  method tokenize(string code) {
    tokens = code.split(" ");
    index = 0;
  }

  method next() {
    if (index < tokens.length()) {
      return tokens[index++];
    }
    return null;
  }

  method peek() {
    if (index < tokens.length()) {
      return tokens[index];
    }
    return null;
  }

  method parse(string code) {
    tokenize(code);
    AST tree = new AST();

    while (peek() != null) {
      tree.add(parseStatement());
    }

    return tree;
  }

  method parseStatement() {
    string token = next();

    match token {
      case "print": return parsePrint();
      case "method": return parseMethod();
      case "class": return parseClass();
      case "if": return parseIf();
      case "go": return parseGoBlock();
      case "safe": return parseSafeBlock();
      case "asm": return parseAsmBlock();
      case else: return parseExpression(token);
    }
  }

  method parsePrint() {
    string value = next();
    return ASTNode("Print", value);
  }

  method parseMethod() {
    string name = next();
    string args = next(); // Simplified
    return ASTNode("Method", name + ":" + args);
  }

  method parseClass() {
    string name = next();
    return ASTNode("Class", name);
  }

  method parseIf() {
    string condition = next();
    return ASTNode("If", condition);
  }

  method parseGoBlock() {
    return ASTNode("GoBlock", "async");
  }

  method parseSafeBlock() {
    return ASTNode("SafeBlock", "protected");
  }

  method parseAsmBlock() {
    return ASTNode("AsmBlock", "low-level");
  }

  method parseExpression(string token) {
    return ASTNode("Expression", token);
  }
}
