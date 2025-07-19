📘 الفصل 6: بناء مكتبة قياسية core.slib – دوال جاهزة، توثيقها، وربطها مع Interpreter

---

🎯 لماذا نحتاج مكتبة قياسية؟

كل لغة برمجة قوية تملك مجموعة دوال وأدوات جاهزة تُسهّل على المطور بناء المشاريع دون الحاجة لكتابة كل شيء من الصفر.  
في لغة S/S++، نُنشئ مكتبة رسمية تدعى core.slib، تكون مرجعية أساسية لكل البرامج.

---

📦 إنشاء ملف المكتبة

ضع الملف داخل مجلد stdlib/ بهذا المسار:

```txt
stdlib/core.slib
```

صيغة المكتبة يمكن أن تكون شبه DSL أو JSON أو أي تنسيق خاص بلغة S.

---

🧰 الدوال القياسية المقترحة

| الدالة            | الوصف                           | التوقيع |
|-------------------|----------------------------------|---------|
| print(text)     | طباعة إلى الشاشة                | func print(text: string) |
| input(prompt)   | قراءة من المستخدم               | func input(prompt: string): string |
| len(item)       | حساب الطول لأي عنصر قابل للقياس| func len(item: list<T>): int |
| type(var)       | معرفة نوع متغير                 | func type(var: any): string |
| add(a,b)        | جمع رقمين                       | func add(a: int, b: int): int |
| split(text,sep) | تقسيم النص                      | func split(text: string, sep: string): list<string> |

> هذه الدوال تُكتب داخل core.slib ويمكن لاحقًا ترجمتها إلى تنفيذ فعلي داخل الـ Interpreter

---

🔧 مثال مكتبة نصيّة

```s
func print(text: string);
func input(prompt: string): string;
func len(item: list<any>): int;
func add(a: int, b: int): int;
func type(x: any): string;
```

---

🔍 كيف يرتبط الـ Interpreter بها؟

عند تنفيذ الـ AST، يبحث الـ Interpreter أولًا:
1. هل الأمر يُنفذ داخليًا (مثل let, print)
2. هل الأمر موجود في core.slib
3. إذا وُجد، يتم استدعاؤه من المكتبة، أو ترجمة الكود إلى عملية فعلية

✅ مثال:

```s
print("أهلاً");
```

في الـ Interpreter:
```python
if node["type"] == "PrintStatement":
    # ينفذ الكود مباشرة
elif node["type"] == "Call":
    # يبحث في core.slib عن الدالة ثم ينفذها
```

---
