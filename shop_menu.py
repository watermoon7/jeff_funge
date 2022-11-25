import tkinter as tk
from tkinter.ttk import Label, Button, Style

window = tk.Tk()

def one():
    print('one')

def two():
    print('two')

def three():
    print('three')

def four():
    print('four')

def five():
    print('five')

menu1 = Label(
    window,
    anchor = tk.CENTER,
    text = 'Shop Menu',
    background = 'cyan',
    borderwidth = 25,
    relief = 'groove',
    cursor = 'clock'
    ).pack(ipadx=10, ipady=10, padx = 70, pady = 20)

buttonStyle = Style()
buttonStyle.configure(
    'e.TButton',
    background = 'blue',
    foreground = 'darkgreen',
    borderwidth = 25,
    relief = 'groove',
    cursor = 'man',
    padding = 12,
    wraplength = 69
    )

option1 = Button(
    window,
    text = 'UPGRADE 1',
    style = 'e.TButton',
    command = one
    ).pack(padx = 5, pady = 6)

option2 = Button(
    window,
    text = 'UPGRADE 2',
    style = 'e.TButton',
    command = two
    ).pack(padx = 5, pady = 6)

option3 = Button(
    window,
    text = 'UPGRADE 3',
    style = 'e.TButton',
    command = three
    ).pack(padx = 5, pady = 6)

option4 = Button(
    window,
    text = 'UPGRADE 4',
    style = 'e.TButton',
    command = four
    ).pack(padx = 5, pady = 6)

option5 = Button(
    window,
    text = 'UPGRADE 5',
    style = 'e.TButton',
    command = five
    ).pack(padx = 5, pady = 6)

def run():
    window.update()
