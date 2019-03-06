from tkinter import*
import sqlite3

con=sqlite3.Connection("w5db")
cur=con.cursor()
#----------------------------Bus Tbale------------------------------------------------------
cur.execute("create table if not exists bus(bus_no number primary key ,bus_name varchar(20),source varchar(20),destination varchar(20),bus_date varchar(20),arrival_time number,departure_time number, distance number)")



cur.execute('select * from bus')
print (cur.fetchall())


#----------------------------BUS TYPE Table-------------------------------------------------
cur.execute("create table if not exists bus_type(id number  ,bustype varchar(20),fare numer)")

cur.execute('select * from bus_type')
print (cur.fetchall())

#----------------------------TICKET Table---------------------------------------------------
cur.execute("create table if not exists ticket(ticket_no number ,source varcahr(20),destination varchar(20),bus_date date,name varchar(20),arrival_time number,departure_time number,bustype varchar(20),rent number,distance number,seat_no)")

v=[(1,'guna','bhopal','1-10-2018','Ram',10,10,'ac',250,10,2)]
cur.executemany("insert into ticket values(?,?,?,?,?,?,?,?,?,?,?)",v)
#----------------------------PAYMENT Table--------------------------------------------------
cur.execute("create table if not exists payment(card_type varchar(20),card_no number,pin number,name varchar(20),reciept varchar(20))")

b=[('obc',123,1234,'Ram','print')]
cur.executemany("insert into payment values(?,?,?,?,?)",b)
#----------------------------USER ENTRY Table-----------------------------------------------
cur.execute("create table if not exists user(first_name varchar(20),last_name varchar(20),mobile_no number,email_id varchar(20),address varchar(20),bus_id number,card_number number,card_holder_name varchar(20),dob date)")
cur.execute("create table if not exists login(email_id varchar(20),password varchar(20),mobile_number number)")
a=[('reena','reena',9876543210),('123','123',8976543210)]
cur.executemany("insert into login values(?,?,?)",a)

root=Tk()
root.geometry("1100x5000")
Button(root,text='Home',bg='white',fg='blue',height=2,width=15,font='times 12 bold',relief='raised').grid(row=1,column=6)
Label(root,text='Welcome to Online Bus Ticket Booking ',fg='green',bg='brown',font='times 20 bold').grid(row=0,column=2,columnspan=30)
a=PhotoImage(file="tr.gif")
l=Label(root,image=a)
l.grid(row=1,column=0)
def close():
    root.destroy()

def f():
    root=Tk()
    root.title('support and help')
    
    def close():
        root.destroy()
    root["bg"]="white"
    Label(root,text='Support and Help ',bg='brown',fg='black',width=20,font='times 20 bold',height=2).grid()
    Label(root,text='Bus related Qury : 1800-103-4482 : STD code = 44820000',bg='white',font='times 15 bold',height=2,width=50).grid()
    Label(root,text='Corporate services :080-349-1244',bg='white',font='times 15 bold',height=2,width=50).grid()
    Label(root,text='Mail Services - reenadheemar57@gmail.com',bg='white',font='times 15 bold',height=2,width=50).grid()
    Button(root,text='Cancel',command=close,bg='white',fg='blue',width=20,height=2,font='times 20 bold').grid()
    root.mainloop()
Button(root,text='Support and Help',height=2,width=15,bg='white',command=f,relief='raised',fg='blue',font='times 12 bold').grid(row=1,column=8)


