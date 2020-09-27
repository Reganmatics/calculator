import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title('mini calculator')
blue = '#112233'

def calcBackground(color):
    app['background'] = color


"""
class calculatorLogic:
    "docstring"
    def __init__(self, 
"""


equation = ''
def expSet(btn):
    global equation
    global expression
    equation += str(btn['text'])
    expression.set(equation)

def delete():
    equation = expression.get()
    equation = equation[:len(equation)-1]
    expression.set(equation)

def clear():
    equation = ' '
    expression.set(equation)

#def writeNumber(

for i in range(10):
    globals()[f'number{i}'] = eval("ttk.Button(app, text = i, command = lambda:expSet(number{}))".format(i))

expression = tk.StringVar()
answer = tk.StringVar()
displayText = tk.Label(app, textvariable = expression, bg = '#777', fg = '#111')
answerText = tk.Label(app, textvariable = answer, bg = '#888')
displayText.grid(row = 0, column = 0, columnspan = 2, sticky = 'nsew')
answerText.grid(row = 0, column = 2, sticky = 'nsew')

number0.grid(row = 4, column = 1)
number1.grid(row = 3, column = 0)
number2.grid(row = 3, column = 1)
number3.grid(row = 3, column = 2)
number4.grid(row = 2, column = 0)
number5.grid(row = 2, column = 1)
number6.grid(row = 2, column = 2)
number7.grid(row = 1, column = 0)
number8.grid(row = 1, column = 1)
number9.grid(row = 1, column = 2)

#mathematicalSymbols
floatVar = tk.StringVar()
multiplyVar = tk.StringVar()
addVar = tk.StringVar()
subtractVar = tk.StringVar()
moduloVar = tk.StringVar()
intDivideVar = tk.StringVar()

#logic_buttons


floatDivideButton = ttk.Button(app, text = '/', command = \
                               lambda:expSet(floatDivideButton))
multiplyButton = ttk.Button(app, text = '*', command = \
                            lambda:expSet(multiplyButton))
addButton = ttk.Button(app, text = '+', command = \
                       lambda:expSet(addButton))
subtractButton = ttk.Button(app, text = '-', command = \
                            lambda:expSet(subtractButton))
moduloButton = ttk.Button(app, text = '%', command = \
                          lambda:expSet(moduloButton))
intDivideButton = ttk.Button(app, text = '//', command = lambda:expSet(intDivideButton))
solveButton = ttk.Button(app, text = '=', command = lambda:solve(expression))

ACButton = ttk.Button(app, text = 'AC', command = clear)
DELButton = ttk.Button(app, text = 'DEL', command = delete)

#floatVar = floatDivideButton['text']
#multiplyVar = multiplyButton['text']

#logic_buttons grid

moduloButton.grid(row = 4 , column = 0)
intDivideButton.grid(row = 4, column = 2)
subtractButton.grid(row = 0, column = 3)
multiplyButton.grid(row = 1, column = 3)
addButton.grid(row = 2, column = 3)
floatDivideButton.grid(row = 3, column = 3)
solveButton.grid(row = 4, column = 3)

ACButton.grid(row = 0, column = 4)
DELButton.grid(row = 1, column = 4)


def solve(expr):
    try:
        answer.set(eval(expr.get()))
    except SyntaxError:
        answer.set('syntax Error')

calcBackground(blue)




