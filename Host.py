# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
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

def database_check_update():
    global data_update
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=p)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use entry_exit_management_system")
    sql = "select * from host_details where host_full_name=%s and host_phone_no=%s"
    val = ([data_update[0], data_update[1]])
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    if result==None:
        data_update.clear()
        return False
    sql = "update host_details set host_full_name=%s,host_email=%s where host_phone_no=%s"
    val = ([data_update[0],data_update[2],result[1]])
    mycursor.execute(sql, val)
    mydb.commit()
    sql = "update host_details set host_phone_no=%s where host_full_name=%s and host_email=%s"
    val = ([data_update[2],data_update[0],data_update[1]])
    mycursor.execute(sql, val)
    mydb.commit()
    return True

def save_update_values():
    global lb2
    global data_update
    for i in range(3):
        var=updatevalues[i].get()
        if var=='':
            if lb2==None:
                lb2=tk.Label(tab2,text = "Response left unfilled",pady=8,font = "Arial 10 italic", fg='red')
                lb2.pack()
            else:
                lb2.configure(fg="red", text="Response left unfilled")
            data_update.clear()
            return False
        elif (i==1) and len(var)!=10:
            if lb2==None:
                lb2=tk.Label(tab2,text = "Phone number must be of 10 digits",pady=8,font = "Arial 10 italic", fg='red')
                lb2.pack()
            else:
                lb2.configure(fg="red", text="Phone number must be of 10 digits")
            data_update.clear()
            return False
        else:
            data_update.append(var)
    return True
def update_details():
    global lb2
    global data_update
    if save_update_values()==False:
        return
    else:
        if database_check_update()==True:
            if lb2==None:
                lb2=tk.Label(tab2,text = "Updated",pady=8,font = "Arial 10 italic", fg='green')
                lb2.pack()
            else:
                lb2.configure(fg="green", text="Updated")
            for i in range(2):
                updatevalues[i].delete(first=0,last=30)
        else:
            if lb2==None:
                lb2=tk.Label(tab2,text = "Details not correct",pady=8,font = "Arial 10 italic", fg='red')
                lb2.pack()
            else:
                lb2.configure(fg="red", text="Details not correct")
            return
    data_update.clear()

def get_input_entry():
    global lb1
    global data_entries
    if save_input_entry()==False:
        return
    else:
        if database_check_entry()==True:
            database_entry(data_entries)
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
updatevalues=[]
lb1,lb2=None,None
data_entries=[]
data_update=[]
root = tk.Tk()
root.title("Host Details")
s = ttk.Style()
s.theme_create( "mytheme", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },"TNotebook.Tab": {"configure": {"padding": [100, 10], "font" : ('Arial', '13', 'bold') },"map":{"background": [("selected", "#ffffff")],"expand": [("selected", [1, 1, 1, 0])] } } } )
s.theme_use("mytheme")
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Entry")
for field in entry[0:3]:
    tk.Label(tab1,text = field,pady=8,font = "Arial 10 bold").pack()
    e=tk.Entry(tab1,width = 30, justify="center")
    e.pack()
    entryvalues.append(e)    
tk.Label(tab1,text = '').pack()
button1=tk.Button(tab1, text = 'submit', pady=1, font = "Arial 10 bold", activebackground= "white")
button1.pack()
button1.config(command = get_input_entry)
lb1=tk.Label(tab1,text = '')
lb1.pack()
tab2 = tk.Frame(notebook,)
notebook.add(tab2, text="Update")
for field in entry[0:3]:
    tk.Label(tab2,text = field,pady=8,font = "Arial 10 bold").pack()
    e=tk.Entry(tab2,width = 30, justify="center")
    e.pack()
    updatevalues.append(e)
tk.Label(tab2,text = '').pack()
button2=tk.Button(tab2, text = 'submit', pady=1, font = "Arial 10 bold", activebackground= "#ffffff")
button2.pack()
button2.config(command = update_details)
lb2=tk.Label(tab1,text = '')
lb2.pack()
root.after(10, databaseconnection)
notebook.grid(row=0, column=0, sticky="nw")
root.mainloop()