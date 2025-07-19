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
