from tkinter import *

root = Tk()
root.title("Calculator")
root['bg'] = "lightgrey"
root.resizable(False, False)
root.iconbitmap("C:/Users/jwald/OneDrive/Desktop/python-files/calc.ico")

global math
global f_num
math = ""
f_num = ""
def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))
def button_add():
    global f_num
    global math
    math = "addition"
    first_num = entry.get()
    f_num = int(first_num)
    entry.delete(0, END)
def times():
    global f_num
    global math
    math = "multiplication"
    first_num = entry.get()
    f_num = int(first_num)
    entry.delete(0, END)
def divide():
    global f_num
    global math
    math = "division"
    first_num = entry.get()
    f_num = int(first_num)
    entry.delete(0, END)
def minus():
    global f_num
    global math
    math = "subtraction"
    first_num = entry.get()
    f_num = int(first_num)
    entry.delete(0, END)
def modulus():
    global f_num
    global math
    math = "subtraction"
    first_num = entry.get()
    f_num = int(first_num)
    entry.delete(0, END)
def button_equal():
    second_num = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, f_num + int(second_num))
    if math == "multiplication":
        entry.insert(0, f_num * int(second_num))
    if math == "subtraction":
        entry.insert(0, f_num - int(second_num))
    if math == "division":
        entry.insert(0, f_num / int(second_num))
c0 = Button(root, text="0", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(0))
c9 = Button(root, text="9", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(9))
c8 = Button(root, text="8", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(8))
c7 = Button(root, text="7", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(7))
c6 = Button(root, text="6", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(6))
c5 = Button(root, text="5", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(5))
c4 = Button(root, text="4", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(4))
c3 = Button(root, text="3", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(3))
c2 = Button(root, text="2", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(2))
c1 = Button(root, text="1", padx=40, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: click(1))
btn_add = Button(root, text="+", padx=38, pady=28, bg="silver", fg="black", borderwidth=2, command=button_add)
times = Button(root, text="*", padx=39, pady=28, bg="silver", fg="black", borderwidth=2, command=times)
minus = Button(root, text="-", padx=39, pady=28, bg="silver", fg="black", borderwidth=2, command=minus)
divide = Button(root, text="/", padx=39, pady=28, bg="silver", fg="black", borderwidth=2, command=divide)
btn_equal = Button(root, text="=", padx=39, pady=28, bg="silver", fg="black", borderwidth=2, command=button_equal)
clr = Button(root, text="Clear", padx=30, pady=28, bg="silver", fg="black", borderwidth=2, command=lambda: entry.delete(0, END))

entry = Entry(root, width=35, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, pady=10)

c7.grid(row=1, column=0)
c8.grid(row=1, column=1)
c9.grid(row=1, column=2)

c4.grid(row=2, column=0)
c5.grid(row=2, column=1)
c6.grid(row=2, column=2)

c1.grid(row=3, column=0)
c2.grid(row=3, column=1)
c3.grid(row=3, column=2)

c0.grid(row=4, column=1)
clr.grid(row=4, column=0)
btn_equal.grid(row=4, column=2)
btn_add.grid(row=4, column=3)

divide.grid(row=1, column=3)
minus.grid(row=2, column=3)
times.grid(row=3, column=3)
btn_add.grid(row=4, column=3)
root.mainloop()