# الفصل 1: مقدمة في لغة S/S++

## 🎯 لماذا لغة S؟

لغة S هي لغة برمجة حديثة متعددة الاستخدامات، تجمع بين:
- بساطة Python في الكتابة.
- سرعة C/C++ في التنفيذ.
- مرونة C# في التنظيم وتعدد المنصات.

تم تصميمها لتكون مناسبة لكل من:
- المبرمجين المبتدئين
- المطورين المحترفين
- مصممي الأدوات والواجهات

## 🧬 ما الفرق بين S و S++؟

| الإصدار | الوصف |
|---------|-------|
| **S**   | نسخة أساسية، مثالية للبناء السريع والمشاريع المتوسطة |
| **S++** | نسخة موسعة، تدعم البرمجة الكائنية، التحكم بالذاكرة، والمكتبات المتقدمة |

## ✅ أهداف اللغة

- سهولة التعلم والاستخدام
- تنظيم نظيف للكود
- دعم مشاريع واسعة النطاق
- مرونة في التصميم وتعدد المنصات

## 🖥️ أول برنامج بلغة S

```s
func main() {
    let name: string = "So2_gemel";
    print("مرحبًا يا " + name);
}
---

## 🔧 ثانيًا: ملف `parser/s_parser.py` كبداية لـ Parser بلغة Python

```python
# s_parser.py – أول نموذج بسيط لتحليل شيفرة S إلى عناصر مبدئية

def simple_parser(code: str):
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('func'):
            print(f"[Function] → {line}")
        elif line.startswith('let'):
            print(f"[Variable] → {line}")
        elif line.startswith('print'):
            print(f"[Output] → {line}")

# تجربة
example_code = """
func main() {
    let name: string = "So2_gemel";
    print("مرحبًا يا " + name);
}
"""

simple_parser(example_code)
