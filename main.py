import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from backend import Database

database = Database("userinfodatabooks.db")
a = 2
b = 3

class Root(object):
    def __init__(self, root):
        self.root = root
        self.root.title("User Information")

        sources = ("Facebook", "Twitter", "Reddit", "Github", "Other")

        self.spacerLabel1 = Label(root, text="     ").grid(column=0, row=0)
        self.spacerLabel2 = Label(root, text="     ").grid(column=100, row=100)

        self.nameLabel = Label(root, text="Full Name").grid(column=a, row=1, sticky=W)
        self.emailLabel = Label(root, text="Email Address").grid(column=a, row=2, sticky=W)
        self.commentLabel = Label(root, text="Comment:").grid(column=a, row=3, sticky=W)
        self.discoverLabel = Label(root, text="Discover Source:").grid(column=a, row=4, sticky=W)

        self.name_var = tkinter.StringVar()
        self.nameInputField = tkinter.Entry(root, textvariable=self.name_var, width=35).grid(column=b, row=1, pady=3, padx=3)
        self.email_var = tkinter.StringVar()
        self.emailInputField = tkinter.Entry(root, textvariable=self.email_var, width=35).grid(column=b, row=2, pady=3,
                                                                                          padx=3)
        self.commentTextBox = tkinter.Text(root, height=6, width=45, bg="white").grid(column=b, row=3, pady=3, padx=3)
        self.submitButn = tkinter.Button(root, height=1, width=15, text="Submit", bg="#ebebeb",
                                         command=self.submit_clicked).grid(
            column=b, row=5, pady=20, padx=7)

        self.showmore_butn = tkinter.StringVar()
        self.showmoreButn = tkinter.Button(root, textvariable=self.showmore_butn, bg="#ebebeb",
                                           command=self.showmore_clicked).grid(column=b, row=6, sticky=E)
        self.showmore_butn.set("Show More")

        self.selected_source = tkinter.StringVar()
        self.dropDownList = ttk.Combobox(root, textvariable=self.selected_source)
        self.dropDownList["values"] = sources
        self.dropDownList["state"] = "readonly"
        self.dropDownList.grid(column=b, row=4, padx=3, pady=3)
        self.dropDownList.bind("<<ComboboxSelected>>")

    def submit_clicked(self):
        if self.name_var.get() == "" or self.email_var.get() == "" or self.selected_source.get() == "":
            messagebox.showinfo("Empty", "Please Complete the Form")
        else:
            database.insert(self.name_var.get(), self.email_var.get(), self.selected_source.get())
            messagebox.showinfo("Submission",
                                self.name_var.get() + ", your info has been added!")

        self.name_var.set("")
        self.email_var.set("")
        self.selected_source.set("")

        print("Your Name is: " + self.name_var.get() +
              "\nYour Email is: " + self.email_var.get() +
              "\nYour Source: " + self.selected_source.get()
              )

    def showmore_clicked(self):
        if self.showmore_butn.get()=="Show More":
            self.showmore_butn.set("Show Less")
            self.list1 = Listbox(root, height=6, width=35)
            self.list1.grid(column=b, row=7, rowspan=6, columnspan=2, pady=7, sticky=E)
            self.list1.bind('<Button-1>')

            self.showData = tkinter.Button(root, text="Show Data", bg="#ebebeb",
                                               command=self.showdata_clicked)
            self.showData.grid(column=b, row=20, sticky=E)
        else:
            self.showmore_butn.set("Show More")
            self.list1.pack_forget()
            self.list1.grid_forget()
            self.showData.pack_forget()
            self.showData.grid_forget()

    def showdata_clicked(self):
        self.list1.delete(0, END)
        for row in database.view():
            print(row)
            self.list1.insert(END, row)


root = Tk()
Root(root)

root.mainloop()
