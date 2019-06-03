from tkinter import *
from tkinter import messagebox

root = Tk()
root.title(u"Что-то")
root.geometry ("640x480")

def que_one():
    question = Label(root, text="На каком языке программирования это всё написано?")
    answer = Entry()
    btn = Button(root, text="Ответить", command=lambda: game1 (que_two))
    question.grid()
    answer.grid()
    btn.grid()

    def game1(que_two):
        if answer.get().lower() == "питон":
            que_two()
        else:
            messagebox.showerror("Ошибка!", "Попробуй еще раз")


def que_two():
    question_2 = Label(root, text="Хочешь домой?")
    answer_2 = Entry()
    btn_2 = Button(root, text="Ответить", command=lambda: game2 (que_two))
    question_2.grid ()
    answer_2.grid()
    btn_2.grid()

    def game2(que_two):
        if answer_2.get().lower == "да":
            messagebox.showinfo("Победа", "Победа!")
        else:
            messagebox.showerror("Ты ошибся")


que_one()


root.mainloop()