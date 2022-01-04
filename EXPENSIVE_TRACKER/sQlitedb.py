import sqlite3
from tkinter import*
window=Tk()
def db():
    con=sqlite3.connect("hii.db")
    cur=con.cursor()
    # cur.execute("CREATE TABLE expense(data INTEGER,name,STRING,title STRING,expense INTEGER)")
    cur.execute("INSERT INTO expense(data,name,title,expense) VALUES(12/4/2000,'chhaya','home',233)")
    print("ok")
    con.commit()
    con.close()
db()
window.mainloop()

# print("database connected")
