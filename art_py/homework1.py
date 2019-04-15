"""Создадим кнопку меняющиую свой цвет и надпись после нажатия"""

from tkinter import *
root=Tk()
b1=Button(text="Действие",width=50, height=5, bg='#ADFF2F', fg='blue')
#b1[bg]='
def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#7B68EE'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'
b1.config(command=change)
b1.pack()
root.mainloop()