def ls():
    root=Tk()
    root.title('Login and sign up')
    def close():
        root.destroy()
    def login():
        root=Tk()
        root.title('login')
        def close():
            root.destroy()
        Label(root,text='enter email address',justify='left').grid(row=1,column=4)
        l1=Entry(root)
        l1.grid(row=1,column=6)
        Label(root,text='enter pasword',justify='left').grid(row=3,column=4)
        l2=Entry(root)
        l2.grid(row=3,column=6)
        Button(root,text='submit').grid(row=5,column=4)
        Button(root,text='Cancel',command=close,height=2,width=20,bg='white',fg='black',font='times 10 bold').grid(row=7,column=8,columnspan=5)
        #if l1.get=login.email_id and l2.get=login.password:
         #   Label(root,text='login successfully').grid()
        #else:
         #   Label(root,text='email i or password incorrect').grid()
    def sign():
        root=Tk()
        root.title('Sign up')
        def close():
            root.destroy()
        Label(root,text='Enter user id',justify='left').grid(row=1,column=2)
        Label(root,text='(example like : john_123)',justify='left').grid(row=1,column=4)
        s1=Entry(root)
        s1.grid(row=1,column=6)
        Label(root,text='enter passwor',justify='left').grid(row=2,column=2)
        s2=Entry(root)
        s2.grid(row=2,column=6)
        Label(root,text='enter mobile number',justify='left').grid(row=3,column=2)
        s3=Entry(root)
        s3.grid(row=3,column=6)
        Button(root,text='Cancel',command=close,height=2,width=20,bg='white',fg='black',font='times 10 bold').grid(row=7,column=8,columnspan=5)
        
        def insrt():
            
            v=[(s1.get(),s2.get(),s3.get())]
            cur.executemany("insert into login values(?,?,?)",v)
            cur.execute('select * from login')
            #l=cur.fetchall()
            #Label(root,text=l).grid(row=4,column=5)
            con.commit()
        Button(root,text='submit',command=insrt).grid(row=5,column=5,columnspan=10)
        Button(root,text='Cancel',command=close,height=2,width=20,bg='white',fg='black',font='times 10 bold').grid(row=7,column=8,columnspan=5)
        root.mainloop()
    Label(root,text='welcome to bus ticket booking',bg='white',fg='black',justify='left',font='times 20 bold').grid(row=0,column=5,columnspan=10)
    Label(root,text='if have already account',justify='left',width=20,bg='white',fg='black',font='times 10 bold').grid(row=2,column=5,columnspan=5)
    Button(root,text='Login',command=login,justify='left').grid(row=4,column=6)
    Label(root,text='create new account',justify='left',width=20,bg='white',fg='black',font='times 10 bold').grid(row=6,column=5,columnspan=5)
    Button(root,text='Sign Up',command=sign,justify='left').grid(row=7,column=6)
    Button(root,text='Cancel',command=close,height=1,width=20,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=8,column=5,columnspan=5)
    root.mainloop()
def manage():
    root=Tk()
    root.title('Manage Booking')
    Label(root,text='Manage booking',bg='white',font='times 15 bold').grid(row=0,column=5)
    def close():
        root.destroy()
    Button(root,text='Cancel',width=15,bg='white',fg='black',font='times 10 bold').grid(columnspan=10)
    Button(root,text='View',width=15,bg='white',fg='black',font='times 10 bold').grid(columnspan=10)
    Button(root,text='Sms',width=15,bg='white',fg='black',font='times 10 bold').grid(columnspan=10)
    Button(root,text='Cancel',command=close,height=2,width=20,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=4,column=3,columnspan=5)

    root.mainloop()
