📘 الفصل 8: بناء مكتبة قياسية للغة S/S++ — التصميم، التوثيق، والربط مع المُفسّر

---

🎯 لماذا نحتاج مكتبة قياسية؟

كل لغة برمجة ناجحة تملك مكتبة أساسية توفر دوال جاهزة للتعامل مع النصوص، القوائم، الإدخال، الطباعة، وغيرها.  
مكتبة core.slib في لغة S/S++ تمثل حجر الأساس لبناء التطبيقات، وتجعل اللغة مفيدة منذ أول تجربة.

---

🧱 تصميم المكتبة القياسية

المكتبة تُكتب كملف مستقل داخل stdlib/:

```bash
stdlib/
└── core.slib
```

وصيغته يمكن أن تكون شبيهة بهيكل اللغة نفسها:

```s
func print(text: string);
func input(prompt: string): string;
func len(list: list<any>): int;
func add(a: int, b: int): int;
func split(text: string, sep: string): list<string>;
func type(x: any): string;
```

---

📚 توثيق دوال المكتبة

| الدالة      | التوقيع                              | الوصف العملي                            |
|-------------|---------------------------------------|------------------------------------------|
| print     | func print(text: string)            | يطبع النص في المخرجات                   |
| input     | func input(prompt: string): string  | يطلب إدخال من المستخدم كنص              |
| len       | func len(list: list<any>): int      | يرجع طول القائمة                        |
| add       | func add(a: int, b: int): int       | جمع رقمين صحيحين                       |
| split     | func split(text, sep): list<string> | تقسيم نص بناءً على فاصل معين           |
| type      | func type(x: any): string           | يرجع نوع المتغير كنص (int, string...)  |

---

⚙️ ربط المكتبة مع المُفسّر

عند تنفيذ كود من نوع CallExpression، يُفحص إذا كانت الدالة من المكتبة:

```python
if call["name"] in core_library:
    execute_builtin(call["name"], call["args"])
```

أو يمكن قراءة core.slib وتحويله إلى سجل دوال متاحة:

```python

داخل interpreter.py
corefunctions = loadslib("stdlib/core.slib")
```

---

📁 مكان توثيق المكتبة في الكِتاب

أنشئ فصل جديد:

```bash
docs/ch8_library.md
```

ويحتوي:

- جدول توثيق الدوال الجاهزة  
- استخدام عملي لكل دالة  
- أمثلة مبنية على examples/  
- طريقة الربط مع المُفسّر

---

🧪 مثال عملي من المشروع:

```s
func main() {
    let name: string = input("ما اسمك؟");
    print("مرحبًا يا " + name);
}
```

يفترض أن المفسّر يعرف أن input و print من core.slib ويقوم بتنفيذهما داخليًا.

---

✅ خطوات إنشاء الملف:

1. أنشئ الملف: stdlib/core.slib
2. اكتب فيه جميع الدوال القياسية بتوقيع واضح
3. اربطها داخل interpreter.py كدوال جاهزة
4. وثّقها في docs/ch8_library.md
5. جرّب كل دالة باستخدام أمثلة عملية

