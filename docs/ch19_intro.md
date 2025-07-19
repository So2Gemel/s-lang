🎮 الفصل 19 – صنع لعبة بلغة S/S++

✨ الهدف:
بناء لعبة تفاعلية (مثل لعبة تجنب العقبات) باستخدام أساسيات لغة S/S++، وتجربة الذكاء في كتابة الكود وتنظيمه بطريقة احترافية.

---

1️⃣ الإعداد المبدئي
```s++
import system;
import graphics;
import input;
import game;

main() {
  Window.create("Avoider Game", 800, 600);
  Game.start();
}
```

- Window.create: تفتح نافذة اللعب.
- Game.start: تبدأ منطق اللعبة.

---

2️⃣ إنشاء الكائنات الأساسية
```s++
class Player {
  int x, y;
  constructor() {
    x = 100;
    y = 500;
  }
  method draw() {
    Graphics.rect(x, y, 40, 40, color.blue);
  }
  method move(int dx) {
    x += dx;
    if (x < 0) x = 0;
    if (x > 760) x = 760;
  }
}
```

---

3️⃣ العقبات المتحركة
```s++
class Obstacle {
  int x, y;
  constructor(int startX) {
    x = startX;
    y = 0;
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

---

4️⃣ منطق اللعبة الأساسي
```s++
class Game {
  static Player player;
  static list<Obstacle> obstacles;

  static method start() {
    player = new Player();
    obstacles = [new Obstacle(200), new Obstacle(400)];
    
    loop() {
      Graphics.clear();
      player.draw();
      foreach (obs in obstacles) {
        obs.update();
        obs.draw();
        if (collide(player, obs)) {
          Graphics.text("Game Over!", 350, 300, color.white);
          break;
        }
      }

      if (Input.left()) player.move(-10);
      if (Input.right()) player.move(10);

      Graphics.refresh();
      sleep(16);
    }
  }
}
```

---

5️⃣ وظيفة الاصطدام
```s++
method collide(Player p, Obstacle o) {
  return abs(p.x - o.x) < 40 && abs(p.y - o.y) < 40;
}
```

---
