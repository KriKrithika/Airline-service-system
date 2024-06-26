from tkinter import *
from tkinter import ttk
import mysql.connector as sql
import sys


conn=sql.connect(host='localhost',password='Krithika@23',user='root',database='airline')
cur=conn.cursor()


r=Tk()


canvas = Canvas(r)
canvas.place(relx=0.5, rely=0.5, anchor='center', relwidth=1.0, relheight=1.0)
y_scroll = Scrollbar(r, orient=VERTICAL, command=canvas.yview)
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll =Scrollbar(r, orient=HORIZONTAL, command=canvas.xview)
x_scroll.pack(side=BOTTOM, fill=X)
canvas.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')
r.update
canvas.config(scrollregion=canvas.bbox('all'))


def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)


r.title("Welcome to Airline Service System!!")
r.geometry('700x700')

id=None
n=None
n1=None
n2=None
n3=None
bi=141

def get_passenger_id():
    global id
    id = e1.get()  
    check_and_display()
    l5.pack()
    l6.pack()
    l7.pack()
    l8.pack()
    l9.pack()
    l10.pack()
    e2.pack()
    b2.pack()

def check_and_display():
    if check_id_exists(id):
        cur.execute("SELECT first_name, last_name FROM passenger WHERE p_id=%s", (id,))
        r2 = cur.fetchone()
        s = ' '.join(r2)
        l2 = Label(r, text=f"Welcome, {s}!")
        l2.pack()
        print("Welcome ",s,"!")
    else:
        l3 = Label(frame, text="Please enter your ID correctly to proceed.")
        l3.pack()
        l4 = Label(frame, text="TRY AGAIN!!")
        l4.pack()
        print("Please enter your ID correctly to proceed.")
        print("TRY AGAIN")
        r.destroy()
        sys.exit()


def check_id_exists(id):
    cur.execute("SELECT * FROM passenger WHERE p_id=%s",(id,))   	
    r1=cur.fetchone()
    return r1 is not None


def get_choice():
    global n
    n = int(e2.get())
    if(check_choice(n)):
        if(n==1):
            available()
        elif(n==2):
            status(id)
        elif(n==3):
            booking(id)
        elif(n==0):
            l11 = Label(frame, text="Have a great day")
            l11.pack()
            r.destroy()
            print("Have a great day!!")
            sys.exit()
    else:
        l12=Label(frame,text="Error!! Invalid choice. Please enter a number between 0 and 3.")
        l12.pack()
        r.destroy()
        print('"Error"\n"Invalid choice. Please enter a number between 0 and 3."')
        sys.exit()

def check_choice(n):
        if(n==0 or n==1 or n==2 or n==3):
                return True
        else:
                return False
            
def list_of_flights():
    cur.execute("SELECT * FROM flight")
    r3 = cur.fetchall()
    tree =ttk.Treeview(frame)
    tree["columns"]=("f_id", "departure_dt", "arrival_dt","origin_ac","destination_ac","no_of_seats")
    for col in tree["columns"]:
        tree.column(col, width=120)
        tree.heading(col, text=col)
    for row in r3:
        tree.insert('', 'end', values=row)
    tree.pack()


def available():
    list_of_flights()
    l12=Label(frame,text="Select your choices")
    l13=Label(frame,text="1.Continue with the flight id.")
    l14=Label(frame,text="2.Continue with origin airport code.")
    l15=Label(frame,text="3.Continue with destination airport code.")
    l12.pack()
    l13.pack()
    l14.pack()
    l15.pack()
    l16.pack()
    e3.pack()
    b3.pack()

def get_choices():
    global n1
    n1 = int(e3.get())
    if(n1==1):
        l17.pack()
        e4.pack()
        b4.pack()
        
    elif(n1==2):
        l18.pack()
        e5.pack()
        b5.pack()

    elif(n1==3):
        l19.pack()
        e6.pack()
        b6.pack()
        
