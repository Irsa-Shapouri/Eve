from tkinter import *
import os

def en():
    window.destroy()
    os.system('En_Assistant.py')

def fa():
    window.destroy()
    os.system('Fa_Assistant.py')
    
window = Tk()
window.title('Eve')

window.geometry('300x225+1000+300')
window.resizable(False, False) 

window.iconphoto(False, PhotoImage(file='images/icon.png'))

bt_EN = Button(window,text='English', height=4,width=50,bg='#d40b0b',activebackground='#ab0e0e',font=('montserrat', 16),command=en)
bt_EN.pack()
bt_FA = Button(window,text='Farsi', height= 6,width=50,bg='#d40b0b',activebackground='#ab0e0e',font=('montserrat', 16),command=fa)
bt_FA.pack()
window.mainloop()