#--------------------------------------------Admin Entry-----------------------------------------------------
def admin():
    root=Tk()
    def close():
        root.destroy()
    
    def bus():
        root=Tk()
        root.title('Insert bus details')
        Label(root,text='insert bus detail',bg='white',font='times 15 bold').grid(row=0,column=5)
        Label(root,text='Enter bus number',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=1,column=0)
        b1=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b1.grid(row=1,column=2)
        Label(root,text='Bus Name',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=2,column=0)
        b2=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b2.grid(row=2,column=2)
        Label(root,text='Source',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=3,column=0)
        b3=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b3.grid(row=3,column=2)
        Label(root,text='Destination',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=4,column=0)
        b4=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b4.grid(row=4,column=2)
        Label(root,text='Date',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=5,column=0)
        b5=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b5.grid(row=5,column=2)
        Label(root,text='Arrival time',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=6,column=0)
        b6=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b6.grid(row=6,column=2)
        Label(root,text='Departure time',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=7,column=0)
        b7=Entry(root,fg='black',bg='white',width=15,font='times 10 bold')
        b7.grid(row=7,column=2)
        Label(root,text='Distance',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=8,column=0)
        b8=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b8.grid(row=8,column=2)
        Label(root,text='Enter bus type(ac/sleeper/non ac)',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=9,column=0)
        b9=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b9.grid(row=9,column=2)
        Label(root,text='Enter suitable fare',width=15,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=10,column=0)
        b10=Entry(root,fg='black',bg='white',width=15,font='times 10 bold',justify='left')
        b10.grid(row=10,column=2)
        def inst():
            v=[(b1.get(),b2.get(),b3.get(),b4.get(),b5.get(),b6.get(),b7.get(),b8.get())]
            cur.executemany("insert into bus values(?,?,?,?,?,?,?,?)",v)
            x=[(b1.get(),b9.get(),b10.get())]
            cur.executemany("insert into bus_type values(?,?,?)",x)
            con.commit()
        def close():
            root.destroy()
        Button(root,text='Submit',command=inst,bg='white',fg='black',width=10,font='times 10 bold',height=1).grid(row=11,column=1,columnspan=5)
        Button(root,text="cancel",command=close,bg="white",fg="black",width=10,height=1,font='times 10 bold').grid(row=11,column=6,columnspan=10)

    def bus_d():
        root=Tk()
        root.title('Delete')
        Label(root,text='delete bus details',font='times 15 bold',bg='white').grid(row=0,column=5)
        Label(root,text='Enter bus id',width=15,font='times 10 bold',justify='left',fg='black',bg='white').grid(row=1,column=0)
        d1=Entry(root,font='times 10 bold',width=15,justify='left')
        d1.grid(row=1,column=2)
        def close():
            root.destroy()
        def dele():
            v=[(d1.get())]
            
            
            cur.execute("delete from bus where bus_no=?",(d1.get()))
            cur.execute("delete from bus_type where id=?",(d1.get()))
            con.commit()
        Button(root,text='submit',command=dele,bg='white',fg='black',width=10,font='times 10 bold',height=1).grid(row=2,column=1,columnspan=5)
        Button(root, text='cancel', command=close, bg='white', fg='black', width=10, font='times 10 bold',height=1).grid(row=2, column=6, columnspan=5)
    Button(root,text='Insert Bus Details',command=bus,bg='white',height=2,width=15,fg='blue',relief='raised',font='times 12 bold').grid(row=1,column=2)
    Button(root,text='Update',bg='white',height=2,width=15,fg='blue',relief='raised',font='times 12 bold').grid(row=2,column=2)
    Button(root,text='Delete',bg='white',command=bus_d,height=2,width=15,fg='blue',relief='raised',font='times 12 bold').grid(row=3,column=2)
    Button(root,text='Cancel',command=close,height=2,width=20,bg='white',fg='black',font='times 10 bold',justify='left').grid(row=4,column=2,columnspan=5)


    root.mainloop()

Button(root,text='Admin',command=admin,bg='white',height=2,width=15,fg='blue',relief='raised',font='times 12 bold').grid(row=1,column=6)   
Button(root,text='Manage Booking',bg='white',height=2,width=15,command=manage,fg='blue',relief='raised',font='times 12 bold').grid(row=1,column=10)   
root.title("BUS BOOKING SYSTEM")
Button(root,text='Login or sign up',command=ls,height=2,width=15,bg='white',fg='blue',relief='raised',font='times 12 bold').grid(row=1,column=12)



