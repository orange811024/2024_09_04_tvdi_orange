from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('登入')
        #===========style==========
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Arial',20))
        #===========end style==========
        #===========topFrame==========
        topFrame= ttk.Frame(self)
        ttk.Label(topFrame,text='個人資料輸入',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        #===========end topFrame==========
        #===========bottomFrame==========
        bottomFrame = ttk.Frame(self)
        ttk.Label(bottomFrame,text='UserName:').grid(column=0,row=0,padx=10)
        username_entry = ttk.Entry(bottomFrame)
        username_entry.grid(column=1,row=0)
        ttk.Label(bottomFrame,text='Password:').grid(row=1,column=0)
        password_entry = ttk.Entry(bottomFrame)
        password_entry.grid(column=1,row=1,pady=10,padx=10)
        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20))
        #===========end bottomFrame==========

def main():
    window = Window(theme='arc')
    window.mainloop()
if __name__ == '__main__':
    main()