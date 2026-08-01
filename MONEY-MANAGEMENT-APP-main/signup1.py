from tkinter import *
import mysql.connector as ms
root=Tk()
root.geometry('1200x600')
Label(root, text='USER DETAILS',font='ar 15 bold',fg='blue').grid(row=0,column=2)

first_name=Label(root, text='First name')
last_name=Label(root, text='Last name')
email_id=Label(root, text='Email Id/Username')
set_password=Label(root, text='Set password')
confirm_password=Label(root, text='Confirm password')

e=Entry(root,width=50)
e1=Entry(root,width=50)
e2=Entry(root,width=50)
e3=Entry(root,width=50)
e4=Entry(root,width=50)

first_name.grid(row=2,column=1)
last_name.grid(row=2,column=2)
email_id.grid(row=2,column=3)
set_password.grid(row=4,column=1)
confirm_password.grid(row=4,column=3)
e.grid(row=3,column=1,padx=50,pady=10)
e1.grid(row=3,column=2,padx=40,pady=10)
e2.grid(row=3,column=3,padx=50,pady=10)
e3.grid(row=5,column=1,padx=30,pady=10)
e4.grid(row=5,column=3,padx=20,pady=10)

def save(*arug):
    if e.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your First Name.')
    elif e1.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your Second Name.')
    elif e2.get()=='':
        messagebox.showerror('ERROR','Please!,Enter your Email id.')
    elif e3.get()=='':
        messagebox.showerror('ERROR','Please!,Set your password.')
    elif e4.get()=='':
        messagebox.showerror('ERROR','Please!,Coniform your password.')
    else:
        mycon=ms.connect(host='localhost',user='root',passwd='1234',database='user_details')
        if mycon.is_connected():
            print('successful ......')
        Cursor_name=mycon.cursor()
        mycursor=mycon.cursor()
        command=('insert into detail values(%s,%s,%s,%s)')
        values=(e.get(),e1.get(),e2.get(),e4.get())
        command1=('insert into detail values(%s,%s)')
        values1=(e.get(),e4.get())
        mycursor.execute(command,values)
        mycursor.execute(command1,values1)
        mycon.commit()
        mycon.close()
        messagebox.askokcancel('','your are signed up successfully.')
        print('saved')
save_btn=PhotoImage(file='C:\\Users\\ADITYA\\Desktop\\resized.png')
image_label=Label(image=save_btn)
button2=Button(root,image=save_btn,command=save,borderwidth=0)
button2.grid(row=8,column=2,padx=2,pady=2)

root.mainloop()

