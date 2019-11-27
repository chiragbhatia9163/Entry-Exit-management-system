# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import mysql.connector
import time
import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(val,exit_time=0):
    sender_email = "summergeeksinnovaccer@gmail.com"
    receiver_email = val[5]
    password = "innovaccer123"
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    if exit_time==0:
        message["Subject"] = "New Visitor"
        html = """\
        <html><body>
        <table align="center", border="2">
        <tr><th colspan="2">VISITOR'S DETAILS</th></tr>
        <tr><td>Name</td><td>"""+val[0]+"""</td></tr>
        <tr><td>Phone number</td><td>"""+val[1]+"""</td></tr>
        <tr><td>Email ID</td><td>"""+val[2]+"""</td></tr>
        <tr><td>Check-in Date</td><td>"""+val[6]+"""</td></tr>
        <tr><td>Check-in Time</td><td>"""+val[7]+"""</td></tr>
        </table><p align="center">Have a Nice Day</p>
        </body></html>"""
    else:
        message["Subject"] = "Thankyou for Visiting"
        html = """\
        <html><body><style>
        table, th, td {border: 1px solid black;}</style>
        <table align="center", border="2">
        <tr><th colspan="2">VISITING DETAILS</th></tr>
        <tr><td>Name</td><td>"""+val[0]+"""</td></tr>
        <tr><td>Phone number</td><td>"""+val[1]+"""</td></tr>
        <tr><td>Check-in Time</td><td>"""+val[7]+"""</td></tr>
        <tr><td>Check-out Time</td><td>"""+exit_time+"""</td></tr>
        <tr><td>Host Name</td><td>"""+val[3]+"""</td></tr>
        <tr><td>Address Visited</td><td>Innovaccer</td></tr>
        </table><p align="center">Have a Nice Day</p>
        </body></html>"""
    part = MIMEText(html, "html")
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def sms(number,message):
    URL = 'https://www.way2sms.com/api/v1/sendCampaign'
    # get request
    def sendGetRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
        'apikey':apiKey,
        'secret':secretKey,
        'usetype':useType,
        'phone': phoneNo,
        'message':textMessage,
        'senderid':senderId}
        return requests.get(reqUrl, req_params)
    # get response
    request=sendGetRequest(URL, '4RTRNRVVB4J9P1H1S4GO8N8A4ZR7AZNB', 'JWHLL6Z2DNTCW9WX', 'stage' , number, 'Innova', message )

p=""
def return_date_and_time():
    t=time.strftime("%c").split()
    return (t[2]+" "+t[1]+ " "+t[4]), t[3]

def databaseconnection():
    global p
    password=simpledialog.askstring("MySQL Server Connection", "Enter MySQL Password",show='*')
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=password)
    p=password
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("create database if not exists entry_exit_management_system")
    mycursor.execute("use entry_exit_management_system")
    mycursor.execute("create table if not exists entry_exit_record (visitor_name varchar(100), visitor_phone_no varchar(100), visitor_email varchar(100), host_full_name varchar(100), host_phone_no varchar(100), host_email varchar(100), date_of_visit varchar(100) ,entry_time varchar(100), status varchar(4), exit_time varchar(100))")
    
def database_entry(data,email,number,date,time):
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=p)
    mycursor = mydb.cursor(buffered=True)
    val=[]
    if len(data)==6:
        val=data+[date,time,'in']
    else:
        val=data+[number,email,date,time,'in']
    send_email(val)
    message="VISITOR'S DETAILS\nName - "+ val[0] + "\nPhone number - " + val[1] + "\nEmail ID - " + val[2] + "\nCheck-in Date " + val[6] + "\nCheck-in Time - " + val[7]
    sms(val[4],message)
    mycursor.execute("use entry_exit_management_system")
    sql = "insert into entry_exit_record (visitor_name, visitor_phone_no, visitor_email, host_full_name, host_phone_no, host_email, date_of_visit, entry_time, status) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values=(val)
    mycursor.execute(sql, values)
    mydb.commit()

def save_input_exit():
    global lb2
    global data_exit
    for i in range(2):
        var=exitvalues[i].get()
        if var=='':
            if lb2==None:
                lb2=tk.Label(tab2,text = "Response left unfilled",pady=8,font = "Arial 10 italic", fg='red')
                lb2.pack()
            else:
                lb2.configure(fg="red", text="Response left unfilled")
            data_exit.clear()
            return False
        elif (i==1) and len(var)!=10:
            if lb2==None:
                lb2=tk.Label(tab2,text = "Phone number must be of 10 digits",pady=8,font = "Arial 10 italic", fg='red')
                lb2.pack()
            else:
                lb2.configure(fg="red", text="Phone number must be of 10 digits")
            data_exit.clear()
            return False
        else:
            data_exit.append(var)
    return True

def save_input_entry(no_of_entries):
    global lb1
    global data_entries
    for i in range(no_of_entries):
        var=entryvalues[i].get()
        if var=='':
            if lb1==None:
                lb1=tk.Label(tab1,text = "Response left unfilled",pady=8,font = "Arial 10 italic", fg='red')
                lb1.pack()
            else:
                lb1.configure(fg="red", text="Response left unfilled")
            data_entries.clear()
            return False
        elif (i==1 or i==4) and len(var)!=10:
            if lb1==None:
                lb1=tk.Label(tab1,text = "Phone number must be of 10 digits",pady=8,font = "Arial 10 italic", fg='red')
                lb1.pack()
            else:
                lb1.configure(fg="red", text="Phone number must be of 10 digits")
            data_entries.clear()
            return False
        else:
            data_entries.append(var)
    return True

