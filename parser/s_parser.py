# s_parser.py — نموذج بسيط لتحليل شيفرة S

def simple_parser(code: str):
    lines = code.strip().split('\n')
    for idx, line in enumerate(lines, 1):
        line = line.strip()
        if line.startswith('func'):
            print(f"[Line {idx}] 🧠 Function → {line}")
        elif line.startswith('let'):
            print(f"[Line {idx}] 🔷 Variable → {line}")
        elif line.startswith('print'):
            print(f"[Line {idx}] 📢 Output → {line}")
        elif line == '{' or line == '}':
            print(f"[Line {idx}] 🔧 Block → {line}")
        elif line == '':
            continue
        else:
            print(f"[Line {idx}] ❓ Unknown → {line}")

# مثال تجريبي لتجربة التحليل
example_code = """
func main() {
    let name: string = "So2_gemel";
    print("مرحبًا يا " + name);
}
"""

# تجربة التحليل
if __name__ == "__main__":
    print("🔍 تحليل الشيفرة بلغة S:\n")
    simple_parser(example_code)
