📘 الفصل 7: تصميم واجهة رسومية للغة S/S++ — بيئة تعليمية، محرر ذكي، وتنفيذ حيّ للكود

---

🎯 لماذا واجهة رسومية؟

في عصر البرمجة الحديثة، التفاعل مع اللغة لا يقتصر على الطرفية والنصوص. واجهة رسومية قوية يمكن أن:

- 🧠 تختصر الحواجز التقنية للمبتدئين
- 🚀 تسرّع عملية التطوير والتجربة
- 📚 تربط التعلم النظري بتنفيذ عملي حيّ
- 📦 تصبح بيئة موحدة لتطوير، تحليل، توثيق، وتنفيذ الأكواد

---

🖥️ مكونات محرر S الذكي

| المكوّن              | الوظيفة                                                 |
|----------------------|----------------------------------------------------------|
| محرر نصي              | لكتابة الشيفرة بلغة S/S++                               |
| زر "تحليل الكود"      | لتحويل الشيفرة إلى AST عبر s_parser.py               |
| زر "تنفيذ الكود"      | لتشغيل AST باستخدام interpreter.py                   |
| نافذة النتائج         | لعرض المخرجات أو الأخطاء                                 |
| قائمة المشاريع        | لاستعراض وتشغيل الأمثلة من examples/                  |
| تبويب التوثيق         | عرض محتوى الفصل التعليمي الحالي من docs/*.md         |
| دعم الحفظ والفتح      | حفظ أكواد واختبارها لاحقًا بسهولة                       |

---

🌐 فلسفة التصميم: واجهة تعليمية تنفيذية

> تجربة واحدة، تجمع:  
> ✍️ الكتابة + 🔍 التحليل + 🚀 التنفيذ + 📚 التعلم + 📊 التوثيق

---

🔧 الخطوات المعمارية لبناء الواجهة

✅ المرحلة 1: اختيار مكتبة GUI

- مبدئيًا: Tkinter (سريعة، مدمجة مع Python)
- لاحقًا: PyQt / Electron لدعم موسّع ومرونة واجهات

---

✅ المرحلة 2: بناء الواجهة الأولية

```python
import tkinter as tk
from tkinter import filedialog, scrolledtext

def run_code():
    code = editor.get("1.0", tk.END)
    with open("temp.s", "w", encoding="utf-8") as f:
        f.write(code)
    # خطوات: تحليل الكود، إنتاج AST، تشغيله ← يتم ربطها لاحقًا

root = tk.Tk()
root.title("S Language Studio")

editor = scrolledtext.ScrolledText(root, width=90, height=25, font=("Consolas", 12))
editor.pack(padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btnframe, text="تحليل الكود", command=runcode).pack(side=tk.LEFT, padx=5)
tk.Button(btnframe, text="تشغيل", command=runcode).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="فتح ملف", command=lambda: filedialog.askopenfilename()).pack(side=tk.LEFT, padx=5)

root.mainloop()
```

🎨 يمكن تحسين هذا النموذج لاحقًا ليشمل:
- تبويبات للكود والنتائج
- عرض الـ AST في شجرة رسومية
- دمج مستندات الفصل التعليمية في نافذة جانبية

---

📚 دمج الفصول التعليمية داخل IDE

✅ فكرة تبويب “الدروس”:

- يعرض كل فصل من docs/*.md
- يقرأ المحتوى ويعرضه في نافذة جانبية
- المتعلم يقرأ الفصل وينفذ الكود مباشرةً

مثال برمجي:

```python
with open("docs/ch2_basics.md", encoding="utf-8") as f:
    lesson_text.insert(tk.END, f.read())
```

---

📦 الربط مع أدوات المشروع

| الأداة            | الوظيفة داخل IDE            |
|------------------|-----------------------------|
| s_parser.py     | تحليل الكود إلى AST         |
| interpreter.py  | تشغيل الكود فعليًا          |
| core.slib       | استدعاء الدوال الجاهزة      |
| syntax.md       | عرض قواعد اللغة المرجعية    |
| ast_samples/    | تخزين وتحليل البناء الشجري  |

> كل هذه الأدوات تُدمج داخل IDE لخلق تجربة كاملة.

---

🎯 رؤية مستقبلية لـ S Studio

✅ ميزات متوقعة في الإصدارات القادمة:

- التلوين التلقائي للكود (Syntax Highlighting)
- التصحيح الذكي (Linting + Suggestions)
- تشغيل جزئي للكود (Execute Selection)
- توصيل عبر الإنترنت لتجارب مجتمع S
- تصدير المشاريع إلى HTML / PDF / Markdown

---

🛠️ تنظيم ملفات الواجهة

```
tools/
└── ide/
    ├── s_studio.py
    ├── assets/
    │   ├── icon.png
    │   └── logo.svg
    ├── templates/
    │   ├── default.s
    │   └── welcome.md
```

---
