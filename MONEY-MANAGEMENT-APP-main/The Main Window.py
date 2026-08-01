from tkinter import*
import tkinter as tk
from tkinter import messagebox
import mysql.connector as ms
from tkinter import ttk
root=Tk()
root.geometry('1200x1000')
#frame
f1=Frame(root,padx=244,pady=3,bg='purple')
f1.grid(row=2,column=2)
f2=Frame(root,padx=30,pady=30,bg='grey')
f2.grid(row=3,column=2)
f33=Frame(root,padx=30,pady=20)
f33.grid(row=4,column=2)
f3=Frame(root,padx=265,bg='purple')
f3.place(x=110,y=345)
f4=Frame(root,padx=95,pady=30,bg='grey')
f4.place(x=110,y=365)
he=LabelFrame(root,text='Credit Details',font='ar 10 bold',padx=100,pady=100,borderwidth=3)
he.grid(row=2,column=8,rowspan=2)
f5=LabelFrame(root,text='Debit Details',font='ar 10 bold',padx=100,pady=100,borderwidth=3)
f5.grid(row=5,column=8,rowspan=5,sticky='s')
#for personal details
def update():
    root = Tk() 
    root.geometry("350x280") 
    root.title("Personal details")
    f1 =Frame(root, borderwidth=3, bg="grey",padx=40,highlightbackground="black", highlightthickness=2) 
    f1.grid(row=0,column=0)
    f2=LabelFrame(root, borderwidth=3, bg="grey",text="Update Data", font="Helvetica 10 ", fg="dark blue",padx=47,highlightbackground="black", highlightthickness=2)
    f2.grid(row=1,column=0)
    l = Label(f1, text="Personal Data", font="Helvetica 16 bold", fg="dark blue", pady=22,justify='center',bg="grey") 
    l.grid(columnspan=2) 
    #label
    A= Label(f1, text="First name :",bg="grey")
    B= Label(f1, text="Last name :",bg="grey")
    C= Label(f1, text="Occupation :",bg="grey")
    D= Label(f1, text="Mobile number :",bg="grey")
    E= Label(f1, text="Email id:",bg="grey")
    F= Label(f2, text="Update Fields",bg="grey")
    G=Label(f2, text="Data",bg="grey")
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


#menu bar
my_menu=Menu(root)
#-profile menu
m1=Menu(my_menu)
m1.add_command(label='Edit')
m1.add_command(label='log out')
#-file menu
m2=Menu(my_menu)
m2.add_command(label='New Transaction')
m2.add_command(label='Delete Transaction')
m2.add_command(label='Display Credit Transaction')
m2.add_command(label='Display Debit Transaction')
m2.add_command(label='View Last Transaction')
#-history menu
m3=Menu(my_menu)
m3.add_command(label='Track Transaction')
m3.add_command(label='Track Monthly')
#-defining menu
root.config(menu=my_menu)
my_menu.add_cascade(label='Profile',menu=m1)
my_menu.add_cascade(label='File',menu=m2)
my_menu.add_cascade(label='History',menu=m3)
#text
h=Label(root,text='User name',font='ar 15 bold').grid(row=0,column=0)
he1=Label(f33,text='Date',fg='white').grid(row=0,column=0)
he1=Label(he,text='Date').grid(row=0,column=0)
he2=Label(he,text='Amount Credited').grid(row=0,column=1)
he3=Label(he,text='Mode of Credit').grid(row=0,column=2)
h01=Label(f3,text='Details',font='ar 10',fg='white',bg='purple').grid(row=11,column=3,columnspan=1,sticky='s')
h1=Label(f1,text='Expenditure Info',font='ar 10',fg='white',bg='purple').grid(row=2,column=3,columnspan=1)
h2=Label(f2,text='Date',bg='grey').grid(row=3,column=2)
h3=Label(f2,text='Amount Credited',bg='grey').grid(row=4,column=2)
h4=Label(f2,text='Mode of Credit',bg='grey').grid(row=5,column=2)
h5=Label(f2,text='Money Spend on',bg='grey').grid(row=6,column=2)
h6=Label(f2,text='Amount Debited',bg='grey').grid(row=7,column=2)
h7=Label(f2,text='Mode of Debit',bg='grey').grid(row=8,column=2)
h03=Label(f4,text='Total Balance :',bg='grey').grid(row=12,column=2,sticky='n')
hf5=Label(f5,text='Date').grid(row=0,column=0)
h1f5=Label(f5,text='Amount Debited').grid(row=0,column=1)
h2f5=Label(f5,text='Mode of Debit').grid(row=0,column=2,padx=20)
#input field
e=Entry(f2,width=50) 
e1=Entry(f2,width=50)
e2=Entry(f2,width=50)
e3=Entry(f2,width=50)
e4=Entry(f2,width=50)
e5=Entry(f2,width=50)
e6=Entry(f4,width=50)


#position of entries
e.grid(row=3,column=3)
e1.grid(row=4,column=3)
e2.grid(row=5,column=3)
e3.grid(row=6,column=3)
e4.grid(row=7,column=3)
e5.grid(row=8,column=3)
e6.grid(row=12,column=3,columnspan=3)
def add_credit_detail():
    if e.get()=='':
        messagebox.showerror('ERROR','Please!,Enter the Date')
    elif e1.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your Amount Credited.')
    elif e2.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your Mode of Credit.')
    else:
        mycon=ms.connect(host='localhost',user='root',passwd='1234',database='user_details')
        if mycon.is_connected():
            print('successful ......')
        Cursor_name=mycon.cursor()
        mycursor=mycon.cursor()
        command=('insert into credit_details values(%s,%s,%s,%s)')
        values=(e.get(),e1.get(),e2.get())
        mycursor.execute(command,values)
        mycon.commit()
        mycon.close()
        messagebox.askokcancel('','your credit details are saved successfully.')
        print('saved')
def add_debited_detail():
    if e.get()=='':
        messagebox.showerror('ERROR','Please!,Enter the Date')
    elif e3.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your Money Spend on.')
    elif e4.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your Amount Debited.')
    elif e5.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your Mode of Debit.')
    else:
        mycon=ms.connect(host='localhost',user='root',passwd='1234',database='user_details')
        if mycon.is_connected():
            print('successful ......')
        Cursor_name=mycon.cursor()
        mycursor=mycon.cursor()
        command=('insert into debit_details values(%s,%s,%s,%s)')
        values=(e3.get(),e4.get(),e5.get())
        mycursor.execute(command,values)
        mycon.commit()
        mycon.close()
        messagebox.askokcancel('','your credit details are saved successfully.')
        print('saved')


#Button
button=Button(f2,text='ADD CREDIT DETAILS',padx=50,bg='dark green',fg='yellow')
button.grid(row=9,column=2)
button1=Button(f2,text='ADD DEBIT DETAILS',padx=50,bg='dark green',fg='yellow')
button1.grid(row=9,column=3)

root.mainloop()


