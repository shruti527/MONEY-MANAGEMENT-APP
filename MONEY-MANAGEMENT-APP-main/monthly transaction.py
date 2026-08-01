# MONTHLY TRANSACTIONS 
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk 
root = Tk() 
root.geometry("475x235") 
root.title("Monthly Transactions")
f1 =LabelFrame(root, borderwidth=3, bg="light grey",text="COMPARE MONTHLY", font="Helvetica 10 ", fg="dark blue",padx=47,highlightbackground="black", highlightthickness=2)
f1.grid(row=0,column=0)
f2 =LabelFrame(root, borderwidth=3, bg="light grey",text="GRAPHICAL REPRESENTATION YEARLY", font="Helvetica 10 ", fg="dark blue",padx=105,highlightbackground="black", highlightthickness=2)
f2.grid(row=1,column=0)


#LABEL
A= Label(f1, text="Month 1 :",bg="light grey")
B= Label(f1, text="Month 2 :",bg="light grey")
C= Label(f1, text="Credited amount :",bg="light grey")
D= Label(f1, text="Debited Amount :",bg="light grey")
E= Label(f2, text="Plot Graph :",bg="light grey")

#STRINGVAR
Avalue = StringVar()
Bvalue = StringVar()
Cvalue = StringVar()
Dvalue = StringVar()
Evalue = StringVar()

#ENTRIES
Aentry=Entry(f1,textvariable = Avalue,width=30)
Bentry = Entry(f1, textvariable = Bvalue,width=30)
Centry = Entry(f1, textvariable = Cvalue,width=30)
Dentry = Entry(f1, textvariable = Dvalue,width=30)
Ecmb = ttk.Combobox(f2,width=30,state='readonly')
Ecmb['values']=("Select","Bar chart","Pie chart")

#GRID
A.grid(row=7,column=0)
B.grid(row=7,column=1)
C.grid(row=10,column=0)
D.grid(row=11,column=0)
E.grid(row=13,column=0)


Aentry.grid(row=8, column=0)
Bentry.grid(row=8, column=1)
Centry.grid(row=10, column=1)
Dentry.grid(row=11, column=1)
Ecmb.grid(row=13, column=1)
def plotgraph():
    X=["Shopping","Travelling","Emi","Food","Maintenance ","Entertainment"," Grocery","Medicines","Rent"]
    c=["red","yellow","black","grey","#0000FF","#00FF00","orange","purple"]
    h=[100,220,300,400,500,600,700,800,900]
    plt.bar(X,h,width=0.8,color=c,bottom=None,align="center")
    plt.xlabel("Expenditure")
    plt.ylabel("Amount")
    plt.title("Debit Amount vs Expenditure")
    plt.show()

def plotpiegraph():
   A=[ 75,32,62,85,36,48,25]
   B=["Entertainment","Grocery","Rent","Medicines","EMI","food","travelling"]
   exp=[0,0,0,0.2,0,0,0]
   plt.pie(A,labels=B,explode=exp,autopct="%2.1f%%")
   plt.title("Debit Amount vs Expenditure")
   plt.show()



Compare_bn=Button(f1,text="COMPARE",bg='dark green',fg='yellow').grid(row=9,column=0,columnspan=2)
Clear_bn=Button(f1,text="CLEAR",bg='dark green',fg='yellow').grid(row=12,column=0,columnspan=2)
Monhistory_bn=Button(f2,text="MONTHLY HISTORY",bg='dark green',fg='yellow',command=plotpiegraph).grid(row=14,column=0,columnspan=2)
