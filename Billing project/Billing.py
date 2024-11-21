from tkinter import *

def TOTAL():
    hoodie_price = int(hoodieen.get()) * 899
    shirt_price = int(checkeden.get()) * 699
    pant_price = int(pantsen.get()) * 999
    total_price = hoodie_price + shirt_price + pant_price
    textarea.insert(END, f"Total Price: {total_price}\n")
    print(f"Total Price: {total_price}")




root=Tk()
root.title("Retail Billing System By SMB")
root.geometry("1270x685")
root.iconbitmap("invoice_icon.ico")
headinglabel=Label(root,text="Billing System",font=("times new roman",30,"bold")
                   ,bg="gray10",fg="white",bd=12,relief=GROOVE)
headinglabel.pack(fill=X)

customer_det_frame=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold")
                              ,bg="gray10",fg="white",relief=GROOVE)
customer_det_frame.pack(fill=X,pady=10)


namelab=Label(customer_det_frame,text="Name",font=("times new roman",15,"bold")
                              ,bg="gray10",fg="white")
namelab.grid(row=0,column=0,padx=20)

nameentry=Entry(customer_det_frame,font=("arial",15),bd=7,width=18)
nameentry.grid(row=0,column=1,padx=8)


phlab=Label(customer_det_frame,text="Phone no",font=("times new roman",15,"bold")
                              ,bg="gray10",fg="white")
phlab.grid(row=0,column=2,padx=20,pady=2)

phentry=Entry(customer_det_frame,font=("aerial",15),bd=7,width=18)
phentry.grid(row=0,column=3,padx=8)


billlab=Label(customer_det_frame,text="Bill no",font=("times new roman",15,"bold")
                              ,bg="gray10",fg="white")
billlab.grid(row=0,column=4,padx=20,pady=2)

billentry=Entry(customer_det_frame,font=("arial",15),bd=7,width=18)
billentry.grid(row=0,column=5,padx=8)

searchbut=Button(customer_det_frame,text="Search",font=("arial",12,"bold"),bd=7,pady=10,width=7)
searchbut.grid(row=0,column=6,padx=20,pady=8)


# body
proframe=Frame(root)
proframe.pack()

menlab=LabelFrame(proframe,text="Men's Clothes",font=("times new roman",15,"bold")
                              ,bg="gray10",fg="white",relief=GROOVE)
menlab.grid(row=0,column=0,padx=5)

