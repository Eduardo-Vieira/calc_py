from tkinter import *

# set de cores
black = "#3b3b3b"
white = "#ffffff"
blue = "#38576b"
gray = "#ECEFF1"
orange = "#FFAB40"

# configuração da janela
window = Tk()
window.resizable(width=0,height=0)
window.title("Calculadora")
window.geometry("235x318")
window.config(background=black)

# Configuração do frame da janela
frame = Frame(window, width=235, height=50, background=blue)
frame.grid(row=0, column=0)

frame_numbers = Frame(window, width=235, height=268)
frame_numbers.grid(row=1, column=0)

# create a StringVar class
my_string_var = StringVar()
# Criando a Label para o frame
app_label = Label(frame,
                  textvariable=my_string_var,
                  width=22,
                  height=2,
                  padx=7,
                  relief=FLAT,
                  anchor="e",
                  justify=RIGHT,
                  font="Ivy 13",
                  bg=blue,
                  fg=white
                  )
app_label.place(x=0,y=0)

# Criando botões para o frame numbers
def app_button(text, width, command, bg=gray, fg=black):
    button = Button(frame_numbers,
                    command=command,
                    text=text,
                    width=width,
                    height=2,
                    background=bg,
                    fg=fg,
                    font="Ivy 13 bold",
                    relief=RAISED,
                    overrelief=RIDGE
                    )
    return button

# set string
my_string= ""

# função para fazer o calculos
def calc():
    global my_string
    my_string_var.set(eval(my_string))
    my_string = ""

# Entrar com valores
def set_string(value):
    global my_string
    my_string = my_string + str(value)
    my_string_var.set(my_string)

# Limpar tudo
def clean():
    global my_string
    my_string = ""
    my_string_var.set("0")

# row 1
btnClean = app_button(text="C", width=11, command=lambda: clean())
btnClean.place(x=0, y=0)

btnPercent = app_button(text="%", width=4, command=lambda: set_string("%"))
btnPercent.place(x=118, y=0)

btnDivider = app_button(text="/", width=4, bg=orange, fg=white, command=lambda: set_string("/"))
btnDivider.place(x=177, y=0)

# row 2
btn7 = app_button(text="7", width=4, command=lambda: set_string("7"))
btn7.place(x=0, y=52)

btn8 = app_button(text="8", width=4, command=lambda: set_string("8"))
btn8.place(x=59, y=52)

btn9 = app_button(text="9", width=4, command=lambda: set_string("9"))
btn9.place(x=118, y=52)

btnMultiply = app_button(text="*", width=4, bg=orange, fg=white, command=lambda: set_string("*"))
btnMultiply.place(x=177, y=52)

# row 3
btn4 = app_button(text="4", width=4, command=lambda: set_string("4"))
btn4.place(x=0, y=104)

btn5 = app_button(text="5", width=4, command=lambda: set_string("5"))
btn5.place(x=59, y=104)

btn6 = app_button(text="6", width=4, command=lambda: set_string("6"))
btn6.place(x=118, y=104)

btnDecrease = app_button(text="-", width=4, bg=orange, fg=white, command=lambda: set_string("-"))
btnDecrease.place(x=177, y=104)

# row 4
btn1 = app_button(text="1", width=4, command=lambda: set_string("1"))
btn1.place(x=0, y=156)

btn2 = app_button(text="2", width=4, command=lambda: set_string("2"))
btn2.place(x=59, y=156)

btn3 = app_button(text="3", width=4, command=lambda: set_string("3"))
btn3.place(x=118, y=156)

btnPlus = app_button(text="+", width=4, bg=orange, fg=white, command=lambda: set_string("+"))
btnPlus.place(x=177, y=156)

# row 5
btnZero = app_button(text="0", width=11, command=lambda: set_string("0"))
btnZero.place(x=0, y=208)

btnPonto = app_button(text=".", width=4, command=lambda: set_string("."))
btnPonto.place(x=118, y=208)

btnResult = app_button(text="=", width=4, bg=orange, fg=white, command=lambda: calc())
btnResult.place(x=177, y=208)

window.mainloop()