def database_check_hostname(host):
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=p)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use entry_exit_management_system")
    sql = "select host_email,host_phone_no from entry_exit_record where host_full_name=%s"
    val = ([host])
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result==None:
        return None,None
    return result[0], result[1]

def database_check_exit():
    global data_exit
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=p)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use entry_exit_management_system")
    sql = "select * from entry_exit_record where visitor_name=%s and visitor_phone_no=%s and status='in'"
    val = ([data_exit[0], data_exit[1]])
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    if result==None:
        data_exit.clear()
        return False
    sql = "update entry_exit_record set exit_time=%s,status='out' where visitor_name=%s and date_of_visit=%s and entry_time=%s"
    t=time.strftime("%c").split()[3]
    val = ([str(t),result[0],result[6],result[7]])
    mycursor.execute(sql, val)
    mydb.commit()
    send_email(result,t)
    return True

def get_input_exit():
    global lb2
    global data_exit
    if save_input_exit()==False:
        return
    else:
        if database_check_exit()==True:
            if lb2==None:
                lb2=tk.Label(tab2,text = "Updated",pady=8,font = "Arial 10 italic", fg='green')
                lb2.pack()
            else:
                lb2.configure(fg="green", text="Updated")
        else:
            if lb2==None:
                lb2=tk.Label(tab2,text = "Details not correct",pady=8,font = "Arial 10 italic", fg='red')
                lb2.pack()
            else:
                lb2.configure(fg="red", text="Details not correct")
            return
    for i in range(2):
        exitvalues[i].delete(first=0,last=30)
    data_exit.clear()

def get_input_entry():
    global lb1
    global data_entries
    global no_of_entries
    global button1
    if save_input_entry(no_of_entries)==False:
        return
    if len(data_entries)==4:
        email,number=database_check_hostname(data_entries[3])
        if email==None or number==None:
            data_entries.clear()
            if lb1!=None:
                lb1.destroy()
            button1.pack_forget()
            for field in entry[4:6]:
                l=tk.Label(tab1,text = field,pady=8,font = "Arial 10 bold")
                l.pack()
                lab.append(l)
                e=tk.Entry(tab1,width = 30, justify="center")
                e.pack()
                entryvalues.append(e)
            button1.pack()
            lb1=tk.Label(tab1,text = "Seems like you've chosen a New Host\nKindly enter some more details and press submit",pady=8,font = "Arial 10 italic", fg='red')
            lb1.pack()
            no_of_entries=6
        else:
            date,time=return_date_and_time()
            database_entry(data_entries,email,number,date,time)
            for i in range(4):
                entryvalues[i].delete(first=0,last=30)
            if lb1==None:
                lb1=tk.Label(tab1,text = "Updated",pady=8,font = "Arial 10 italic", fg='green')
                lb1.pack()
            else:
                lb1.configure(fg="green", text="Updated")
            data_entries.clear()
    elif len(data_entries)==6:
        no_of_entries=4
        for i in range(2):
            lab[i].destroy()
            entryvalues[5-i].destroy()
            entryvalues.pop(5-i)
        lb1.configure(fg="green", text="Updated")
        for i in range(4):
            entryvalues[i].delete(first=0,last=30)
        lab.clear()
        date,time=return_date_and_time()
        database_entry(data_entries,0,0,date,time)
        data_entries.clear()
entry = "Visitor's Full Name", "Visitor's Phone Number (10 digits)", "Visitor's Email Address", "Host's Full Name", "Host's Phone number(10 digits)", "Host's Email Address"
entryvalues=[]
exitvalues=[]
lb1,lb2=None,None
data_entries=[]
data_exit=[]
lab=[]
no_of_entries=4
root = tk.Tk()
root.title("Entry-Exit Management System")
s = ttk.Style()
s.theme_create( "mytheme", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },"TNotebook.Tab": {"configure": {"padding": [100, 10], "font" : ('Arial', '13', 'bold') },"map":{"background": [("selected", "#ffffff")],"expand": [("selected", [1, 1, 1, 0])] } } } )
s.theme_use("mytheme")
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Entry")
for field in entry[0:4]:
    tk.Label(tab1,text = field,pady=8,font = "Arial 10 bold").pack()
    e=tk.Entry(tab1,width = 30, justify="center")
    e.pack()
    entryvalues.append(e)    
tk.Label(tab1,text = '').pack()
button1=tk.Button(tab1, text = 'submit', pady=1, font = "Arial 10 bold", activebackground= "white")
button1.pack()
button1.config(command = get_input_entry)
tk.Label(tab1,text = '').pack()
tab2 = tk.Frame(notebook,)
notebook.add(tab2, text="Exit")
for field in entry[0:2]:
    tk.Label(tab2,text = field,pady=8,font = "Arial 10 bold").pack()
    e=tk.Entry(tab2,width = 30, justify="center")
    e.pack()
    exitvalues.append(e)
tk.Label(tab2,text = '').pack()
button2=tk.Button(tab2, text = 'submit', pady=1, font = "Arial 10 bold", activebackground= "#ffffff")
button2.pack()
button2.config(command = get_input_exit)
notebook.grid(row=0, column=0, sticky="nw")
root.after(10, databaseconnection)
root.mainloop()

