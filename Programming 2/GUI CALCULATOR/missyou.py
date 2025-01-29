from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry('315x510')
win.configure(background='white')

def btnclick(num):
    global operator
    operator = operator + str(num)
    _input.set(operator)
    miss_you_label.grid_forget()  # Hide the "I miss you" message when other buttons are clicked

def clear():
    global operator
    operator = ""
    _input.set("")
    miss_you_label.grid_forget()  # Hide the "I miss you" message when clear is clicked

def answer():
    global operator
    ans = str(eval(operator))
    _input.set(ans)
    operator = ""
    miss_you_label.grid_forget()  # Hide the "I miss you" message after showing the answer

def show_miss_you():
    miss_you_label.grid(row=1, columnspan=5)  # Show the "I miss you" message when + is clicked

# Title label
label = Label(win, font=('arial', 20, 'bold'), text='YujiTech', bg='white', fg='black')
label.grid(columnspan=5)

# "I miss you" label (initially hidden)
miss_you_label = Label(win, font=('arial', 14, 'italic'), text='I MISS YOU BOSSING', bg='white', fg='black')

_input = StringVar()
operator = ""

display = Entry(win, font=('arial', 20, 'bold'), textvariable=_input, insertwidth=7, bd=5, bg="white", justify='right')
display.grid(row=2, columnspan=4)

# ------------------ Row-1 -------------------------------------------------------------------------------------------------------

b7 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="7", bg="grey", command=lambda: btnclick(7))
b7.grid(row=3, column=0)

b8 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="8", bg="grey", command=lambda: btnclick(8))
b8.grid(row=3, column=1)

b9 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="9", bg="grey", command=lambda: btnclick(9))
b9.grid(row=3, column=2)

Add = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="+", bg="grey", command=lambda: [btnclick("+"), show_miss_you()])
Add.grid(row=3, column=3)

# ---------------- Row-2 ------------------------------------------------------------------------------------------------------------

b4 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="4", bg="grey", command=lambda: btnclick(4))
b4.grid(row=4, column=0)

b5 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="5", bg="grey", command=lambda: btnclick(5))
b5.grid(row=4, column=1)

b6 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="6", bg="grey", command=lambda: btnclick(6))
b6.grid(row=4, column=2)

Sub = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="-", bg="grey", command=lambda: btnclick("-"))
Sub.grid(row=4, column=3)

# ---------------- Row-3 ------------------------------------------------------------------------------------------------------------

b1 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="1", bg="grey", command=lambda: btnclick(1))
b1.grid(row=5, column=0)

b2 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="2", bg="grey", command=lambda: btnclick(2))
b2.grid(row=5, column=1)

b3 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="3", bg="grey", command=lambda: btnclick(3))
b3.grid(row=5, column=2)

Mul = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="*", bg="grey", command=lambda: btnclick("*"))
Mul.grid(row=5, column=3)

# ---------------- Row-4 ------------------------------------------------------------------------------------------------------------

b0 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="0", bg="grey", command=lambda: btnclick(0))
b0.grid(row=6, column=0)

Dot = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text=".", bg="grey", command=lambda: btnclick("."))
Dot.grid(row=6, column=1)

Equal = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="=", bg="grey", command=answer)
Equal.grid(row=6, column=2)

Div = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="/", bg="grey", command=lambda: btnclick("/"))
Div.grid(row=6, column=3)

# ---------------- Clear Button --------------------------------------------------------------------------------------------------

Clear = Button(win, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="C", bg="grey", command=clear)
Clear.grid( columnspan=4)

win.mainloop()
