
🎮 الفصل ٣٠ – صناعة لعبة بسيطة باستخدام S/S++

🎯 الهدف:
تصميم لعبة خفيفة مثل “تجنب العقبات” أو “جمع النقاط” باستخدام المكونات الأساسية للغة S/S++، وتطبيق مفاهيم من فصول سابقة مثل الكائنات، الرسومات، الأحداث، والمؤقتات.

---

1️⃣ إعداد اللعبة: شاشة ونافذة

```spp
import graphics;
import input;
import game;

main() {
  Window.create("Pixel Runner", 800, 600);
  RunnerGame.start();
}
```

- Window.create: تنشئ واجهة اللعبة.
- RunnerGame.start: تبدأ اللعبة من الكائن الرئيسي.

---

2️⃣ اللاعب: كائن متحرك

```spp
class Player {
  int x = 100;
  int y = 500;

  method move(int dx) {
    x += dx;
    if (x < 0) x = 0;
    if (x > 760) x = 760;
  }

  method draw() {
    Graphics.rect(x, y, 40, 40, color.blue);
  }
}
```

🔹 اللاعب يتحرك يمين ويسار ويتفاعل مع المدخلات.

---

3️⃣ العقبات: كائنات ساقطة

```spp
class Obstacle {
  int x;
  int y = 0;

  constructor(int startX) {
    x = startX;
  }

  method update() {
    y += 5;
    if (y > 600) {
      y = 0;
      x = rand(0, 760);
    }
  }

  method draw() {
    Graphics.rect(x, y, 40, 40, color.red);
  }
}
```

🟥 العقبات تنزل من الأعلى وتحاول الاصطدام باللاعب.

---

4️⃣ المنطق الرئيسي: اللعبة نفسها

```spp
class RunnerGame {
  static Player player;
  static list<Obstacle> obstacles;
  static int score = 0;

  static method start() {
    player = new Player();
    obstacles = [new Obstacle(300), new Obstacle(600)];

    loop() {
      Graphics.clear();
      player.draw();

      foreach (obs in obstacles) {
        obs.update();
        obs.draw();
        if (collide(player, obs)) {
          Graphics.text("💥 Game Over", 350, 280, color.white);
          break;
        }
      }

      Graphics.text("Score: " + score, 10, 10, color.yellow);
      score++;

      if (Input.left()) player.move(-10);
      if (Input.right()) player.move(10);

      Graphics.refresh();
      sleep(16);
    }
  }

  static method collide(Player p, Obstacle o) {
    return abs(p.x - o.x) < 40 && abs(p.y - o.y) < 40;
  }
}
```

🏆 اللعبة تستمر وتحتسب النقاط، وتتوقف عند التصادم!

---

🎨 تحسينات مرحة ممكن تضيفها:

- 🎶 صوت انفجار عند نهاية اللعبة
- 🌟 مؤثرات عند جمع النقاط
- 👾 أشكال متغيرة للعقبات
- 🌙 وضع ليلي أو وضع متقدم مع مؤقت

---

✅ النتيجة:
> صنعت لعبة برسومات، تفاعل، عداد نقاط، وتحكم... بلغة واحدة موحدة: S/S++  
> اللعبة ممكن تحويلها إلى تطبيق APK (راجع فصل 21)، أو ربطها بمكتبات حماية (راجع فصل 29).

---
