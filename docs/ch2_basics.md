

✍️ تعريف المتغيرات

لغة S تسمح لك بإنشاء متغيرات باستخدام الكلمة المفتاحية let. يُكتب اسم المتغير، نوعه، ثم قيمته.

✅ الشكل العام:

```s
let المتغير: النوع = القيمة;
```

🧪 أمثلة عملية:

```s
let age: int = 25;
let pi: float = 3.14;
let isReady: bool = true;
let name: string = "So2_gemel";
```

---
🧠 أنواع البيانات المدعومة

| النوع     | الوصف                            | مثال             |
|-----------|-----------------------------------|------------------|
| int     | عدد صحيح                          | let x: int = 5; |
| float   | عدد عشري                          | let y: float = 1.5; |
| bool    | منطقي: true أو false         | let ok: bool = false; |
| string  | نص                                 | let msg: string = "Hello"; |
| list<T> | قائمة تحتوي عناصر من نوع T       | let nums: list<int> = [1, 2, 3]; |
| map<K,V>| خريطة مفتاح ↔ قيمة               | let dict: map<string,int> = {"a":1}; |

---
📢 الطباعة

تستخدم print() لعرض النصوص على الشاشة.

📌 أمثلة:

```s
print("مرحبًا بلغتي الجديدة!");
```

✨ دمج نص + متغير:

```s
let name: string = "So2_gemel";
print("أهلاً يا " + name);
```

---

🛠️ تمرين عملي

اكتب برنامجًا يعرّف الاسم والعمر، ويطبع رسالة ترحيب:

```s
func main() {
    let name: string = "So2_gemel";
    let age: int = 23;
    print("مرحبًا " + name);
    print("عمرك هو " + age);
}
```
