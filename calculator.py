
from tkinter import *
import math
import ast   #ast- abstract syntax tree :it has various modules to pass expressions and evaluate

root = Tk()
root.title("Calculator")
root.geometry("150x150+60+60")
root.resizable(0,0)

#get the user input and place it in the text field
i=0
def getvariables(num):
    global i
    display.insert(i, num,)
    i+=1


def getoperation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+= length


def clearall():
    display.delete(0,END)

def undo():
    entirestring = display.get()
    if len(entirestring):
        newstring = entirestring[:-1]
        clearall()
        display.insert(0, newstring)
    else:
        clearall()
        display.insert(0 , "")

def factorial(operator):
    entirestring = display.get()
    num=int (entirestring)
    f=1
    for x in range(1,num+1):
        f=f*x
    clearall()
    display.insert(0,f)

def calculate():
    entirestring = display.get()
    try:
            a = ast.parse(entirestring,mode="eval")
            result = eval(compile(a,'<string>','eval'))
            clearall()
            display.insert(0, result)

    except Exception:
        clearall()
        display.insert(0, "Error")


#adding the input field
display = Entry(root)
display.grid(row =1, columnspan =10, sticky = W+E)

#adding buttons to the calculator

Button(root, text = "1", command = lambda : getvariables(1)).grid(row = 2 , column = 0)
Button(root, text = "2", command = lambda : getvariables(2)).grid(row = 2 , column = 1)
Button(root, text = "3", command = lambda : getvariables(3)).grid(row = 2 , column = 2)

Button(root, text = "4", command = lambda : getvariables(4)).grid(row = 3 , column = 0)
Button(root, text = "5", command = lambda : getvariables(5)).grid(row = 3 , column = 1)
Button(root, text = "6", command = lambda : getvariables(6)).grid(row = 3 , column = 2)

Button(root, text = "7", command = lambda : getvariables(7)).grid(row = 4 , column = 0)
Button(root, text = "8", command = lambda : getvariables(8)).grid(row = 4 , column = 1)
Button(root, text = "9", command = lambda : getvariables(9)).grid(row = 4 , column = 2)

#adding other buttons to the calculator
Button(root, text = "AC", command = lambda :clearall()).grid(row=5 , column = 0)
Button(root, text = "0", command = lambda : getvariables(0)).grid(row=5 , column = 1)
Button(root, text = "=", command = lambda :calculate()).grid(row=5 , column = 2)

Button(root, text = "+", command = lambda :getoperation("+")).grid(row=2 , column = 3)
Button(root, text = "-", command = lambda :getoperation("-")).grid(row=3 , column = 3)
Button(root, text = "*", command = lambda :getoperation("*")).grid(row=4 , column = 3)
Button(root, text = "/", command = lambda :getoperation("/")).grid(row=5 , column = 3)

#adding newoperations
Button(root, text = "pi", command = lambda :getoperation("3.14")).grid(row=2 , column = 4)
Button(root, text = "%", command = lambda :getoperation("%")).grid(row=3 , column = 4)
Button(root, text = "(", command = lambda :getoperation("(")).grid(row=4 , column = 4)
Button(root, text = "exp", command = lambda :getoperation("**")).grid(row=5 , column =4)

Button(root, text = "del", command = lambda :undo()).grid(row=2 , column = 5)
Button(root, text = "x!", command = lambda :factorial("!")).grid(row=3 , column = 5)
Button(root, text = ")", command = lambda :getoperation(")")).grid(row=4 , column = 5)
Button(root, text = "x^2", command = lambda :getoperation("**2")).grid(row=5 , column =5)


root.mainloop()