from tkinter import *
import random


foto_list = ["pic\\Валгамаа.png", "pic\\Вильяндимаа.png", "pic\\Вырумаа.png", "pic\\Ида-Вирумаа.png", "pic\\Йыгевамаа.png"
        , "pic\\Лээне-Вирумаа.png", "pic\\Ляэнемаа.png", "pic\\Пылвамаа.png", "pic\\Пярнумаа.png",
                 "pic\\Рапламаа.png", "pic\\Сааремаа.png", "pic\\Тартумаа.png", "pic\\Харьюмаа.png",
                 "pic\\Хийумаа.png", "pic\\Ярвамаа.png"]

foto_list1 = ["pic1\\Castillo.png","pic1\\Colosseum.png","pic1\\GreatWallNearBeijingWinter.png","pic1\\Machu_Picchu.png","pic1\\Petra.png",]

foto_list2 = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль ","Август ","Сентябрь ","Октябрь  ","Ноябрь  ","Декабрь  "]
foto3 = foto_list2.copy()



def func():
    global tk, can


    def list_to_txt(event):
        global can, foto  # ----------------
        txt.delete(0.0, END)
        valik = lbox.curselection()
        txt.insert(END, lbox.get(valik[0]))
        can.delete(ALL)  # ---------------
        foto = PhotoImage(file=foto_list[valik[0]])  # -------------
        can.create_image(0, 0, image=foto, anchor=NW)  # -----------------

    def txt_to_list(event):
        text = txt.get(0.0, END)
        text = text[-2:-1]
        if text == "\n":
            pass
        else:
            foto_list.append(text)
            print(foto_list)
            lbox.config(height=len(foto_list))
            lbox.insert(END, text)
            txt.delete(0.0, END)

    win = Toplevel()
    win["bg"] = color1
    win.geometry("600x400")
    lbox = Listbox(win, width=20, height=len(foto_list), selectmode=SINGLE)
    for element in foto_list:
        lbox.insert(END, element[4:])
    lbox.grid(row=0, column=0)
    lbox.bind("<<ListboxSelect>>", list_to_txt)
    txt = Text(win, height=1, width=20, wrap=WORD)
    txt.grid(row=1, column=1)
    txt.bind("<Return>", txt_to_list)
    can = Canvas(win, width=300, height=200, bg="gold")  # --------------
    can.grid(row=0, column=1, columnspan=2)  # --------------------
    foto = PhotoImage(file="pic\\Валгамаа.png")  # ----------------
    can.create_image(0, 0, image=foto, anchor=NW)  # -----------------
    win.mainloop()

def func1():
    global tk, can


    def list_to_txt(event):
        global can, foto  # ----------------
        txt.delete(0.0, END)
        valik = lbox.curselection()
        txt.insert(END, lbox.get(valik[0]))
        can.delete(ALL)  # ---------------
        foto = PhotoImage(file=foto_list1[valik[0]])  # -------------
        can.create_image(0, 0, image=foto, anchor=NW)  # -----------------

    def txt_to_list(event):
        text = txt.get(0.0, END)
        text = text[-2:-1]
        if text == "\n":
            pass
        else:
            foto_list.append(text)
            print(foto_list1)
            lbox.config(height=len(foto_list1))
            lbox.insert(END, text)
            txt.delete(0.0, END)

    win = Toplevel()
    win["bg"] = color1
    win.geometry("600x400")
    lbox = Listbox(win, width=20, height=len(foto_list1), selectmode=SINGLE)
    for element in foto_list1:
        lbox.insert(END, element[5:])
    lbox.grid(row=0, column=0)
    lbox.bind("<<ListboxSelect>>", list_to_txt)
    txt = Text(win, height=1, width=20, wrap=WORD)
    txt.grid(row=1, column=1)
    txt.bind("<Return>", txt_to_list)
    can = Canvas(win, width=300, height=200, bg="gold")  # --------------
    can.grid(row=0, column=1, columnspan=2)  # --------------------
    foto = PhotoImage(file=foto_list1[0])  # ----------------
    can.create_image(0, 0, image=foto, anchor=NW)  # -----------------
    win.mainloop()

