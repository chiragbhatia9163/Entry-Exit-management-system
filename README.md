# Entry-Exit-management-system <br />
Language used - Python (backend and frontend)<br />
Requirements - MySQL, Python<br />
Password - Your MySQL server connection password<br />

The Application has two parts:<br />
1. Host Entry<br />
2. Visitor's Entry/Exit

**Host**
1. This is the first part of the application which is to be done before entering visitor's details.
2. It works by accepting details like Host's Full Name, Host's Phone number, Host's Email Address from the<br />
user and storing them at the backend (by creating a mysql database).

**Visitor :** <br />
1. This part works by accepting details like Visitor's Name, Phone number, Email Address, Host's Full Name from the<br />
user in the Entry tab and storing them at the backend (by creating a seperate mysql database).
2. If the host details are there in the already created database, then they are directly fetched or otherwise
the 'Details not found' is shown on the screen.
3. After the visitor chooses the right Host and checks in, an Email and SMS is triggered to the Host informing him about the details of the visitor.<br />
4. After the meeting ends, the visitor is supposed to enter his details in the Exit tab, which inturn triggers an email to him/her about his/her visit details.<br />
5. The database is updated at every Entry and Exit operation with Entry and Exit time stamp of the Visitor.<br />

Only name of the Host is asked from the visitor as it is very unlikely to make a visitor enter Phone no/Email ID of the Host.
If two hosts name are same, that can be handeled by adding a suffix to such names while adding into the database.

**Additional Features :**
1. The application starts only after the user enters MySQL server connection password. This acts as a security measure<br />
so that unauthorized people can't access the database.<br />
2. As all the entries are compulsary for the user to enter, if he/she leaves any entry empty<br />
or does not enter a valid phone number a warning message is shown on the screen.<br />
3. If the host is already present in the database then the same hosts' details cannot be entered again.

**Limitations :**
1. As messaging service is paid, the trial version does not send SMS everytime to the Host. Only 3 SMS per day allowed.
2. There's no option to confirm valid Email ID and Phone no of Visitor and Host. Entering wrong Email ID and Phone no leads to error.
3. If the sql server password is wrongly entered, the application has to be restarted.
4. Host's details once entered cannot be changed. 

**Future prospects :**
1. Confirming phone numbers and email addresses by sending OTP/confirmation links.
2. Displaying waiting message for a visitor if the host is in a meeting. And sending SMS/Email to the visitor once the Host is free.
3. Making the host choose his meeting hours. A message - 'Host not available' can be shown on the screen in this case.
4. Making the host choose who should be allowed to enter the premises to meet him/her.
5. Update feature for Host's details, by providing a seperate update tab in Host UI.
6. Make the code more time efficient.

**Database details :** <br />
1. Visitor Name, Visitor Phone number, Visitor Email ID, Host Name, Date of visit, Entry time, status, Exit time <br />
2. Host Name, Host Phone number, Host Email ID

**Links to download :**
1. You can download latest version of Python 3 from - https://www.python.org/downloads/ <br />
If you are using Windows OS, then while installing Python make sure that “Add Python to PATH “ is checked. <br />
2. You can download latest version of MySQL from - https://dev.mysql.com/downloads/installer/
