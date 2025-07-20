📘 الفصل ٤٥ – دعم واجهات HUD و ImGui داخل لغة S/S++
> الواجهات الرسومية الفورية + طبقات العرض التفاعلية + أدوات التطوير البصري

---

🎯 هدف الفصل

هذا الفصل يضيف التوسعات التالية للغة:

1. 🎨 دعم مكتبة ImGui لواجهات التطوير الفوري داخل التطبيق
2. 🧭 دعم HUD (Heads-Up Display) لعرض البيانات الحية فوق التطبيقات والألعاب
3. ⚙️ توسيع أدوات الرسم، التحكم، والعرض داخل IDE وملفات .spp
4. 📦 ربط كل هذا بمكتبات رسمية مثل slibgui, slibhud, و slibimgui

---

🎨 1. مكتبة ImGui – واجهة المبرمجين الأنيقة

🔹 ImGui تُستخدم في أدوات مثل Unreal Engine, Godot, وDevTools

🧱 تركيب الواجهة:

```spp
import slib:slibimgui

main() {
  ImGui.begin("⚙️ إعدادات المشروع");

  ImGui.text("أدخل اسم المشروع:");
  string name = ImGui.input("ProjectName", "MyApp");

  if (ImGui.button("✅ إنشاء")) {
    Builder.create(name);
  }

  ImGui.end();
}
```

🎯 هذا النوع من الواجهات يُستخدم لبناء أدوات تحليل، محركات ألعاب، ومحررات داخلية.

---

🧭 2. HUD – طبقة العرض الفورية داخل التطبيقات والألعاب

🔹 HUD تعرض بيانات حيّة دون تعطيل الرسم أو التفاعل

📦 مثال داخل لعبة:

```spp
import slib:slibhud

main() {
  HUD.text("🧠 الطاقة: 92%", 10, 10, color.green);
  HUD.text("🕓 الوقت: " + system.time(), 10, 40, color.cyan);
}
```

🔹 تُستخدم داخل loop() دون التأثير على الحركة أو الأحداث.

---

🖼️ 3. أدوات التصميم داخل IDE – محرر رسومي عبر S/S++

🔧 تم إضافة وظائف مثل:

| الأداة | الوظيفة |
|--------|----------|
| UIDesigner.drawPanel() | إنشاء لوحات قابلة للتحكم |
| HUD.attach() | ربط البيانات الحية بالمراقبة |
| ImGui.slider() | تعيين متغيرات رسومية |
| Preview.render() | عرض حي لمكونات المشروع |

🎮 مثال واجهة إعدادات متقدمة:

```spp
ImGui.begin("🎮 إعدادات التحكم");
int speed = ImGui.slider("السرعة", 1, 100, default = 30);
HUD.text("🔄 السرعة الحالية: " + speed, 300, 10, color.yellow);
```

---

📦 4. توثيق كل مكتبة رسمية

```text
slibimgui/
├── ImGui.slib
├── docs.md
├── examples/ImGuiEditor.spp

slibhud/
├── HUD.slib
├── samples/HUDGame.spp

slibgui/
├── UI.slib
├── assets/icons, buttons
```

📚 كل مكتبة موثقة داخل stdlib-spp, وتُدار عبر spm و sis install slibimgui

---

🧩 مشروع متكامل من الفصل ٤٥

```spp
safe {
  HUD.text("⚡ FPS: " + system.fps(), 10, 10, color.green);
  ImGui.begin("📊 مراقبة اللعبة");
  int level = ImGui.slider("Level", 1, 10, 3);
  if (ImGui.button("🔁 إعادة")) {
    Game.restart(level);
  }
  ImGui.end();
}
```

✅ يتم استخدام HUD + ImGui + Slider + حماية تنفيذ + أداء حي داخل مشروع واحد

---

✅ النتيجة

> الفصل ٤٥ يحوّل لغة S/S++ إلى منصة تصميم واجهات متكاملة — لكل من الألعاب، الأدوات، المحررات، والتعليم البصري  
> من الآن، لم يعد المشروع مجرد كود… بل تجربة رسومية تفاعلية تُبنى داخل اللغة نفسها

---