def func2():
    global tk, can, lbox, win
    def add():
        print(foto3)
        global lbox
        if len(foto3) == 12:
            print("asd")
        elif len(foto3) != 12:
            for i in foto_list2:
                for j in foto3:
                    if i not in foto3:
                        lbox.insert(0, i)
                        foto3.append(i)
    
    def random1():
        rn = random.randint(0, len(foto3)-1)
        if rn % 2:
            tx = Label(win, text=f"{foto3[rn]} % 2").grid(row=11, column=0)
        else:
            tx = Label(win, text=f"{foto3[rn]} else").grid(row=11, column=0)

    def random2():
        rn = random.randint(0, len(foto3)-1)
        tx = Label(win, text=f"{rn}").grid(row=13, column=0)

    def listb():

        tk1 = Toplevel()
        r = 0
        for i in range(len(foto_list2)):
            c = Checkbutton(tk1, text = foto_list2[r], width=10).grid(column=3, row=r)
            r += 1


    def list_to_txt(event):
        global can, foto  # ----------------
        valik = lbox.curselection()

    def txt_to_list(event):
        text = txt.get(0.0, END)
        text = text[-2:-1]
        if text == "\n":
            pass
        else:
            foto_list.append(text)
            print(foto_list2)
            lbox.config(height=len(foto_list2))
            lbox.insert(END, text)
            txt.delete(0.0, END)

    win = Toplevel()
    win["bg"] = color1
    win.geometry("600x400")
    lbox = Listbox(win, width=20, height=len(foto_list2), selectmode=SINGLE)
    for element in foto_list2:
        lbox.insert(END, element)

    lbox.grid(row=0, column=0)
    lbox.bind("<<ListboxSelect>>", list_to_txt)
    Button(win, text="Удалить", width=20, height=1, font="Arial 9", bg=color2, command=lambda: (lbox.delete(0, 0), foto3.pop(0))).grid(row=6, column=0)
    Button(win, text="Добавить", width=20, height=1, font="Arial 9", bg=color2, command=add).grid(row=7, column=0)
    Button(win, text="Случайная месяц", width=20, height=1, font="Arial 9", bg=color2, command=random1).grid(row=8, column=0)
    Button(win, text="Случайная цисло", width=20, height=1, font="Arial 9", bg=color2, command=random2).grid(row=9, column=0)
    Button(win, text="Listbox", width=20, height=1, font="Arial 9", bg=color2, command=listb).grid(row=10, column=0)
    win.mainloop()

tk = Tk()
font1 = "Arial 16"
color1 = "#e56b6f"
color2 = "#f4f1de"
tk.geometry("490x200")
tk["bg"] = color1
tk.title("Table")

Label(text="Нажми на кнопку", width=70).grid(row=0, column=0, columnspan=10)
Frame(width=20, height=170, bg=color1).grid(row=2, column=0, rowspan=3)
Button(text="Уезды Эстонии", width=20, height=2, font="Arial 9", bg=color2, command=func).grid(row=2, column=1)
Button(text="чудес света", width=20, height=2, font="Arial 9", bg=color2, command=func1).grid(row=2, column=2)
Button(text="месяцы года", width=20, height=2, font="Arial 9", bg=color2, command=func2).grid(row=3, column=1)
Button(text=" знаки зодиака", width=20, height=2, font="Arial 9", bg=color2).grid(row=3, column=2)
Button(text="Европейские города", width=20, height=2, font="Arial 9", bg=color2).grid(row=4, column=1)
Button(text="фигуры", width=20, height=2, font="Arial 9", bg=color2).grid(row=4, column=2)
Button(text="цветов", width=20, height=2, font="Arial 9", bg=color2).grid(row=2, column=3)

tk.mainloop()
