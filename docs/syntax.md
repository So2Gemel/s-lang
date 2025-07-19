# 🔤 قواعد الكتابة في لغة S/S++

هذا الملف يشرح القواعد الأساسية للغة البرمجة S وسلسلتها المتقدمة S++. يشمل طريقة تعريف المتغيرات، الدوال، الأصناف، التحكم بالتدفق، والاستدعاء المعياري.

---

## ✍️ تعريف المتغيرات

```s
let x: int = 5;
let name: string = "So2_gemel";
let isReady: bool = true;
let pi: float = 3.14;
```



🧠 تعريف الدوال
```s
func greet(name: string): string {
    return "Hello " + name;
}
```
•الدوال تستخدم func
•الوسائط تُعرّف بالنوع
•النوع المعاد يُكتب بعد الأقواس


🖥️ نقطة الدخول الأساسية
```s
func main() {
    print("Hello from S!");
}```

🔁 التحكم بالتدفق
الشروط:
```s
if x > 10 {
    print("x كبير");
} else {
    print("x صغير");
}```
الحلقات:
```s
for i in 0..5 {
    print(i);
}

while isReady {
    print("جاهز");
}
```

📦 تنظيم الكود إلى Modules
```s
module Tools;

func sayHi(): string {
    return "Hi";
}
```
ثم في ملف آخر:
```s
use Tools;
print(sayHi());```

🎭 الأصناف (S++ فقط)
```s++
class Person {
    let name: string;

    func __init__(n: string) {
        self.name = n;
    }

    func greet(): string {
        return "مرحبًا " + self.name;
    }
}```

الملاحظات:
- self تشير إلى الكائن الحالي
- الدالة init تُستخدم للبناء

---

🧰 الدوال القياسية

| الدالة     | الوصف               |
|------------|---------------------|
| print()  | طباعة على الشاشة    |
| input()  | إدخال من المستخدم   |
| len()    | طول القائمة أو النص |
| type()   | معرفة نوع المتغير   |

---

⚠️ قواعد إضافية

- التعليقات تبدأ بـ # أو //
- كل أمر يُختم بـ ;
- الكتل تُكتب بين {}

---

🧪 مثال شامل

```s
func main() {
    let name: string = input("اسمك؟");
    if name == "So2_gemel" {
        print("أهلاً يا المعماري 👑");
    } else {
        print("مرحبًا " + name);
    }
}
```

---
