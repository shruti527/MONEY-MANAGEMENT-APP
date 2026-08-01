#DELETE TRANSACTIONS 

from tkinter import *
root = Tk() 
root.geometry("1366x768") 
root.title("Delete Transactions")
f1 =LabelFrame(root, borderwidth=3, bg="#ADD8E6",text="CREDIT DETAILS", font="Algerian 10 ", fg="dark blue",padx=500,pady=150,highlightbackground="black", highlightthickness=2)
f1.grid(row=0,column=0)
f2 =LabelFrame(root, borderwidth=3, bg="#ADD8E6",text="DEBIT DETAILS", font="Algerian 10 ", fg="dark blue",padx=500,pady=150,highlightbackground="black", highlightthickness=2)
f2.grid(row=1,column=0)



#LABEL
A= Label(f1, text="Date Of Credit :",bg="#ADD8E6")
B= Label(f1, text="Amount Credited :",bg="#ADD8E6")
C= Label(f2, text="Date Of Debit :",bg="#ADD8E6")
D= Label(f2, text="Expenditure :",bg="#ADD8E6")
E= Label(f2, text="Amount Debited :",bg="#ADD8E6")

#STRINGVAR
Avalue = StringVar()
Bvalue = StringVar()
Cvalue = StringVar()
Dvalue = StringVar()
Evalue= StringVar()
#ENTRIES
Aentry=Entry(f1,textvariable = Avalue,width=30)
Bentry = Entry(f1, textvariable = Bvalue,width=30)
Centry = Entry(f2, textvariable = Cvalue,width=30)
Dentry = Entry(f2, textvariable = Dvalue,width=30)
Eentry = Entry(f2, textvariable = Evalue,width=30)

#GRID
A.grid(row=8)
B.grid(row=9)
C.grid(row=11)
D.grid(row=12)
E.grid(row=13)


Aentry.grid(row=8, column=1)
Bentry.grid(row=9, column=1)
Centry.grid(row=11, column=1)
Dentry.grid(row=12, column=1)
Eentry.grid(row=13, column=1)

Delete_bn=Button(f1,text="DELETE",bg='dark green',fg='yellow').grid(row=10,column=0,columnspan=2)
Delete_bn=Button(f2,text="DELETE",bg='dark green',fg='yellow').grid(row=14,column=0,columnspan=2)





