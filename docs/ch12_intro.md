# 📘 الفصل 12: مشروع مكتمل بلغة S/S++ — إصدار النسخة الرسمية للتعليم

---

## 🎯 ما ستتعلمه في هذا الفصل

في هذا الفصل، سنطبّق كل شيء تعلمناه في الفصول السابقة:  
سنكتب برنامجًا حقيقيًا باستخدام لغة S/S++، ثم نشرحه خطوة بخطوة، ونبين كيف تُصدر مشروع كامل بلغة S.  
هذا الفصل هو تتويج للرحلة التعليمية التي مررنا بها.

---

## 🧱 وصف المشروع

برنامج بسيط يسمى: **دفتر الطالب StudentBook**  
يقوم بـ:

- تخزين بيانات الطالب (اسم، عمر، درجات)  
- حساب المعدل النهائي  
- طباعة تقرير واضح

---

## 🧪 كود المشروع الكامل

```s++
class Student {
    let name: string;
    let age: int;
    let grades: list<float>;

    func init(n: string, a: int, g: list<float>) {
        self.name = n;
        self.age = a;
        self.grades = g;
    }

    func average(): float {
        let sum: float = 0;
        for grade in self.grades {
            sum = sum + grade;
        }
        return sum / len(self.grades);
    }

    func report() {
        print("اسم الطالب: " + self.name);
        print("العمر: " + str(self.age));
        print("عدد المواد: " + str(len(self.grades)));
        print("المعدل النهائي: " + str(self.average()));
    }
}

func main() {
    let s: Student = Student("أحمد", 17, [88.5, 91.0, 76.5, 82.0]);
    s.report();
}
