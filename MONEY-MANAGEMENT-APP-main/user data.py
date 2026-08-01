import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',passwd='1234',database='user_details')
if mycon.is_connected():
    print('successful ......')
Cursor_name=mycon.cursor()
mycursor=mycon.cursor()
mycursor.execute('create table user(First_name,Second_name,Email_id,Password)')
mycursor.execute('insert into user(e,e1,e2,e4)')
