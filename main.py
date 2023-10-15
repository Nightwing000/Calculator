from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=25, borderwidth=5 )
e.grid(row=0, column=0, columnspan=3)

mem = Label(root, width=15, text="Memory", )
mem.grid(row=0, column=5, columnspan= 3)


def Button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def Button_clear():
    e.delete(0, END)


def Button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def Button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(first_number)
    e.delete(0, END)


def Button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)


def Button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)


def Button_deci(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def Button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtract":
        e.insert(0, f_num - float(second_number))
    if math == "multiply":
        e.insert(0, f_num * float(second_number))
    if math == "divide":
        e.insert(0, f_num / float(second_number))

def Memstore():
    e.get()



button0 = Button(root, text="0", padx=20, pady=10, command=lambda: Button_click(0))
button1 = Button(root, text="1", padx=20, pady=10, command=lambda: Button_click(1))
button2 = Button(root, text="2", padx=20, pady=10, command=lambda: Button_click(2))
button3 = Button(root, text="3", padx=20, pady=10, command=lambda: Button_click(3))
button4 = Button(root, text="4", padx=20, pady=10, command=lambda: Button_click(4))
button5 = Button(root, text="5", padx=20, pady=10, command=lambda: Button_click(5))
button6 = Button(root, text="6", padx=20, pady=10, command=lambda: Button_click(6))
button7 = Button(root, text="7", padx=20, pady=10, command=lambda: Button_click(7))
button8 = Button(root, text="8", padx=20, pady=10, command=lambda: Button_click(8))
button9 = Button(root, text="9", padx=20, pady=10, command=lambda: Button_click(9))


button_add = Button(root, text="+", padx=20, pady=10, command=Button_add)
button_clear = Button(root, text="C", padx=20, pady=10, command=Button_clear)
button_equal = Button(root, text="=", padx=20, pady=10, command=Button_equal)
button_decimal_point = Button(root, text=u'\u002E', padx=20, pady=10, command=lambda: Button_deci("."))
button_subtract = Button(root, text="-", padx=20, pady=10, command=Button_subtract)
button_multiply = Button(root, text="X", padx=20, pady=10, command=Button_multiply)
button_divide = Button(root, text="/", padx=20, pady=10, command=Button_divide)


button_mclear = Button(root, text="MC", padx=15, pady=10, command=lambda: Button_click(9))
button_mplus = Button(root, text="M+", padx=15, pady=10, command=lambda: Button_click(9))
button_mminus = Button(root, text="M-", padx=15, pady=10, command=lambda: Button_click(9))
button_mstore = Button(root, text="MS", padx=15, pady=10, command=lambda: Button_click(9))
button_mrecall = Button(root, text="MR", padx=15, pady=10, command=lambda: Button_click(9))


button0.grid(row=5, column=1)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_add.grid(row=2, column=3)
button_equal.grid(row=5, column=2)
button_clear.grid(row=2, column=4)
button_decimal_point.grid(row=5, column=0)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)

button_mclear.grid(row =1 , column =0 )
button_mplus.grid(row =1 , column =1)
button_mminus.grid(row =1 , column =2)
button_mstore.grid(row =1 , column =3)
button_mrecall.grid(row = 1, column = 4)

root.mainloop()
