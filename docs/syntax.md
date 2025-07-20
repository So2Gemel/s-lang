📘 syntax.md — التوثيق الرسمي لهيكل لغة S/S++
> الإصدار: v1.0.9 • التاريخ: 2025-07-20 • المؤلف: مطور سانجي/سيفارو

---

🔰 الأقسام الأساسية

| القسم | الوصف |
|-------|------|
| الكلمات المفتاحية | method, class, main, loop, safe, go, return, import |
| الأنواع | int, float, string, bool, list, map, any, void |
| بناء دالة | تعريف دالة باستخدام method مع نوع عائد، باراميتر، ونص تنفيذ |
| بناء كلاس | تعريف صنف باستخدام class مع خصائص ودوال مرتبطة |
| التحكم بالتدفق | دعم if, else, loop, break, continue, switch |
| التوصيل الخارجي | دعم import من slib: أو compiler: أو system: أو plugin: |
| الأمن | كتلة safe { ... } لحماية الكود من التنفيذ الخطر |
| التنفيذ المباشر | استخدام main() أو go للتنفيذ عند تشغيل الملف |
| واجهات | دعم GUI, HUD, ImGui, Prompt, عبر مكتبات رسمية |
| التعليق | باستخدام // تعليق أو / تعليق متعدد /

---

⚙️ أمثلة نحوية موسوعية

🎯 تعريف دالة

```spp
method multiply(int a, int b) => a * b;
```

🧠 تعريف صنف

```spp
class Counter {
  int count = 0;

  method increment() {
    count += 1;
  }

  method reset() => count = 0;
}
```

📦 الاستيراد من مكتبة رسمية

```spp
import slib:slibmath
import slib:slibcore
```

🔁 تنفيذ حلقة باستخدام loop

```spp
loop (int i = 0; i < 5; i++) {
  print("🔢 الرقم: " + i);
}
```

⛔ كتلة آمنة لمنع التهديدات

```spp
safe {
  system.exec("ls -l");
  slibcrypto.encryptFile("secret.txt", "key123");
}
```

---

📚 أنواع البيانات الحديثة (آخر توسع)

| النوع | الوصف | مثال |
|-------|-------|-------|
| map<string, any> | جدول بيانات قابل للتحليل | {"user": "So2", "rank": 7} |
| list<float> | قائمة رقمية | [1.2, 3.5, 6.7] |
| any | نوع عام لا يُقيد القيمة | any x = 42 or "hello" |

---

🧩 أساليب التوسع الجديدة

- 📎 دعم الدوال المختصرة: method add(a, b) => a + b;
- 🧠 دعم المحرر الذكي داخل IDE: @suggest, @readonly, @hidden
- 📦 دعم التوسعات داخل الملفات .smod و .splugin
- 🔌 دعم تحميل تلقائي للمكتبات من خلال sis, spm
- 🎨 دعم عناصر واجهة من النوع Button, Panel, Slider, TextBox
- 🧾 دعم تحويل AST داخليًا داخل مشاريع المترجم الرسمي

---

🧠 شروط الترجمة داخل المترجم الرسمي S/S++

- كل ملف .spp يجب أن يحتوي على دالة main() أو استخدام go
- لا يُسمح باستخدام دوال داخل safe تستدعي rm, eval, fork, :(){:|:&};: إلا من خلال inject داخل slibhook
- كل مكتبة slibXXX يجب أن تكون مُعرّفة داخل meta.sinfo ومربوطة في stdlib.lock

---

✨ ملاحظات مهمة

- التعليقات المتعددة مسموحة: / شرح هنا /
- يمكن استخدام emoji داخل الكود: "✅ نجاح"
- الألوان داخل HUD/GUI تعتمد على نوع string من مكتبة slibhud
- دعم method داخل class يعرض this تلقائيًا
- الكلمات المحجوزة لا يجب استخدامها كمتغير: loop, class, return

---
