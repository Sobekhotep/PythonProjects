from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.resizable(width=False, height=False)

text_num1 = Label(text="Enter numbers below")
text_num1.place(relx=.05, rely=.15)

enter_numbers = Entry(width=30, justify=RIGHT, font=("Verdana", 13, "bold"))
enter_numbers.place(relx=.05, rely=.2)

first_number = 0
second_number = 0
var = 0



def function(param):
    try:
        if param == "add":
            result = float(entering_nums[0]) + float(entering_nums[2])
        elif param == "subtract":
            result = float(entering_nums[0]) - float(entering_nums[2])
        elif param == "multiply":
            result = float(entering_nums[0]) * float(entering_nums[2])
        elif param == "divide":
            result = float(entering_nums[0]) / float(entering_nums[2])
        else:
            result = "Unknown operation"
    except ValueError:
        enter_numbers.insert(0, "Not number")
    except ZeroDivisionError:
        enter_numbers.insert(0, "Can not be divided by zero")
    else:
        enter_numbers.insert(0, result)

def clear_result():
    enter_numbers.delete(0, END)

def action(var):
    first_num = enter_numbers.get()
    entering_nums.insert(0, first_num)
    entering_nums.insert(1, var)
    clear_result()

def decide():
    second_num = enter_numbers.get()
    enter_numbers.insert(2, second_num)
    clear_result()
    function(entering_nums[1])



title_1 = Label(text="Use keyboard for enter numbers", pady = 20)
title_1.pack()

btn_add = Button(root, text="+", command=action("add"), height="1", width="1")
btn_add.place(relx=.05, rely=.3)

btn_subt = Button(root, text="-", command=action("subtract"), height="1", width="1")
btn_subt.place(relx=.15, rely=.3)

btn_mult = Button(root, text="*", command=action("multiply"), height="1", width="1")
btn_mult.place(relx=.25, rely=.3)

btn_divide = Button(root, text="/", command=action("divide"), height="1", width="1")
btn_divide.place(relx=.35, rely=.3)

btn_result = Button(root, text="=", command=decide, height="1", width="1")
btn_result.place(relx=.45, rely=.3)

btn_clear = Button(root, text="Clear", command=clear_result(), height="1", width="1")
btn_clear.place(relx=.55, rely=.3)

root.mainloop()