def get_flight_id():
    global n3
    n3 = int(e4.get())
    cur.execute("SELECT * FROM flight WHERE f_id=%s",(n3,))
    r4 = cur.fetchall()
    tree =ttk.Treeview(frame)
    tree["columns"]=("f_id", "departure_dt", "arrival_dt","origin_ac","destination_ac","no_of_seats")
    for col in tree["columns"]:
        tree.column(col, width=100)
        tree.heading(col, text=col)
    for row in r4:
        tree.insert('', 'end', values=row)
    tree.pack()
    

def get_oac():
    global a
    a=e5.get()
    cur.execute("SELECT * FROM flight WHERE origin_ac=%s",(a,))
    r5 = cur.fetchall()
    tree =ttk.Treeview(frame)
    tree["columns"]=("f_id", "departure_dt", "arrival_dt","origin_ac","destination_ac","no_of_seats")
    for col in tree["columns"]:
        tree.column(col, width=100)
        tree.heading(col, text=col)
    for row in r5:
        tree.insert('', 'end', values=row)
    tree.pack()

def get_dac():
    global b
    b=e6.get()
    cur.execute("SELECT * FROM flight WHERE destination_ac=%s",(b,))
    r6= cur.fetchall()
    tree =ttk.Treeview(frame)
    tree["columns"]=("f_id", "departure_dt", "arrival_dt","origin_ac","destination_ac","no_of_seats")
    for col in tree["columns"]:
        tree.column(col, width=100)
        tree.heading(col, text=col)
    for row in r6:
        tree.insert('', 'end', values=row)
    tree.pack()

def status(id):
    cur.execute("SELECT * FROM booking WHERE p_id=%s",(id,))
    r7=cur.fetchall()
    tree =ttk.Treeview(frame)
    tree["columns"]=("b_id", "f_id", "p_id","status")
    for col in tree["columns"]:
        tree.column(col, width=100)
        tree.heading(col, text=col)
    for row in r7:
        tree.insert('', 'end', values=row)
    tree.pack()

def get_f_id():
    global bi
    global n2
    n2=e7.get()
    l21.pack()
    cur.execute("UPDATE flight SET no_of_seats=no_of_seats-1 WHERE f_id=%s",(n2,))
    conn.commit()
    bi+=1
    data=(bi,n2,id,"Successful")
    cur.execute("INSERT INTO booking VALUES(%s,%s,%s,%s)",data)
    conn.commit()
    

def booking(id):
    list_of_flights()
    l20.pack()
    e7.pack()
    b7.pack()

l1 = Label(frame, text="Enter your passenger ID")
l1.pack()
e1 = Entry(frame)
e1.pack()
b1 = Button(frame, text="Enter", command=get_passenger_id)
b1.pack()

l5=Label(frame,text="Choices")
l6=Label(frame,text="1.To see the available flight and available number of seats.")
l7=Label(frame,text="2.To check the status of your ticket.")
l8=Label(frame,text="3.To book a ticket.")
l9=Label(frame,text="0.To log out.")

l10 = Label(frame, text="Enter your choice")
e2 = Entry(frame)
b2 = Button(frame, text="Enter", command=get_choice)

l16 = Label(frame, text="enter your choice")
e3 = Entry(frame)
b3 = Button(frame, text="Enter", command=get_choices)

l17 = Label(frame, text="enter flight id")
e4 = Entry(frame)
b4 = Button(frame, text="Enter", command=get_flight_id)

l18 = Label(frame, text="enter the origin airport code")
e5 = Entry(frame)
b5 = Button(frame, text="Enter", command=get_oac)

l19 = Label(frame, text="enter the destination airport code")
e6= Entry(frame)
b6 = Button(frame, text="Enter", command=get_dac)

l20 = Label(frame, text="enter flight id")
e7 = Entry(frame)
b7 = Button(frame, text="Enter", command=get_f_id)

l21=Label(frame, text="Your ticket has been booked successfully you will recieve the e-ticket in your mail.")

r.mainloop()

conn.close()

