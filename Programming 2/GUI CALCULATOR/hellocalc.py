from tkinter import *

PINK = "#e3979c"
Value = None
Calc = ""


def Nine():
    global Calc
    Calc += "9"
    Display.config(text=Calc)


def Eight():
    global Calc
    Calc += "8"
    Display.config(text=Calc)


def Seven():
    global Calc
    Calc += "7"
    Display.config(text=Calc)


def Six():
    global Calc
    Calc += "6"
    Display.config(text=Calc)


def Five():
    global Calc
    Calc += "5"
    Display.config(text=Calc)


def Four():
    global Calc
    Calc += "4"
    Display.config(text=Calc)


def Three():
    global Calc
    Calc += "3"
    Display.config(text=Calc)


def Two():
    global Calc
    Calc += "2"
    Display.config(text=Calc)


def One():
    global Calc
    Calc += "1"
    Display.config(text=Calc)


def Zero():
    global Calc
    Calc += "0"
    Display.config(text=Calc)


def Cube():
    global Calc
    Calc += "^3"
    Display.config(text=Calc)


def Square():
    global Calc
    Calc += "^2"
    Display.config(text=Calc)


def Cee():
    global Calc
    Calc = " "
    Display.config(text=Calc)


def Clear():
    global Calc
    try:
        Clear_1 = [*Calc]
        Clear_1.pop(-1)
    except IndexError:
        pass
    else:
        Calc = "".join(Clear_1)
    Display.config(text=Calc)


def Divide():
    global Calc
    Calc += "/"
    Display.config(text=Calc)


def Multiply():
    global Calc
    Calc += "*"
    Display.config(text=Calc)


def Add():
    global Calc
    Calc += "+"
    Display.config(text=Calc)


def Subtract():
    global Calc
    Calc += "-"
    Display.config(text=Calc)


def Decimal():
    global Calc
    Calc += "."
    Display.config(text=Calc)


def Equal():
    global Calc
    new_Calc = Calc.replace("^2", "**2", 1)
    new_Calc_1 = new_Calc.replace("^3", "**3", 1)
    try:
        solu = round(eval(new_Calc_1), 4)
    except SyntaxError:
        pass
    else:
        Calc = f"{solu}"
        Display.config(text=solu)


window = Tk()
window.title("Calculator")
window.config(padx=10, pady=10)

# Label
Display = Label(text="", width=45, height=4, bg=PINK)
Display.grid(row=0, columnspan=4, column=0)
# Buttons
Cube_button = Button(text="^3", width=10, height=2, command=Cube)
Cube_button.grid(row=1, column=0)
Squared = Button(text="X^2", width=10, height=2, command=Square)
Squared.grid(row=1, column=1)
C_button = Button(text="C", width=10, height=2, command=Cee)
C_button.grid(row=1, column=2)
X_button = Button(text="X", width=10, height=2, command=Clear)
X_button.grid(row=1, column=3)
Seven_Button = Button(text="7", width=10, height=2, command=Seven)
Seven_Button.grid(row=2, column=0)
Eight_Button = Button(text="8", width=10, height=2, command=Eight)
Eight_Button.grid(row=2, column=1)
Nine_Button = Button(text="9", width=10, height=2, command=Nine)
Nine_Button.grid(row=2, column=2)
Division_Button = Button(text="/", width=10, height=2, command=Divide)
Division_Button.grid(row=2, column=3)
Four_button = Button(text="4", width=10, height=2, command=Four)
Four_button.grid(row=3, column=0)
Five_Button = Button(text="5", width=10, height=2, command=Five)
Five_Button.grid(row=3, column=1)
Six_button = Button(text="6", width=10, height=2, command=Six)
Six_button.grid(row=3, column=2)
Multiply_button = Button(text="*", width=10, height=2, command=Multiply)
Multiply_button.grid(row=3, column=3)
One_button = Button(text="1", width=10, height=2, command=One)
One_button.grid(row=4, column=0)
Two_Button = Button(text="2", width=10, height=2, command=Two)
Two_Button.grid(row=4, column=1)
Three_button = Button(text="3", width=10, height=2, command=Three)
Three_button.grid(row=4, column=2)
Minus_button = Button(text="-", width=10, height=2, command=Subtract)
Minus_button.grid(row=4, column=3)
Zero_button = Button(text="0", width=10, height=2, command=Zero)
Zero_button.grid(row=5, column=0)
Full_stop = Button(text=".", width=10, height=2, command=Decimal)
Full_stop.grid(row=5, column=1)
Equal_button = Button(text="=", width=10, height=2, command=Equal)
Equal_button.grid(row=5, column=2)
Plus_button = Button(text="+", width=10, height=2, command=Add)
Plus_button.grid(row=5, column=3)

window.mainloop()