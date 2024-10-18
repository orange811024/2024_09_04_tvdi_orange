import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('使用ttk的套件')
        self.geometry('400x300')
        style = ttk.Style(self)
        '''
        style.configure('TLabel',font=('Helvetica',11)) #改變現有的
        style.configure('Title.TLabel',font=('Helvetica',30),background='#FFC1E0',foreground='red') #自訂的Style
        message = ttk.Label(self,text='使用ttk的Label',style='Title.TLabel')
        #message = 區域變數
        #self.message = 全域變數
        print(message.winfo_class())
        message.pack()
        '''
        style.configure('Main.TButton',font=('Arial',15))
        btn1 = ttk.Button(self,text='Button Demo',style='Main.TButton')
        btn1.pack(ipadx=10,ipady=10)


def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()