hoodie=Label(menlab,text="Hoodie's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
hoodie.grid(row=0,column=0,padx=20,pady=8)
hoodieen=Entry(menlab,font=("arial",15),bd=5,width=10)
hoodieen.grid(row=0,column=1,padx=8)

checked=Label(menlab,text="Shirt's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
checked.grid(row=1,column=0,padx=20,pady=8)
checkeden=Entry(menlab,font=("arial",15),bd=5,width=10)
checkeden.grid(row=1,column=1,padx=8)

pants=Label(menlab,text="Pant's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
pants.grid(row=2,column=0,padx=20,pady=8)
pantsen=Entry(menlab,font=("arial",15),bd=5,width=10)
pantsen.grid(row=2,column=1,padx=8)

trouser=Label(menlab,text="Trouser's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
trouser.grid(row=3,column=0,padx=20,pady=8)
trouseren=Entry(menlab,font=("arial",15),bd=5,width=10)
trouseren.grid(row=3,column=1,padx=8)



wmenlab=LabelFrame(proframe,text="Women's Clothes",font=("times new roman",15,"bold")
                              ,bg="gray10",fg="white",relief=GROOVE)
wmenlab.grid(row=0,column=1,padx=5)

whoodie=Label(wmenlab,text="Hoodie's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
whoodie.grid(row=0,column=0,padx=20,pady=8)
whoodieen=Entry(wmenlab,font=("arial",15),bd=5,width=10)
whoodieen.grid(row=0,column=1,padx=8)

wpants=Label(wmenlab,text="Pant's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
wpants.grid(row=1,column=0,padx=20,pady=8)
wpantsen=Entry(wmenlab,font=("arial",15),bd=5,width=10)
wpantsen.grid(row=1,column=1,padx=8)

top=Label(wmenlab,text="Top's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
top.grid(row=2,column=0,padx=20,pady=8)
topen=Entry(wmenlab,font=("arial",15),bd=5,width=10)
topen.grid(row=2,column=1,padx=8)

nd=Label(wmenlab,text="NightDress",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
nd.grid(row=3,column=0,padx=20,pady=8)
nden=Entry(wmenlab,font=("arial",15),bd=5,width=10)
nden.grid(row=3,column=1,padx=8)


clab=LabelFrame(proframe,text="Children",font=("times new roman",15,"bold")
                              ,bg="gray10",fg="white",relief=GROOVE)
clab.grid(row=0,column=2,padx=5)

top=Label(clab,text="Top's",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
top.grid(row=1,column=0,padx=20,pady=8)
topen=Entry(clab,font=("arial",15),bd=5,width=10)
topen.grid(row=1,column=1,padx=8)

cnd=Label(clab,text="NightDress",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
cnd.grid(row=0,column=0,padx=20,pady=8)
cnden=Entry(clab,font=("arial",15),bd=5,width=10)
cnden.grid(row=0,column=1,padx=8)

inner=Label(clab,text="Inners",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
inner.grid(row=2,column=0,padx=20,pady=8)
inneren=Entry(clab,font=("arial",15),bd=5,width=10)
inneren.grid(row=2,column=1,padx=8)

mf=Label(clab,text="MicroFibers",font=("arial",12,"bold"),bg="gray10",fg="white",bd=7,pady=10,width=7)
mf.grid(row=3,column=0,padx=20,pady=8)
mfen=Entry(clab,font=("arial",15),bd=5,width=10)
mfen.grid(row=3,column=1,padx=8)


billframe=Frame(proframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)

billarea=Label(billframe,text="Bill area",font=("times new roman",15,"bold"),bd=7,relief=GROOVE)
billarea.pack(fill=X)

scroll=Scrollbar(billframe,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)


textarea=Text(billframe,height=15,width=50,yscrollcommand=scroll.set)
textarea.pack()
scroll.config(command=textarea.yview)


menuframe=LabelFrame(root,text='Bill Menu',font=("times new roman",15,"bold")
                ,bg="gray10",fg="white",relief=GROOVE,bd=8)
menuframe.pack()

menscost=Label(menuframe,text="M-Price",font=("times new roman",15,"bold")
               ,bg="gray10",fg="white")
menscost.grid(row=0,column=0,pady=9,padx=10)

menentry=Entry(menuframe,font=("times new roman",15,"bold"),bd=5)
menentry.grid(row=0,column=1,pady=9,padx=8)

wmenscost=Label(menuframe,text="W-Price",font=("times new roman",15,"bold")
               ,bg="gray10",fg="white")
wmenscost.grid(row=1,column=0,pady=9,padx=10)

wmenentry=Entry(menuframe,font=("times new roman",15,"bold"),bd=5)
wmenentry.grid(row=1,column=1,pady=9,padx=8)

ccost=Label(menuframe,text="W-Price",font=("times new roman",15,"bold")
               ,bg="gray10",fg="white")
ccost.grid(row=2,column=0,pady=9,padx=10)

centry=Entry(menuframe,font=("times new roman",15,"bold"),bd=5)
centry.grid(row=2,column=1,pady=9,padx=8)


menstax=Label(menuframe,text="M-GST",font=("times new roman",15,"bold")
               ,bg="gray10",fg="white")
menstax.grid(row=0,column=2,pady=9,padx=10)

menstaxen=Entry(menuframe,font=("times new roman",15,"bold"),bd=5)
menstaxen.grid(row=0,column=3,pady=9,padx=8)

wmenstax=Label(menuframe,text="W-GST",font=("times new roman",15,"bold")
               ,bg="gray10",fg="white")
wmenstax.grid(row=1,column=2,pady=9,padx=10)

wmenstaxen=Entry(menuframe,font=("times new roman",15,"bold"),bd=5)
wmenstaxen.grid(row=1,column=3,pady=9,padx=8)

ctax=Label(menuframe,text="W-GST",font=("times new roman",15,"bold")
               ,bg="gray10",fg="white")
ctax.grid(row=2,column=2,pady=9,padx=10)

ctaxen=Entry(menuframe,font=("times new roman",15,"bold"),bd=5)
ctaxen.grid(row=2,column=3,pady=9,padx=8)

buttonfr=Frame(menuframe,bd=8,relief=GROOVE)
buttonfr.grid(row=0,column=4,rowspan=3)


tot=Button(buttonfr,text="Total",font=("arial",16,"bold"),bg="gray10",fg="white",width=8,pady=10,command=TOTAL)
tot.grid(row=0,column=0,pady=20,padx=2)

bill=Button(buttonfr,text="Bill",font=("arial",16,"bold"),bg="gray10",fg="white",width=8,pady=10)
bill.grid(row=0,column=1,pady=20,padx=2)

email=Button(buttonfr,text="Email",font=("arial",16,"bold"),bg="gray10",fg="white",width=8,pady=10)
email.grid(row=0,column=2,pady=20,padx=2)

print=Button(buttonfr,text="Print",font=("arial",16,"bold"),bg="gray10",fg="white",width=8,pady=10)
print.grid(row=0,column=3,pady=20,padx=2)

clear=Button(buttonfr,text="Clear",font=("arial",16,"bold"),bg="gray10",fg="white",width=8,pady=10)
clear.grid(row=0,column=4,pady=20,padx=2)


root.mainloop()