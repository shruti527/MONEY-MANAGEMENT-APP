#FOR TRACK TRANSACTION:-
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
root = Tk() 
root.geometry("420x280") 
root.title("Track Transactions")
f1 =LabelFrame(root, borderwidth=3, bg="light grey",text="DATA ENTRY", font="Helvetica 10 ", fg="dark blue",padx=73,highlightbackground="black", highlightthickness=2)
f1.grid(row=1,column=0,sticky='w')
f2 =LabelFrame(root, borderwidth=3, bg="light grey",text="DETAILS", font="Helvetica 10 ", fg="dark blue",padx=47,highlightbackground="black", highlightthickness=2)
f2.grid(row=2,column=0,sticky='w')
f3 =LabelFrame(root, borderwidth=3, bg="light grey",text="GRAPHICAL REPRESENTATION", font="Helvetica 10 ", fg="dark blue",padx=75,highlightbackground="black", highlightthickness=2)
f3.grid(row=3,column=0,sticky='w')



#LABEL
A= Label(f1, text="Starting Date :",bg="light grey")
B= Label(f1, text="Ending Date :",bg="light grey")
C= Label(f2, text="Total Money Earn :",bg="light grey")
D= Label(f2, text="Total money Spent :",bg="light grey")
E= Label(f2, text="Total Money Available :",bg="light grey")
F= Label(f3, text="Plot Graphs :",bg="light grey")

#STRINGVAR
Avalue = StringVar()
Bvalue = StringVar()
Cvalue = StringVar()
Dvalue = StringVar()
Evalue = StringVar()
Fvalue = StringVar()

#ENTRIES
Aentry=Entry(f1,textvariable = Avalue,width=30)
Bentry = Entry(f1, textvariable = Bvalue,width=30)
Centry = Entry(f2,textvariable = Cvalue,width=30)
Dentry = Entry(f2, textvariable = Dvalue,width=30)
Eentry = Entry(f2, textvariable = Evalue,width=30)
Fcmb=ttk.Combobox(f3,width=30,state='readonly')
Fcmb['values']=('Bar Chart','Pie Chart')

#GRID
A.grid(row=8)
B.grid(row=9)
C.grid(row=10)
D.grid(row=11)
E.grid(row=12)
F.grid(row=13)

Aentry.grid(row=8, column=1)
Bentry.grid(row=9, column=1)
Centry.grid(row=10, column=1)
Dentry.grid(row=11, column=1)
Eentry.grid(row=12,column=1)
Fcmb.grid(row=13,column=1)
def plot_graph():
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
         
Show_bn=Button(f1,text="SHOW",bg='dark green',fg='yellow').grid(row=15,column=0,columnspan=2)
Clear_bn=Button(f2,text="CLEAR",bg='dark green',fg='yellow').grid(row=15,column=0,columnspan=2)
VIEW_bn=Button(f3,text="VIEW",bg='dark green',fg='yellow',command=plot_graph).grid(row=15,column=0,columnspan=2)

root.mainloop()
