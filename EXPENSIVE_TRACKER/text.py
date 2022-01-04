from tkinter import *
import sqlite3
from tkcalendar import *
from tkinter import ttk
def db():
    con=sqlite3.connect("hii.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE expense(data INTEGER,name,STRING,title STRING,expense INTEGER)")
    print("ok")
    cur.close()
db()
window=Tk()
window.geometry("820x700")
window.title("expense Tracker")
DateEntry(window,text="mm/dd/yyyy").place(x=200,y=50)
lable1 = Label(window,text="date" ,font=("Arial bold",16)).place(x=40,y=60)
DateEntry(window,text="mm/dd/yyyy").place(x=200,y=50)

lable2= Label(window,text="name" ,font=("Arial bold",16)).place(x=40,y=110)
bt1=Entry(window).place(x=200,y=110)
lable3= Label(window,text="Title",font=("Arial bold",16)).place(x=40,y=170)
bt2=Entry(window).place(x=200,y=170)
lable4 = Label(window,text="expense",font=("Arial bold",16)).place(x=40,y=220)
bt3=Entry(window).place(x=200,y=220)

button=Button(window,text="submit",bg="red",fg="black").place(x=200,y=300)

Elist=['Date','Name','Title','Expense']
Etable=ttk.Treeview(window,column=Elist,show='headings',height=7)
for c in Elist:
    Etable.heading(c,text=c.title())
Etable.grid(row=5,column=0,padx=7,pady=400,columnspan=3)
window.mainloop()

    