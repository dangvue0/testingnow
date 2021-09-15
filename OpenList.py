import tkinter
from tkinter import *
from tkinter import messagebox
from SeleClass import SeleCall
from tkinter import ttk
from htmlparser import MyHTMLParser
from functiontest import People

selecall=SeleCall()

# myhtmlparser = MyHTMLParser()
# myhtmlparser.feed('<html><head><title>Test</title></head>'
#                   '<body><h1>TESTME</h1></body></html>')

# luk = People
# luk("B", "C").hey()
# lus = People("Hey", "ME")
# lus.hey()
# lui = People("1", "100").hey()

a = 2
b = 3

class Root(object):
    def __init__(self, root):
        self.root = root
        self.root.title("Open List")

        self.spacerLabel1 = Label(root, text="     ").grid(column=0, row=0)
        self.spacerLabel2 = Label(root, text="     ").grid(column=100, row=100)

        self.commentLabel = Label(root, text="List:").grid(column=a, row=1, sticky=W)

        self.box_info = tkinter.StringVar()
        self.commentTextBox = tkinter.Text(root, height=20, width=45, bg="white")
        self.commentTextBox.grid(column=a, row=2, pady=3, padx=3)

        self.submitButn = tkinter.Button(root, height=1, width=8, text="Go", bg="#ebebeb",
                                         command=self.submit_clicked).grid(
            column=a, row=3, pady=15, padx=7, sticky=W)
        self.closedButn = tkinter.Button(root, height=1, width=18, text="CloseChromeWindows", bg="#ebebeb",
                                         command=self.closedbutn_clicked).grid(
            column=a, row=3, pady=20, padx=7, sticky=E)


    def submit_clicked(self):
        self.result = self.commentTextBox.get("1.0", "end-1c")
        # selecall = SeleCall()
        if (self.result == ""):
            messagebox.showinfo("Empty", "Textbox is empty.")
            print("empty")
        else:
            # self is needed to make these vars not a one time use
            self.arrayitems = self.result.split('\n')
            for self.arrayitem in self.arrayitems:
                print(self.arrayitem)
                selecall.opennewwindowandsearch(self.arrayitem)

    def closedbutn_clicked(self):
        selecall.closewindow()

root = Tk()
Root(root)

root.mainloop()