Label(root,text='Enter Source City',width=20,bg='white',relief='raised',font='times 12 bold',height=2,justify='left').grid(row=2,column=4)
e=Entry(root,justify='left',bd=4,width=10,font='times 15 bold')
e.grid(row=2,column=6,columnspan=4)
Label(root,text='Enter Destinaion City',width=20,bg='white',relief='raised',font='times 12 bold',height=2,justify='left').grid(row=3,column=4)
e1=Entry(root,justify='left',bd=4,width=10,font='times 15 bold')
e1.grid(row=3,column=6,columnspan=4)
Label(root,text='Date',width=20,bg='white',relief='raised',font='times 12 bold',height=2,justify='left').grid(row=4,column=4)
e2=Entry(root,justify='left',bd=4,width=10,font='times 15 bold')
e2.grid(row=4,column=6,columnspan=4)


    
def bookdetail():
    root=Tk()
    root.title('Book ticket')
    def close():
        root.destroy()
    
    Label(root,text='BOOK TICKET',bg='red',width=20,height=3).grid(row=0,column=3)
    Label(root,text='Enter first name',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=1,column=0)
    c1=Entry(root,justify='left',bd=2,width=10)
    c1.grid(row=1,column=2,columnspan=3)
    Label(root,text='Enter last name',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=2,column=0)
    c2=Entry(root,justify='left',bd=4,width=10)
    c2.grid(row=2,column=2,columnspan=3)
    Label(root,text='mobile number',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=3,column=0)
    c3=Entry(root,justify='left',bd=4,width=10)
    c3.grid(row=3,column=2,columnspan=3)
    Label(root,text='e-mail id',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=4,column=0)
    c4=Entry(root,justify='left',bd=4,width=10)
    c4.grid(row=4,column=2,columnspan=3)
    Label(root,text='Address',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=5,column=0)
    c5=Entry(root,justify='left',bd=4,width=10)
    c5.grid(row=5,column=2,columnspan=3)
    Label(root,text='Bus id',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=6,column=0)
    c6=Entry(root,justify='left',bd=4,width=10)
    c6.grid(row=6,column=2,columnspan=3)
    Label(root,text='Enter card number',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=1,column=6)
    p1=Entry(root,justify='left',bd=4,width=10)
    p1.grid(row=1,column=8)
    Label(root,text='Enter car holdr name',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=2,column=6)
    p2=Entry(root,justify='left',bd=4,width=10)
    p2.grid(row=2,column=8)
    Label(root,text='Enter date of birth',height=2,width=20,bg='white',relief='raised',justify='left').grid(row=3,column=6)
    p3=Entry(root,justify='left',bd=4,width=10)
    p3.grid(row=3,column=8)
    def insert():
        v=[(c1.get(),c2.get(),c3.get(),c4.get(),c5.get(),c6.get(),p1.get(),p2.get(),p3.get())]
        l=cur.executemany("insert into user values(?,?,?,?,?,?,?,?,?)",v)
        con.commit()
#     def show():
        cur.execute("select * from user")
        a=cur.fetchall()
        Label(root,text=a).grid(row=8,column=4)
    Button(root,text='submit',command=insert,height=2,width=20,bg='white').grid(row=7,column=2,columnspan=5)
    Button(root,text='Cancel',command=close,height=2,width=20,bg='white',fg='black',font='times 10 bold').grid(row=7,column=8,columnspan=5)
    
    root.mainloop()
   

def show():
    
    
    
    cur.execute('select bus.bus_no,bus.bus_name,bus.source,bus.destination,bus.bus_date,bus.arrival_time,bus.distance,bus_type.bustype,bus_type.fare from bus join bus_type on bus.bus_no=bus_type.id where bus.source=? and bus.destination=? and bus.bus_date=?',(e.get(),e1.get(),e2.get()))
    l=cur.fetchall()
    x=8
    for i in l:
        Label(root,text=l,bg='white',fg='black',height=1,font='times 10 bold',justify='left').grid(row=x,column=0,columnspan=5)
        Button(root,text='Choose Seat',bg='white',fg='black',relief='raised').grid(row=x,column=5)
        Button(root,text='Book Ticket',command=bookdetail,bg='orange',relief='raised').grid(row=x,column=6)
        x+=1
            
Button(root,text='Search',command=show,height=2,width=20,bg='white',fg='black',font='times 10 bold').grid(row=7,column=4,columnspan=5)
Button(root,text='Cancel',command=close,height=2,width=20,bg='white',fg='black',font='times 10 bold').grid(row=7,column=8,columnspan=5)


root.mainloop()

