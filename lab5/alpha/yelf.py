from tkinter import *

root = Tk()
root.title("Заголовок окна программы") #заголовок окна
root.geometry('400x200') # начальные размеры окна

lab = Label(root, text="Это 1 надпись! \nЭто 2 надпись!", font="Arial 14")

lab.pack()

def start():
    root.geometry('600x500')
    
b1 = Button(text='Начать', width=15, height=3, command=lambda: b1.pack_forget())
b1.config(command=start)
b1.place(x=0, y=0)


    
root.mainloop()
