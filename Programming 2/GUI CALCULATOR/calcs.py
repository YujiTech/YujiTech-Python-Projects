import tkinter as tk
import tkinter.font as font
from tkinter import END

global num1
global num2
global op


def show(num):
    display_box.insert(END, num)


def clear():
    display_box.delete("1.0", END)


def assign(sign):
    global num1
    global op
    op = sign
    num1 = display_box.get("1.0", "end-1c")
    clear()


def calculate():
    global num2
    global op
    num2 = display_box.get("1.0", "end-1c")
    result = 0

    # displaying the operation to perform
    if op == "+":
        result = float(num1) + float(num2)
    elif op == "-":
        result = float(num1) - float(num2)
    elif op == "*":
        result = float(num1) * float(num2)
    elif op == "/":
        result = float(num1) / float(num2)
    clear()
    display_box.insert(END, result)


window = tk.Tk()
window.title("Simple Calculator GUI")
window.geometry("650x600")

# creating frame with background color
root_frame = tk.Frame(window)
root_frame.config(bg="#17161b")

# creating layout with background color
display_frame = tk.LabelFrame(root_frame, width=400, height=80, bg="#17161b")
display_frame.grid(row=0, column=0, pady=(10, 10))
display_frame.grid_propagate(0)

keypad_frame = tk.LabelFrame(root_frame, width=400, height=490, bg="#17161b")
keypad_frame.grid(row=1, column=0, padx=10, pady=(10, 10))
keypad_frame.grid_propagate(0)

numbers_frame = tk.LabelFrame(keypad_frame, width=260, height=465, bg="#17161b")
numbers_frame.grid(row=0, column=0, padx=(10, 20), pady=(10, 10))
numbers_frame.grid_propagate(0)

signs_frame = tk.LabelFrame(keypad_frame, width=100, height=465, bg="#17161b")
signs_frame.grid(row=0, column=1, pady=(10, 10))
signs_frame.grid_propagate(0)

display_box = tk.Text(display_frame, width=20, height=1, font=("Helvetica", 24))
display_box.grid(row=0, column=0, padx=(20, 5), pady=(20, 5))

# add number button with colors
button_1 = tk.Button(numbers_frame, text="1", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="1": show("1"))
button_1.grid(row=0, column=0, padx=10, pady=10)

button_2 = tk.Button(numbers_frame, text="2", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="2": show("2"))
button_2.grid(row=0, column=1, padx=10, pady=10)

button_3 = tk.Button(numbers_frame, text="3", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="3": show("3"))
button_3.grid(row=0, column=2, padx=10, pady=10)

button_4 = tk.Button(numbers_frame, text="4", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="4": show("4"))
button_4.grid(row=1, column=0, padx=10, pady=10)

button_5 = tk.Button(numbers_frame, text="5", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="5": show("5"))
button_5.grid(row=1, column=1, padx=10, pady=10)

button_6 = tk.Button(numbers_frame, text="6", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="6": show("6"))
button_6.grid(row=1, column=2, padx=10, pady=10)

button_7 = tk.Button(numbers_frame, text="7", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="7": show("7"))
button_7.grid(row=2, column=0, padx=10, pady=10)

button_8 = tk.Button(numbers_frame, text="8", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="8": show("8"))
button_8.grid(row=2, column=1, padx=10, pady=10)

button_9 = tk.Button(numbers_frame, text="9", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="9": show("9"))
button_9.grid(row=2, column=2, padx=10, pady=10)

button_0 = tk.Button(numbers_frame, text="0", height=2, width=3, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda num="0": show("0"))
button_0.grid(row=3, column=0, padx=10, pady=10)

button_ce = tk.Button(numbers_frame, text="CE", height=2, width=3, bd=1, fg="#fff", bg="#3697f5",
                      command=lambda: clear())
button_ce.grid(row=3, column=1, padx=10, pady=10)

button_equals = tk.Button(numbers_frame, text="=", height=2, width=3, bd=1, fg="#fff", bg="#fe9037",
                          command=lambda: calculate())
button_equals.grid(row=3, column=2, padx=10, pady=10)

# adding symbols with colors
button_add = tk.Button(signs_frame, text="+", width=3, height=2, bd=1, fg="#fff", bg="#2a2d36",
                       command=lambda sign="+": assign("+"))
button_add.grid(row=0, column=0, padx=(10, 10), pady=10)

button_subtract = tk.Button(signs_frame, text="-", width=3, height=2, bd=1, fg="#fff", bg="#2a2d36",
                            command=lambda sign="-": assign("-"))
button_subtract.grid(row=1, column=0, padx=(10, 10), pady=10)

button_multiply = tk.Button(signs_frame, text="*", width=3, height=2, bd=1, fg="#fff", bg="#2a2d36",
                            command=lambda sign="*": assign("*"))
button_multiply.grid(row=2, column=0, padx=(10, 10), pady=10)

button_divide = tk.Button(signs_frame, text="/", width=3, height=2, bd=1, fg="#fff", bg="#2a2d36",
                          command=lambda sign="/": assign("/"))
button_divide.grid(row=3, column=0, padx=(10, 10), pady=10)

# applying font to the button
button_font = font.Font(size=20, weight="bold", family="Helvetica")

for button in numbers_frame.winfo_children():
    button["font"] = button_font

for button in signs_frame.winfo_children():
    button["font"] = button_font

root_frame.pack()

window.mainloop()