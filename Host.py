

import tkinter as tk
from tkinter import simpledialog
import mysql.connector
p=""
def databaseconnection():
    global p
    password=simpledialog.askstring("MySQL Server Connection", "Enter MySQL Password",show='*')
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=password)
    p=password
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("create database if not exists entry_exit_management_system")
    mycursor.execute("use entry_exit_management_system")
    mycursor.execute("create table if not exists host_details (host_full_name varchar(100), host_phone_no varchar(100), host_email varchar(100))")
def database_entry(data):
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=p)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use entry_exit_management_system")
    sql = "insert into host_details (host_full_name, host_phone_no, host_email) values (%s, %s, %s)"
    values=(data)
    mycursor.execute(sql, values)
    mydb.commit()
def database_check_entry():
    global data_entries
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=p)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use entry_exit_management_system")
    sql = "select * from host_details where host_full_name=%s and host_phone_no=%s"
    val = (data_entries[0], data_entries[1])
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    if result!=None:
        data_entries.clear()
        return False
    else:
        return True
def save_input_entry():
    global lb1
    global data_entries
    for i in range(3):
        var=entryvalues[i].get()
        if var=='':
            if lb1==None:
                lb1=tk.Label(root,text = "Response left unfilled",pady=8,font = "Arial 10 italic", fg='red')
                lb1.pack()
            else:
                lb1.configure(fg="red", text="Response left unfilled")
            data_entries.clear()
            return False
        elif (i==1) and len(var)!=10:
            if lb1==None:
                lb1=tk.Label(root,text = "Phone number must be of 10 digits",pady=8,font = "Arial 10 italic", fg='red')
                lb1.pack()
            else:
                lb1.configure(fg="red", text="Phone number must be of 10 digits")
            data_entries.clear()
            return False
        else:
            data_entries.append(var)
    return True
def get_input_entry():
    global lb1
    global data_entries
    if save_input_entry()==False:
        return
    else:
        if database_check_entry()==True:
            database_entry(data_entries)
            if lb1==None:
                lb1=tk.Label(root,text = "Updated",pady=8,font = "Arial 10 italic", fg='green')
                lb1.pack()
            else:
                lb1.configure(fg="green", text="Updated")
        else:
            if lb1==None:
                lb1=tk.Label(root,text = "Host already exists",pady=8,font = "Arial 10 italic", fg='red')
                lb1.pack()
            else:
                lb1.configure(fg="red", text="Host already exists")
            return
    for i in range(3):
        entryvalues[i].delete(first=0,last=30)
    data_entries.clear()
entry ="Host's Full Name", "Host's Phone number(10 digits)", "Host's Email Address"
entryvalues=[]
lb1=None
data_entries=[]
root = tk.Tk()
root.title("Host Details")
for field in entry[0:3]:
    tk.Label(root,text = field,pady=8,font = "Arial 10 bold").pack()
    e=tk.Entry(root,width = 30, justify="center")
    e.pack()
    entryvalues.append(e)    
tk.Label(root,text = '').pack()
button1=tk.Button(root, text = 'submit', pady=1, font = "Arial 10 bold", activebackground= "white")
button1.pack()
button1.config(command = get_input_entry)
tk.Label(root,text = '').pack()
root.after(10, databaseconnection)
root.geometry("300x250")
root.mainloop()
