🌐 الفصل ٣٣ – كيف تربط S/S++ مع لغات أخرى (C/C++, Python, Go, C#)

🎯 الهدف:
دمج لغة S/S++ مع لغات خارجية للحصول على وظائف إضافية، واجهات متقدمة، أو مكتبات موجودة بالفعل... عبر الربط الديناميكي أو الترجمة البينية.

---

1️⃣ ربط مع C/C++ عبر مكتبات .so

🔧 مثال مكتبة C:
```c
// libmath.c
int add(int a, int b) {
    return a + b;
}
```

ثم تحوّلها إلى مكتبة:

```bash
gcc -shared -fPIC -o libmath.so libmath.c
```

📥 استدعاؤها داخل S/S++:

```spp
import native:libmath;

main() {
  int result = call("add", 3, 7);
  print("Result: " + result); // 10
}
```

✅ تستخدم import native: للربط الديناميكي مع دوال مكتبة C.

---

2️⃣ ربط مع Python عبر واجهة النظام

```spp
main() {
  string output = shell.exec("python3 -c 'print(3 + 7)'");
  print("Python Result: " + output);
}
```

📦 تنفذ كود بايثون من داخل S/S++ وتُحضر الناتج!

---

3️⃣ ربط مع Go عبر مكتبة .so أو تنفيذ مباشر

🔧 مثال Go بسيط:
```go
package main
import "C"
import "fmt"

//export PrintHello
func PrintHello() {
  fmt.Println("Hello from Go!")
}
```

Compile:
```bash
go build -buildmode=c-shared -o libgo.so gofile.go
```

📥 ربط في S/S++:
```spp
import native:libgo;

main() {
  call("PrintHello");
}
```

🧠 تقدر تستفيد من مكتبات Go مثل التشفير أو الشبكات.

---

4️⃣ ربط مع C# عبر .exe أو ملف .dll

📥 تنفيذ مباشر:
```spp
main() {
  shell.exec("dotnet run MyCSharpApp.exe");
}
```

🔁 أو عبر ملف DLL:
```spp
import native:libcsharp;

main() {
  string result = call("GetVersion");
  print("C# version: " + result);
}
```

⚡ تقدر تستخدم كل أدوات واجهة المستخدم، الشبكات، أو AI من بيئة .NET داخل S/S++!

---

🔬 كيف تدير الاتصال بشكل ذكي؟

| الطريقة | مناسبة لـ | الملاحظات |
|---------|------------|------------|
| import native: | C, C++, Go, C# DLL | يحتاج عنوان الدالة بدقة |
| shell.exec() | Python, C#, Bash | مرن ويعمل مع السكريبتات |
| الربط عبر JSON أو ملفات | أي لغة | إرسال واستقبال بيانات |

---

✅ النتيجة:

> لغة S/S++ لم تعد معزولة… بل تندمج مع أبرز لغات العالم لتصنع أدوات هجينة متقدمة، تجمع بين سهولة البرمجة والأداء العالي والتكامل المرن!  
> الآن يمكنك استخدام مكتبة مكتوبة بأي لغة… والتحكم بها من داخل S/S++.
