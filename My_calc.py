from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.resizable(width=False, height=False)

text_num1 = Label(text="Enter first number below")
text_num1.place(relx=.05, rely=.15)

enter_first_num = Entry(width=30, justify=RIGHT)
enter_first_num.place(relx=.05, rely=.2)

text_num2 = Label(text="Enter second number below")
text_num2.place(relx=.05, rely=.25)

enter_sec_num = Entry(width=30, justify=RIGHT)
enter_sec_num.place(relx=.05, rely=.3)

text_result = Label(text="Here is your result:")
text_result.place(relx=.05, rely=.35)

result = Entry(width=30, justify=RIGHT)
result.place(relx=.05, rely=.4)

def add():
    clear_result()
    try:
        sum_nums = float(enter_first_num.get()) + float(enter_sec_num.get())
    except ValueError:
        result.insert(0, "Not number")
    else:
        result.insert(0, sum_nums)

def subtract():
    clear_result()
    try:
        subtr_nums = float(enter_first_num.get()) - float(enter_sec_num.get())
    except ValueError:
        result.insert(0, "Not number")
    else:
        result.insert(0, subtr_nums)

def multiply():
    clear_result()
    try:
        mult_nums = float(enter_first_num.get()) * float(enter_sec_num.get())
    except ValueError:
        result.insert(0, "Not number")
    else:
        result.insert(0, mult_nums)

def divide():
    clear_result()
    try:
        div_nums = float(enter_first_num.get()) / float(enter_sec_num.get())
    except ValueError:
        result.insert(0, "Not number")
    else:
        result.insert(0, div_nums)

def clear_result():
    result.delete(0, END)

def clear_enter_fields():
    enter_first_num.delete(0, END)
    enter_sec_num.delete(0, END)
    result.delete(0, END)

title_1 = Label(text="Use keyboard for enter numbers", pady = 20)
title_1.pack()

btn_add = Button(root, text="+", command=add, height="1", width="1")
btn_add.place(relx=.7, rely=.2)

btn_subt = Button(root, text="-", command=subtract, height="1", width="1")
btn_subt.place(relx=.8, rely=.2)

btn_mult = Button(root, text="*", command=multiply, height="1", width="1")
btn_mult.place(relx=.7, rely=.3)

btn_divide = Button(root, text="/", command=divide, height="1", width="1")
btn_divide.place(relx=.8, rely=.3)

btn_clear = Button(root, text="Clear", command=clear_enter_fields, height="1", width="3")
btn_clear.place(relx=.7, rely=.4)

root.mainloop()


