#for personal details 
from tkinter import *
from tkinter import ttk 
import mysql.connector as ms
root = Tk() 
root.geometry("350x280") 
root.title("Personal details")
f1 =Frame(root, borderwidth=3, bg="light grey",padx=40,highlightbackground="black", highlightthickness=2) 
f1.grid(row=0,column=0)
f2=LabelFrame(root, borderwidth=3, bg="light grey",text="Update Data", font="Helvetica 10 ", fg="dark blue",padx=47,highlightbackground="black", highlightthickness=2)
f2.grid(row=1,column=0)
l = Label(f1, text="Personal Data", font="Algerian 16 bold", fg="dark blue", pady=22,justify='center',bg="light grey") 
l.grid(columnspan=2) 
#label
A= Label(f1, text="First name :",bg="light grey")
B= Label(f1, text="Last name :",bg="light grey")
C= Label(f1, text="Occupation :",bg="light grey")
D= Label(f1, text="Mobile number :",bg="light grey")
E= Label(f1, text="Email id:",bg="light grey")
F= Label(f2, text="Update Fields",bg="light grey")
G=Label(f2, text="Data",bg="light grey")
#stringvar
Avalue = StringVar()
Bvalue = StringVar()
Cvalue = StringVar()
Dvalue = StringVar()
Evalue = StringVar()
Fvalue = StringVar()
Gvalue = StringVar()
#entries
Aentry = Entry(f1,textvariable = Avalue,width=30)
Bentry = Entry(f1, textvariable = Bvalue,width=30)
Centry = Entry(f1,textvariable = Cvalue,width=30)
Dentry = Entry(f1, textvariable = Dvalue,width=30)
Eentry = Entry(f1, textvariable = Evalue,width=30)
Fcmb = ttk.Combobox(f2,width=30,state='readonly')
Fcmb['values']=("Select","First name","Last name","Occupation","Mobile number","Email id")
Gentry = Entry(f2,textvariable = Gvalue ,width=30)
#grid
A.grid(row=8)
B.grid(row=9)
C.grid(row=10)
D.grid(row=11)
E.grid(row=12)
F.grid(row=13)
G.grid(row=14)
Aentry.grid(row=8, column=1)
Bentry.grid(row=9, column=1)
Centry.grid(row=10, column=1)
Dentry.grid(row=11, column=1)
Eentry.grid(row=12,column=1)
Fcmb.grid(row=13,column=1)
Gentry.grid(row=14,column=1)

def save():
    mycon=ms.connect(host='localhost',user='root',passwd='1234',database='user_details')
    if mycon.is_connected():
        print('successful ......')
    Cursor_name=mycon.cursor()
    mycursor=mycon.cursor()
    command=('update detail set Fcmb.get()=Gentry.get() where Password=e4.get()')
    mycursor.execute(command)
    mycon.commit()
    mycon.close()
    messagebox.askokcancel('','your details are updated successfully.')
    print('saved')
    
    
    
         

update_bn=Button(f2,text="Update",bg='dark green',fg='yellow',command=save).grid(row=15,column=0,columnspan=2)

root.mainloop()


