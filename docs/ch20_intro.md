📱 الفصل 20 – كيف تبني تطبيق بلغة S/S++

✨ الهدف:
تعلم بناء تطبيق يعرض واجهة رسومية، يستقبل مدخلات، ويتفاعل مع المستخدم بلغة S/S++، خطوة بخطوة.

---

1️⃣ إنشاء الهيكل الأساسي
```s++
import system;
import gui;

main() {
  App.create("S/S++ Notes", 400, 600);
  UI.init();
}
```

- App.create: تنشئ التطبيق مع عنوان وحجم.
- UI.init: تبدأ واجهة المستخدم.

---

2️⃣ تصميم الواجهة
```s++
class UI {
  static TextBox input;
  static List notes;

  static method init() {
    input = new TextBox(10, 10, 380);
    Button addBtn = new Button("Add", 300, 50, 80);
    addBtn.onClick = UI.addNote;

    notes = [];
  }

  static method addNote() {
    if (input.text != "") {
      notes.append(input.text);
      input.clear();
    }
  }

  static method draw() {
    input.draw();
    Graphics.text("Notes:", 10, 90, color.black);
    int y = 120;
    foreach (note in notes) {
      Graphics.text("- " + note, 20, y, color.darkGray);
      y += 20;
    }
  }
}
```

---

3️⃣ تحديث واجهة التطبيق تلقائيًا
```s++
App.loop(() => {
  Graphics.clear();
  UI.draw();
  Graphics.refresh();
  sleep(16);
});
```

---

4️⃣ التعامل مع اللمس والمدخلات
يمكنك إضافة:
```s++
if (Input.touch()) {
  // التفاعل مع الأزرار أو العناصر
}
```

---

✅ النتيجة:
تطبيق بسيط لتدوين الملاحظات، بواجهة رسومية، مدخل نصي، وزر لإضافة المحتوى. قابل للتوسع بسهولة.

---

🚀 أفكار للتوسعة لاحقًا:
- 🔒 حماية الملاحظات بكلمة مرور.
- ☁️ مزامنة عبر الإنترنت.
- 🎨 تخصيص الألوان والسمات.
- 📲 تحويله لـ APK في الفصل التالي.

---
