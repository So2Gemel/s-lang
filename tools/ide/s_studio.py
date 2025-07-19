import tkinter as tk
from tkinter import filedialog
import subprocess

class SStudio:
    def __init__(self, root):
        self.root = root
        self.root.title("S-Studio IDE")
        self.text = tk.Text(root, font=("Courier New", 12))
        self.text.pack(fill="both", expand=True)

        # الشريط العلوي
        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="ملف", menu=file_menu)
        file_menu.add_command(label="فتح", command=self.open_file)
        file_menu.add_command(label="حفظ", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="تشغيل", command=self.run_code)

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("S/S++ Files", "*.s *.SPP")])
        if path:
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, code)

    def save_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".s", filetypes=[("S/S++ Files", "*.s *.SPP")])
        if path:
            code = self.text.get(1.0, tk.END)
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)

    def run_code(self):
        code = self.text.get(1.0, tk.END)
        with open("_temp.s", "w", encoding="utf-8") as f:
            f.write(code)
        subprocess.run(["python", "../parser/interpreter.py", "_temp.s"])

if __name__ == "__main__":
    root = tk.Tk()
    ide = SStudio(root)
    root.mainloop()
