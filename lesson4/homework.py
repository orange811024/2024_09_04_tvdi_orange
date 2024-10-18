from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件，這是title')
        style = ttk.Style(self)

        topFrame = ttk.Frame(self,width=300,height=100,borderwidth=3,relief='groove')
        topFrame.pack(padx=10,pady=(10,0),expand=True,fill='x')
        btn1 = ttk.Button(topFrame,text='按鈕1')
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text='按鈕2')
        btn2.pack(side='left',expand=True,fill='x',padx=10)
        btn3 = ttk.Button(topFrame,text='按鈕3')
        btn3.pack(side='left',expand=True,fill='x',padx=10)

        bottomFrame = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottomFrame.pack(padx=10,pady=10,side='left')
        btnF1_1 = ttk.Button(bottomFrame,text='按鈕(大)',width=50)
        btnF1_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF1_2 = ttk.Button(bottomFrame,text='按鈕(小)')
        btnF1_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF1_3 = ttk.Button(bottomFrame,text='按鈕(小)')
        btnF1_3.pack(side='top',expand=True,fill='x',padx=10)

        bottomFrame = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottomFrame.pack(padx=10,pady=10,side='left')
        btnF2_1 = ttk.Button(bottomFrame,text='按鈕(大)')
        btnF2_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF2_2 = ttk.Button(bottomFrame,text='按鈕(小)')
        btnF2_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF2_3 = ttk.Button(bottomFrame,text='按鈕(大)')
        btnF2_3.pack(side='top',expand=True,fill='x',padx=10)

        bottomFrame = ttk.Frame(self,width=500,height=300,borderwidth=3,relief='groove')
        bottomFrame.pack(padx=10,pady=10,side='left')
        btnF3_1 = ttk.Button(bottomFrame,text='按鈕')
        btnF3_1.pack(side='top',expand=True,fill='x',padx=10)
        btnF3_2 = ttk.Button(bottomFrame,text='按鈕')
        btnF3_2.pack(side='top',expand=True,fill='x',padx=10)
        btnF3_3 = ttk.Button(bottomFrame,text='按鈕')
        btnF3_3.pack(side='top',expand=True,fill='x',padx=10)


def main():
    window = Window(theme='radiance')
    window.mainloop()

if __name__ == '__main__':
    main()