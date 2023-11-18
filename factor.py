from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Analog Factorial")
window.geometry("1200x600")
window.resizable(width=False, height=False)
window.iconbitmap("F.ico")
window.config(bg="grey")


def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n


class Factorial():

    def __init__(self, N, n):
        self.N = N
        self.n = n
        self.countCollect = []
        self.zero_while = 0

    def Final(self):

        for number in range(1, self.N + 1):
            self.countCollect.append(number)
        # print(self.countCollect)

        for exponent in range(0, len(self.countCollect)):
            self.countCollect[exponent] = self.countCollect[exponent] ** self.n
        # print(self.countCollect)
        if label_x["text"] > label_n["text"]:
            Label(window, text=self.countCollect).pack()

        while self.zero_while < self.n:

            for cycle in range(0, len(self.countCollect)):
                if cycle == len(self.countCollect) - 1:
                    break
                res = abs(self.countCollect[cycle] -
                          self.countCollect[cycle + 1])
                self.countCollect[cycle] = res
            try:
                self.countCollect.pop(-1)
            except IndexError:
                pass
                # print("Показатель степени должен быть меньше основаня!")

            # print(self.countCollect,f" цикл отработал {self.zero_while + 1} раз(а)")

            if label_x["text"] > label_n["text"]:

                Label_output = Label(window, text=self.countCollect)

                if self.countCollect[0] == fac(self.n):
                    Label_output["text"] = f"{self.n}! = {self.countCollect[0]}"

                Label_output.pack()

            else:

                Label_output_warn = Label(
                    window, text="Основание должно быть больше показателя")
                Label_output_warn.place(x=470, y=400)

                break

            self.zero_while = self.zero_while + 1


def get_entry_x():
    try:
        label_x["text"] = int(number_x.get())

        if isinstance(label_n["text"], int) and isinstance(label_x["text"], int):
            # в одной ищ функций можно убрать данный блок if, но удобнее читать, когда их две

            label_success = Label(
                window, text=f"Основание = {label_x['text']} и показатель = {label_n['text']}")
            label_success.place(x=500, y=300)

            for widget in window.winfo_children():
                if isinstance(widget, Label):
                    widget.pack_forget()

            Factorial(label_x["text"], label_n["text"]).Final()

    except ValueError:
        label_x["text"] = "Нужно указать целое число!"
        return label_x


def get_entry_n():
    try:
        label_n["text"] = int(number_n.get())

        if isinstance(label_n["text"], int) and isinstance(label_x["text"], int):

            label_success = Label(
                window, text=f"Основание = {label_x['text']} и показатель = {label_n['text']}")
            label_success.place(x=500, y=300)

            for widget in window.winfo_children():
                if isinstance(widget, Label):
                    widget.pack_forget()

            Factorial(label_x["text"], label_n["text"]).Final()

    except ValueError:
        label_n["text"] = "Нужно указать целое число!"
        return label_n


number_x = Entry()
number_x.place(x=225, y=350)

number_n = Entry()
number_n.place(x=825, y=350)


button_x = Button(window, text="Ввод основания", command=get_entry_x)
button_x.place(x=240, y=400)

button_n = Button(window, text="Ввод показателя", command=get_entry_n)
button_n.place(x=840, y=400)


label_x = Label(window, text="No Data", width=22, height=5)
label_x.place(x=210, y=250)  # вывод значения основания

label_n = Label(window, text="No Data", width=22, height=5)
label_n.place(x=810, y=250)  # вывод значения показателя


window.mainloop()
