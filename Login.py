# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from AdminScreen import Ui_AddAdmin
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
from PyQt5.QtGui import QKeySequence
from cryptography.fernet import Fernet
from AdminScreen import Ui_AddAdmin
import pymysql
#the above is the imports that are needed to run specific functions.

f = open("Main.txt","r")  #this is used to open up the file where the database settings are kept

dbname = str(f.readline())
dbname =  dbname.replace('\n','' )
userDB = str(f.readline())
userDB =  userDB.replace('\n','' )
passDB =  str(f.readline())                     #lines 20 - 27 are used to get clear variables from the text in the file that was opened.
passDB =  passDB.replace('\n','' )
address = str(f.readline())
address = address.replace('\n','' )

class Ui_LoginWin(QDialog):
    #The below is used to build the form and call certain functions when clicked on.
    def setupUi(self, LoginWin):
        LoginWin.setObjectName("LoginWin")
        LoginWin.resize(350, 261)
        LoginWin.setStyleSheet("background-image: url(NewYork.png);")
        self.groupBox = QtWidgets.QGroupBox(LoginWin)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 351, 281))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Username = QtWidgets.QLineEdit(self.groupBox)
        self.Username.setGeometry(QtCore.QRect(130, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Username.setFont(font)
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.groupBox)
        self.Password.setGeometry(QtCore.QRect(130, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password.setFont(font)
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.CancelBtn = QtWidgets.QPushButton(self.groupBox)
        self.CancelBtn.setGeometry(QtCore.QRect(10, 210, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setObjectName("CancelBtn")
        self.LoginBtn = QtWidgets.QPushButton(self.groupBox)
        self.LoginBtn.setGeometry(QtCore.QRect(250, 210, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LoginBtn.setFont(font)
        self.LoginBtn.setObjectName("LoginBtn")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.LoginBtn.clicked.connect(self.login) #this will open and run the function called login

        self.CancelBtn.clicked.connect(LoginWin.close) #this will close the form when clicked

        QtCore.QMetaObject.connectSlotsByName(LoginWin)
        self.retranslateUi(LoginWin)

        self.address = address
        self.dbname = dbname
        self.passDB = passDB        #line 92 - 95 are used to call the database variable.
        self.userDB = userDB

        LoginWin.keyPressEvent = self.keyPressEvents;   #this is used to allow shortcuts for buttons.

    def keyPressEvents(self, event):
        if event.key() == QtCore.Qt.Key_Return: #if enter button is clicked then it will go to login function

            self.login() 

        elif event.key() == QtCore.Qt.Key_Escape: #if escape button is clicked then it will close the login
            
            LoginWin.close()
        
    def login(self):    #this is used to create
        
        self.disabletab = 0;

        file = open('key.key','rb') #these 3 lines get the key that will be used for decrpytion of the password
        key = file.read()
        file.close()
        

        if(self.Password.text() == "" or self.Username.text() == "" ):
            self.messagebox("Error","Please enter all fields");         #117 - 118 are checking if any of the inputs are left blank
      
        else:

            passwd = self.Password.text();
            usernm = self.Username.text();

            try:        #try statment used to check if it can make a connection to the DB

                conn = pymysql.connect(host =address,
                                           user = userDB,
                                           passwd = passDB ,        #lines 127 and 130 are used to create connection to DB
                                           db = dbname)
            
                myCursor = conn.cursor()


                GetEncrypt = ("SELECT * FROM adminusers WHERE Username = %s")       #query to get the details of the password
                getEncrpytion = myCursor.execute(GetEncrypt,(usernm))               # this is then calling the sql 

          

                myresult = myCursor.fetchall() #this will gather all the details from the database

                if(len(myresult) == 0): #if there is no result then it will show this message box
                    self.messagebox("Error","Please enter a valid user");

                else:

                    for x in myresult:      #the following for loop will get the column that I am looking for which is the passowrd
                        enccrpytedpassword = x[6];


                    f2 = Fernet(key)
                    decrypted = f2.decrypt(str.encode(enccrpytedpassword))   #line 151 to 152 will be decrypting the password that was gotten from DB

                    passwerd = decrypted.decode() #then will decode the message


                    if(str(passwerd) == passwd): #Now checking if the user entered the correct password

                        query = ("SELECT * FROM adminusers WHERE Username = %s AND Password = %s" ) #SQL for getting all the details for the user 
                        data = myCursor.execute(query,(usernm,enccrpytedpassword))
         
  

                        if(data > 0 ):      #if there is a field with data populated it will continue

                                   myresult = myCursor.fetchall()

                                   for x in myresult:   
                                       field = x[4];          #this is used to get the users field.

           
                                   if(field == 'Super-Admin'):  #once gotten the field it will check if the user is a super-admin

                                       self.disabletab = 0  #No tabs disabled cause user is super-admin
              
                                       self.mainscreen(self.disabletab,self.address,self.userDB,self.passDB,self.dbname)    #sending DB details and if tabs should be disabled to the main screen function
          

                                   elif(field == 'Normal Admin'):  #if user is a normal admin then the following will run

                                       self.disabletab = 1;  #as this is a normal admin it will disable certain fields in the main screen , this is used via a boolen check
                                       self.mainscreen(self.disabletab,self.address,self.userDB,self.passDB,self.dbname)    #sending information to main screen function
                          
                                   else:
                                     self.messagebox("Error","Please confirm username or password");

           
                        else:
                                   self.messagebox("Error","No user exists");
        
                        conn.close()  
                        LoginWin.close() #will close the window once successful 
                    else:
                         self.messagebox("Error","The Details do not match");
            except:
                self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect

    def mainscreen(self,disabletab,address,userDB,passDB,dbname): #this is the funtion to send detials across to main screen
        self.main = QtWidgets.QMainWindow() #calling the main window 

        self.tabID = self.disabletab
        self.addres = self.address
        self.userdb = self.userDB       #lines 201-2015 are the new details to be sent across 
        self.passdb = self.passDB
        self.DBname = self.dbname

        self.ui = Ui_AddAdmin(self.tabID,self.addres,self.userdb,self.passdb,self.DBname) #sending details to adminScreen class
        self.ui.setupUi(self.main)
        self.main.show()        #opening the screen

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          #line 211 to 217 are the perameters to set the display message boxes
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()     

    def retranslateUi(self, LoginWin):
        _translate = QtCore.QCoreApplication.translate
        LoginWin.setWindowTitle(_translate("LoginWin", "Login"))
        self.label.setText(_translate("LoginWin", "Username : "))
        self.label_2.setText(_translate("LoginWin", "Password  :"))
        self.CancelBtn.setText(_translate("LoginWin", "Cancel"))
        self.LoginBtn.setText(_translate("LoginWin", "Login"))
        self.label_3.setText(_translate("LoginWin", "DPM Systems"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWin = QtWidgets.QDialog()
    ui = Ui_LoginWin()
    ui.setupUi(LoginWin)
    LoginWin.show()
    
    app.exec_()
