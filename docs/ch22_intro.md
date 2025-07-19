🧩 الفصل 22 – كيف تصنع مكتبات وملفات slibاسم.so بلغة S/S++

🎯 الهدف:
إنشاء مكتبات ذكية بصيغة .slibاسم.so تحتوي على وظائف محددة يمكن استدعاؤها داخل أي مشروع، مما يزيد من إعادة الاستخدام، الحماية، والتنظيم.

---

1️⃣ هيكل مشروع المكتبة

```text
MyLibrary/
├── math.spp
├── tools.spp
├── build.spp
├── slib/
│   └── libmath.slibmath.so
```

- math.spp: يحتوي دوال رياضية.
- tools.spp: يحتوي أدوات مساعدة.
- build.spp: ملف تجميع.
- slib/: مجلد لحفظ المكتبة الناتجة باسم slibاسم.so.

---

2️⃣ مثال على محتوى math.spp

```spp
module math;

method add(int a, int b) {
  return a + b;
}

method multiply(int a, int b) {
  return a * b;
}
```

---

3️⃣ ملف tools.spp

```spp
module tools;

method greet(string name) {
  return "Welcome " + name + "!";
}
```

---

4️⃣ ملف البناء build.spp

```spp
build {
  inputs = ["math.spp", "tools.spp"];
  output = "slib/libmath.slibmath.so"; // التسمية الصحيحة
  target = "library";
  name = "libmath";
}
```

---

5️⃣ توليد المكتبة باستخدام أداة البناء sbuild

```bash
sbuild build.spp
```

💥 النتيجة:
```
slib/libmath.slibmath.so
```

مكتبة خارجية جاهزة للاستدعاء.

---

6️⃣ استخدام المكتبة داخل تطبيق S/S++

```spp
import slib:libmath;

main() {
  int x = math.add(6, 4);
  int y = math.multiply(3, 5);
  string msg = tools.greet("So2");
  print(x);   // 10
  print(y);   // 15
  print(msg); // Welcome So2!
}
```

---

💡 ملاحظات مهمة:

- 📦 يمكن تقسيم المكتبات حسب الوظيفة (libmath، libnet، libui).
- 🔐 ملفات .slibاسم.so قابلة للتشفير والحماية ضد الهندسة العكسية.
- 🚀 مكتبتك يمكن مشاركتها على GitHub كـ “إضافات S/S++”.
- 🧠 يمكن استخدام المكتبات في لعبة (فصل 19) أو تطبيق (فصل 20–21) لتقليل التكرار.

---

✅ النتيجة:
إنشاء مكتبة احترافية بصيغة slibاسم.so يُعتبر أحد أقوى ميزات لغة S/S++، ويمهّد لتكوين نظام وحدات قوي وقابل للنشر عالميًا.

---
