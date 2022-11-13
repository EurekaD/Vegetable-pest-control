from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn01 = Button(self, text='搜索', command=self.query())
        self.btn01.pack()

        self.lab1 = Label(self, text='蔬菜名称:', font=('宋体', 14))
        self.lab1.pack()

        self.lab2 = Label(self, text='病虫害名称:', font=('宋体', 14))
        self.lab2.pack()

    def query(self):
        pass
if __name__ == '__main__':
    root = Tk()
    root.title('蔬菜病虫害防治test1')
    # 设置窗口大小
    root.geometry('600x600+100+200')
    # 提示信息label
    app = Application(root)
    root.mainloop()





