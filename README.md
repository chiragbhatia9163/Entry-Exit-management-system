# Entry-Exit-management-system <br />
Language used - Python (backend and frontend)<br />
Requirements - MySQL, Python<br />
Password - Your MySQL server connection password<br />

**Worflow :** <br />
1. This application works by accepting details like Visitor's Name, Phone number, Email Address, Host Name from the<br />
user in the Entry tab and storing them at the backend (by creating a mysql database).<br />
2. If the host details are there in the database, then they are directly fetched or otherwise<br />
the Host's Phone number and Email Address are to be entered which will be used for future entries as well.<br />
3. Once the visitor checks in, an Email and SMS is triggered to the Host informing him of the details of the visitor.<br />
4. After the meeting or visit is over, the visitor is supposed to enter his details in the Exit tab,<br />
which inturn triggers an email to him/her stating his/her visit details.<br />
5. The database is updated at every Entry and Exit operation with Entry and Exit time of the Visitor.<br />

**Additional Features :**
1. The application starts only after the user enters MySQL server connection password. This acts as a security measure<br />
so that unauthorized people can't access the database.<br />
2. As all the entries are compulsary for the user to enter, if he/she leaves any entry empty<br />
or does not enter a valid phone number a warning message is shown on the screen.<br />
3. If the user enters a New Host's name, an acknowledgement message is shown with two more blank entries<br />
of Host's Phone number and Email address which are to be entered by the visitor.<br />

**Limitations**
1. As messaging service is paid, hence the trial version does not send SMS everytime to the Host.
2. There's no option to confirm valid email address and phone number of Visitor and Host.

**Future prospects**
1. Making a seperate UI for entry of Host data.
2. Confirming phone numbers and email addresses by sending OTP/confirmation links.
3. Displaying waiting message for a visitor if the host is in a meeting. And sending SMS/Email to the visitor once the Host is free.
4. Making the host choose his meeting hours. A message - 'Host not available' can be shown on the screen in this case.

**Links to download :**
1. You can download latest version of Python 3 from - https://www.python.org/downloads/ <br />
If you are using Windows OS, then while installing Python make sure that “Add Python to PATH “ is checked. <br />
2. You can download latest version of MySQL from - https://dev.mysql.com/downloads/installer/

**Database details :** <br />
Visitor Name, Visitor Phone number, Visitor Email ID, Visitor Name, Visitor Phone number, Visitor Email ID, Date of visit, Entry time, status, Exit time
