📲 الفصل 21 – تحويل تطبيق بلغة S/S++ إلى ملف APK

🎯 الهدف:
إنشاء مشروع تطبيق بلغة .spp وتحويله إلى ملف APK جاهز للتثبيت على أجهزة Android باستخدام أدوات من بيئة S/S++.

---

1️⃣ هيكل المشروع
```text
MyApp/
├── main.spp
├── manifest.xml
├── assets/
│   └── icon.png
├── build.spp
```

- main.spp: يحتوي منطق التطبيق.
- manifest.xml: معلومات الحزمة والتصاريح.
- build.spp: إعدادات التصدير.
- assets/: ملفات الصور والموارد.

---

2️⃣ كود التطبيق داخل main.spp
```spp
import system;
import gui;

main() {
  App.create("S Notes", 400, 600);
  UI.init();
}

class UI {
  static TextBox input;
  static List notes;

  static method init() {
    input = new TextBox(10, 10, 380);
    Button addBtn = new Button("Add", 310, 60, 80);
    addBtn.onClick = UI.save;

    notes = [];
  }

  static method save() {
    if (input.text != "") {
      notes.append(input.text);
      input.clear();
    }
  }

  static method draw() {
    input.draw();
    Graphics.text("Your Notes:", 10, 100, color.black);
    int y = 130;
    foreach (note in notes) {
      Graphics.text("- " + note, 20, y, color.gray);
      y += 20;
    }
  }
}

App.loop(() => {
  Graphics.clear();
  UI.draw();
  Graphics.refresh();
  sleep(16);
});
```

---

3️⃣ ملف manifest.xml
```xml
<manifest>
  <package name="com.slang.snotes" />
  <app label="S Notes" icon="icon.png" />
  <activity name="MainActivity" />
  <permissions>
    <permission name="INTERNET" />
  </permissions>
</manifest>
```

---

4️⃣ ملف البناء build.spp
```spp
build {
  input = "main.spp";
  output = "SNotes.apk";
  manifest = "manifest.xml";
  assets = ["assets/"];
  target = "apk";
}
```

---

5️⃣ التصدير باستخدام أداة sbuild
```bash
sbuild build.spp
```

☑️ بعد التشغيل، سيظهر الملف الناتج:  
output/SNotes.apk

---

6️⃣ تجربة التطبيق
- انقل الملف إلى هاتفك باستخدام USB أو Wi-Fi.
- فعّل “التثبيت من مصادر غير معروفة”.
- ثبت التطبيق وابدأ التفاعل مع الملاحظات مباشرة 🎉

---

🧠 تلميحات احترافية:
- يمكنك لاحقًا توقيع الملف SNotes.apk باستخدام أدوات توقيع خاصة بـ S/S++.
- أضف مكتبات .slib.so لتوسيع الوظائف (فصل 22 🔜).
- أنشئ واجهات بـ Dark Mode أو واجهات متغيرة حسب اللغة.

---

✅ النتيجة:
أنت الآن رسميًا مطوّر Android بلغة S/S++!  
تحويل الكود إلى تطبيق حقيقي بصيغة .apk يفتح الباب للنشر، التوزيع، والتجربة العالمية 🌍

