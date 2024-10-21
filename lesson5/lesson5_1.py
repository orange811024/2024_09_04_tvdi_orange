from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件，這是title')
        style = ttk.Style(self)

        #=====start topFrame=====
        topFrame = ttk.Frame(self,width=300,height=300,borderwidth=3,relief='groove')
        topFrame.pack(padx=10,pady=(10,0),expand=True,fill='x')
        self.btn1 = ttk.Button(topFrame,text='按鈕1',command=self.user_click1)
        self.btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text='按鈕2',command=self.user_click2)
        btn2.pack(side='left',expand=True,fill='x',padx=10)
        btn3 = ttk.Button(topFrame,text='按鈕3',command=self.user_click3)
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        #=====end topFrame=====
        
        #=====start leftFrame=====
        bottonFrame1 = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottonFrame1.pack(padx=10,pady=10,side='left')
        btnF1_1 = ttk.Button(bottonFrame1,text='按鈕(大)', padding=(30,40))
        btnF1_1.bind('<ButtonRelease>',self.left_button_click)
        btnF1_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF1_2 = ttk.Button(bottonFrame1,text='按鈕(小)', padding=10)
        btnF1_2.bind('<ButtonRelease>',self.left_button_click)
        btnF1_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF1_3 = ttk.Button(bottonFrame1,text='按鈕(小)', padding=10)
        btnF1_3.bind('<ButtonRelease>',self.left_button_click)
        btnF1_3.pack(side='top',expand=True,fill='x',padx=10)
        #=====end leftFrame=====

        #=====start centerFrame=====
        bottonFrame2 = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottonFrame2.pack(padx=10,pady=10,side='left')
        btnF2_1 = ttk.Button(bottonFrame2,text='按鈕(大)', padding=(30,25))
        btnF2_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF2_2 = ttk.Button(bottonFrame2,text='按鈕(小)', padding=10)
        btnF2_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF2_3 = ttk.Button(bottonFrame2,text='按鈕(大)', padding=25)
        btnF2_3.pack(side='top',expand=True,fill='x',padx=10)
        #=====end centerFrame=====

        #=====start rightFrame=====
        bottonFrame3 = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottonFrame3.pack(padx=10,pady=10,side='left')
        btnF3_1 = ttk.Button(bottonFrame3,text='按鈕', padding=(30,20))
        btnF3_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF3_2 = ttk.Button(bottonFrame3,text='按鈕', padding=20)
        btnF3_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF3_3 = ttk.Button(bottonFrame3,text='按鈕', padding=20)
        btnF3_3.pack(side='top',expand=True,fill='x',padx=10)
        #=====end rightFrame=====

    def user_click1(self):
        self.btn1.configure(text='被按了')
        print("Hello!Button1")
    def user_click2(self):
        print("Hello!Button2")
    def user_click3(self):
        print("Hello!Button3")
    def left_button_click(self,event):
        print(event)
        print(type(event))
        print(event.x)
        print(event.y)
        print(event.width)
        print(event.widget.configure(text='被按了'))

def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()