📘 الفصل 5: بناء مشاريع عملية باستخدام لغة S/S++

---

🎯 لماذا المشاريع العملية؟

تطبيق المعرفة النظرية في مشاريع حقيقية هو الوسيلة الأقوى لتثبيت المفاهيم، واكتشاف الثغرات، وتحسين التصميم.  
لغة S/S++ تم تصميمها لتكون مناسبة لتطبيقات متنوعة: أدوات صغيرة، برامج سطح المكتب، أنظمة تعليمية، وحتى واجهات رسومية لاحقًا.

---

🧮 المشروع 1: آلة حاسبة بسيطة

✅ الفكرة:

تطبيق يحسب العمليات الرياضية الأربعة بناءً على المُدخلات.

💻 الكود:

```s
func add(a: int, b: int): int {
    return a + b;
}

func sub(a: int, b: int): int {
    return a - b;
}

func main() {
    let x: int = 10;
    let y: int = 5;

    print("مجموع: " + add(x, y));
    print("فرق: " + sub(x, y));
}
```

---

📓 المشروع 2: مدونة نصية (Text Logger)

✅ الفكرة:

برنامج يحتفظ بقائمة نصوص ويعرضها لاحقًا.

💻 الكود:

```s++
class Logger {
    let logs: list<string>;

    func init() {
        self.logs = [];
    }

    func add(msg: string) {
        self.logs.push(msg);
    }

    func show() {
        for i in 0..len(self.logs) {
            print("[" + i + "]: " + self.logs[i]);
        }
    }
}

func main() {
    let log: Logger = new Logger();
    log.add("بدأ البرنامج");
    log.add("تمت إضافة سجل جديد");
    log.show();
}
```

---

🧠 المشروع 3: أداة تحليل النصوص

✅ الفكرة:

تحليل عدد الكلمات والحروف في نص مدخل.

```s
func countWords(text: string): int {
    return len(text.split(" "));
}

func countChars(text: string): int {
    return len(text);
}

func main() {
    let msg: string = "لغة S تبني مستقبل البرمجة";
    print("كلمات: " + countWords(msg));
    print("أحرف: " + countChars(msg));
}
```

---

🚀 نصائح لتنظيم المشاريع:

- ضع كل مشروع في مجلد داخل examples/
- أضف ملف AST لكل مثال في ast_samples/
- أرفق شرح داخل docs/ch5_projects.md لكل مشروع

---
