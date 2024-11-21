from tkinter import *
import random
from tkinter import messagebox
import os

root = Tk()
root.title("Billing System")
root.geometry("1280x720")

# Variables
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
Rate = IntVar()
qnty = IntVar()
billno = StringVar()
x = random.randint(1000, 9999)
billno.set(str(x))

l = []  # List to store item prices

# Create bills directory if it doesn't exist
if not os.path.exists("bills"):
    os.makedirs("bills")

# Functions
def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t Welcome to Billing Software")
    textarea.insert(END, f'\n\n Bill number: \t\t{billno.get()}')
    textarea.insert(END, f'\n Customer Name: \t\t{c_name.get()}')
    textarea.insert(END, f'\n Phone number: \t\t{c_phone.get()}')
    textarea.insert(END, "\n=====================================")
    textarea.insert(END, "\n Product\t\t QTY\t\tPrice")
    textarea.insert(END, "\n=====================================")
    textarea.config(font="arial 15 bold")

def additm():
    n = Rate.get()
    m = qnty.get() * n
    l.append(m)
    if item.get() == '':
        messagebox.showerror('Error', 'Please enter an item')
    else:
        textarea.insert(END, f'\n{item.get()}\t\t{qnty.get()}\t\t{m}')

def gbill():
    if c_name.get() == '' or c_phone.get() == '':
        messagebox.showerror('Error', 'Customer details are required')
    else:
        tex = textarea.get(10.0, END)
        welcome()
        textarea.insert(END, tex)
        textarea.insert(END, "\n=====================================\n")
        textarea.insert(END, f"Total Payable Amount:\t\t\t{sum(l)}")
        textarea.insert(END, "\n=====================================\n")
        savebill()

def savebill():
    op = messagebox.askyesno('Save Bill', 'Do you want to save the bill?')
    if op:
        bill_data = textarea.get(1.0, END)
        with open(f"bills/{billno.get()}.txt", 'w') as f:
            f.write(bill_data)
        messagebox.showinfo('Saved', f'Bill no: {billno.get()} saved successfully')

def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    qnty.set(0)
    welcome()

def exit_app():
    op = messagebox.askyesno('Exit', 'Do you want to exit?')
    if op:
        root.destroy()


title = Label(root, text="Billing Software", font=("times new roman", 25, "bold"),
              bg="gray15", fg="white")
title.pack(fill=X)


cusD = LabelFrame(root, text="Customer Details", font=("times new roman", 18, "bold"),
                  relief=GROOVE, bd=10, bg="gray15", fg="white")
cusD.place(x=0, y=50, relwidth=1)

cname = Label(cusD, text="Customer Name", font=("times new roman", 18, "bold"),
              bg="gray15", fg="white")
cname.grid(row=0, column=0, padx=2, pady=5)

cnameen = Entry(cusD, width=15, font="arial 15 bold", relief=SUNKEN, textvariable=c_name)
cnameen.grid(row=0, column=1, padx=2)

cph = Label(cusD, text="Phone number", font=("times new roman", 18, "bold"),
            bg="gray15", fg="white")
cph.grid(row=0, column=2, padx=2, pady=5)

cphen = Entry(cusD, width=15, font="arial 15 bold", relief=SUNKEN, textvariable=c_phone)
cphen.grid(row=0, column=3, padx=2, pady=5)


proD = LabelFrame(root, text="Product Details", font=("times new roman", 18, "bold"),
                  relief=GROOVE, bd=10, bg="gray15", fg="white")
proD.place(x=1, y=160, width=630, height=520)

itm = Label(proD, text="Product Name", font=("times new roman", 18, "bold"),
            bg="gray15", fg="white")
itm.grid(row=0, column=0, padx=30, pady=20)

itmen = Entry(proD, width=20, font="arial 15 bold", textvariable=item)
itmen.grid(row=0, column=1, padx=30, pady=20)

rate = Label(proD, text="Product Rate", font=("times new roman", 18, "bold"),
             bg="gray15", fg="white")
rate.grid(row=1, column=0, padx=30, pady=20)

rateen = Entry(proD, width=20, font="arial 15 bold", textvariable=Rate)
rateen.grid(row=1, column=1, padx=30, pady=20)

qty = Label(proD, text="Quantity", font=("times new roman", 18, "bold"),
            bg="gray15", fg="white")
qty.grid(row=2, column=0, padx=30, pady=20)

qtyen = Entry(proD, width=20, font="arial 15 bold", textvariable=qnty)
qtyen.grid(row=2, column=1, padx=30, pady=20)


btn1 = Button(proD, text="Add item", font="arial 15 bold", padx=5, pady=10,
              bg="gray15", fg="white", width=10, bd=8, command=additm)
btn1.grid(row=3, column=0, padx=10, pady=30)

btn2 = Button(proD, text="Generate Bill", font="arial 15 bold", padx=5, pady=10,
              bg="gray15", fg="white", width=10, bd=8, command=gbill)
btn2.grid(row=3, column=1, padx=10, pady=30)

btn3 = Button(proD, text="Clear", font="arial 15 bold", padx=5, pady=10,
              bg="gray15", fg="white", width=10, bd=8, command=clear)
btn3.grid(row=4, column=0, padx=10, pady=30)

btn4 = Button(proD, text="Exit", font="arial 15 bold", padx=5, pady=10,
              bg="gray15", fg="white", width=10, bd=8, command=exit_app)
btn4.grid(row=4, column=1, padx=10, pady=30)


bill = Frame(root, relief=GROOVE, bd=10)
bill.place(x=700, y=170, width=500, height=500)

billtitle = Label(bill, text="Bill Area", font="arial 15 bold", relief=GROOVE, bd=7)
billtitle.pack(fill=X)

scroll = Scrollbar(bill, orient=VERTICAL)
textarea = Text(bill, height=50, width=50, yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.pack()

welcome()

root.mainloop()
