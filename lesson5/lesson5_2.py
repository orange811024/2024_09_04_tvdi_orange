from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

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
        bottomFrame.columnconfigure(index=0,weight=1)
        bottomFrame.columnconfigure(index=1,weight=9)

        ttk.Label(bottomFrame,text='UserName:').grid(column=0,row=0,padx=(10,0),sticky='E')
        self.username = tk.StringVar()
        ttk.Entry(bottomFrame,textvariable=self.username).grid(column=1,row=0,pady=10)

        ttk.Label(bottomFrame,text='Password:').grid(column=0,row=1,sticky='E')
        self.password = tk.StringVar()
        ttk.Entry(bottomFrame,textvariable=self.password,show='*').grid(column=1,row=1,pady=10,padx=10)

        #=====row2=====
        radioFrame = ttk.Frame(bottomFrame,height=10).grid(column=0,row=2,columnspan=2)
        size = (('Small','S'),
                ('Medium','M'),
                ('Large','L'),
                ('Extra Large','XL'),
                ('Extra Extra Large','XXL'))
        label = ttk.Label(radioFrame,text="What's your t-shirt size?").pack()
        #=====end row2=====

        cancel_btn = ttk.Button(bottomFrame,text='取消',command=self.cancel_click)
        cancel_btn.grid(column=0,row=2,padx=10,pady=(30,0))

        ok_btn = ttk.Button(bottomFrame,text='確定',command=self.ok_click)
        ok_btn.grid(column=1,row=2,padx=10,pady=(30,0),sticky='E')

        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #===========end bottomFrame==========
    def cancel_click(self):
        self.username.set('')
        self.password.set('')
    def ok_click(self):
        username = self.username.get()
        password = self.password.get()
        showinfo(title='使用者輸入',message=f'使用者名稱:{username}\n使用者密碼:{password}')


def main():
    window = Window(theme='arc')
    #window.username.set('輸入姓名')
    #window.password.set('輸入密碼')
    window.mainloop()
if __name__ == '__main__':
    main()