import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import imageio
import random


class NoButton(tk.Button):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.bind('<Enter>', self.move_away)

    def move_away(self, event):
        new_x = random.randint(0, self.master.winfo_width() - self.winfo_width())
        new_y = random.randint(0, self.master.winfo_height() - self.winfo_height())
        self.place(x=new_x, y=new_y)


class LoveCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Открытка")
        self.root.geometry("400x300")  # Установка начального размера окна

        # Загрузка изображения для заднего фона
        self.background_image = Image.open("background.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # self.label = tk.Label(root, text="Я тебя люблю!", font=("Helvetica", 20))
        # self.label.pack(pady=20)

        self.button_yes = tk.Button(root, text="Да", command=self.show_gif)
        self.button_yes.pack(side=tk.LEFT, padx=10)

        self.button_no = NoButton(root, text="Нет")
        self.button_no.pack(side=tk.RIGHT, padx=10)

    def show_gif(self):
        gif_path = "your_gif.gif"  # Укажите имя вашего гиф-изображения

        new_window = tk.Toplevel(self.root)
        new_window.title("Гифка")
        new_window.geometry("450x400")  # Установка размера нового окна

        # Задний фон на новом окне
        background_label = tk.Label(new_window, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        gif = imageio.get_reader(gif_path)
        frames = [ImageTk.PhotoImage(Image.fromarray(frame)) for frame in gif]

        label = tk.Label(new_window, image=frames[0])
        label.image = frames[0]
        label.pack()

        def update_frame(frame_num):
            label.configure(image=frames[frame_num])
            label.image = frames[frame_num]
            new_window.after(100, update_frame, (frame_num + 1) % len(frames))

        update_frame(1)

        # Скрываем исходное окно
        self.root.withdraw()


def main():
    root = tk.Tk()
    love_card = LoveCard(root)
    root.mainloop()


if __name__ == "__main__":
    main()
