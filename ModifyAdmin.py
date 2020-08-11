from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet
import pymysql
from PyQt5.QtCore import pyqtSlot

class Ui_ModifyAdminUI(object):

    def __init__(self,adminIDmodi,address,userDB,passDB,dbname):

        self.AdminIDs = adminIDmodi;
        self.address = address
        self.userDB = userDB            #lines 8 to 14 are getting the detials from the adminscreen to call on the DB here
        self.passDB = passDB
        self.dbname = dbname

    def setAdminUserInterfaces(self,Ui_AddAdmin):

        self.mainsuperadmin = Ui_AddAdmin           #16 - 18 will be used to reload data into the adminscreen without the user clicking on reload

    def setupUi(self, ModifyAdminUI):           #this sets the look and feel of the window

        self.modifyScreen = ModifyAdminUI       #this will be used to close the screen once modifying is complete

        ModifyAdminUI.setObjectName("ModifyAdminUI")
        ModifyAdminUI.resize(466, 496)
        ModifyAdminUI.setStyleSheet("background-image: url(NewYork.png);")
        self.label_7 = QtWidgets.QLabel(ModifyAdminUI)
        self.label_7.setGeometry(QtCore.QRect(150, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.UsernameAdminModi = QtWidgets.QLineEdit(ModifyAdminUI)
        self.UsernameAdminModi.setGeometry(QtCore.QRect(130, 270, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UsernameAdminModi.setFont(font)
        self.UsernameAdminModi.setText("")
        self.UsernameAdminModi.setObjectName("UsernameAdminModi")
        self.label_11 = QtWidgets.QLabel(ModifyAdminUI)
        self.label_11.setGeometry(QtCore.QRect(10, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setObjectName("label_11")
        self.LocationModi = QtWidgets.QLineEdit(ModifyAdminUI)
        self.LocationModi.setGeometry(QtCore.QRect(130, 130, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LocationModi.setFont(font)
        self.LocationModi.setText("")
        self.LocationModi.setObjectName("LocationModi")
        self.NumberOfAdminModi = QtWidgets.QLineEdit(ModifyAdminUI)
        self.NumberOfAdminModi.setGeometry(QtCore.QRect(130, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumberOfAdminModi.setFont(font)
        self.NumberOfAdminModi.setText("")
        self.NumberOfAdminModi.setObjectName("NumberOfAdminModi")
        self.label_6 = QtWidgets.QLabel(ModifyAdminUI)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.PasswordAdminModi = QtWidgets.QLineEdit(ModifyAdminUI)
        self.PasswordAdminModi.setGeometry(QtCore.QRect(130, 340, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordAdminModi.setFont(font)
        self.PasswordAdminModi.setText("")
        self.PasswordAdminModi.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordAdminModi.setObjectName("PasswordAdminModi")
        self.label_9 = QtWidgets.QLabel(ModifyAdminUI)
        self.label_9.setGeometry(QtCore.QRect(10, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.NameOfAdminModi = QtWidgets.QLineEdit(ModifyAdminUI)
        self.NameOfAdminModi.setGeometry(QtCore.QRect(130, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameOfAdminModi.setFont(font)
        self.NameOfAdminModi.setText("")
        self.NameOfAdminModi.setObjectName("NameOfAdminModi")
        self.label_10 = QtWidgets.QLabel(ModifyAdminUI)
        self.label_10.setGeometry(QtCore.QRect(10, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(ModifyAdminUI)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.DeleteAdmin = QtWidgets.QPushButton(ModifyAdminUI)
        self.DeleteAdmin.setGeometry(QtCore.QRect(10, 440, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteAdmin.setFont(font)
        self.DeleteAdmin.setObjectName("DeleteAdmin")
        self.UpdateAdmin = QtWidgets.QPushButton(ModifyAdminUI)
        self.UpdateAdmin.setGeometry(QtCore.QRect(350, 440, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UpdateAdmin.setFont(font)
        self.UpdateAdmin.setAcceptDrops(False)
        self.UpdateAdmin.setObjectName("UpdateAdmin")

        self.retranslateUi(ModifyAdminUI)
        QtCore.QMetaObject.connectSlotsByName(ModifyAdminUI)
        
        self.DeleteAdmin.clicked.connect(self.delete)          #clicking on this delete a user
        self.DeleteAdmin.clicked.connect(ModifyAdminUI.close)  #while it deletes it will close the window

        self.UpdateAdmin.clicked.connect(self.update)   #clicking the update button will run the update function
        
        self.setVariabless()    #this functions sets the data into the input for user to easily modify

    def setVariabless(self):
        try:
            conn = pymysql.connect(host = self.address,
                                       user = self.userDB,
                                       passwd = self.passDB ,       
                                       db = self.dbname)	
   
            myCursor = conn.cursor()		
            Query = ("SELECT * FROM adminusers WHERE AdminID = %s")		    
       
            data = myCursor.execute(Query,(self.AdminIDs))		
            myresult = myCursor.fetchall()

            for x in myresult:
                adname = x[1];
                location = x[2];
                number = x[3];                  #this will gather all the details from DB and create new variables of itself.
                field = x[4];
                username = x[5];
                password = x[6];

            file = open('key.key','rb')
            key = file.read()
            file.close() 
            f2 = Fernet(key)
            decrypted = f2.decrypt(str.encode(password))        #lines 152 - 157 , this is similar to the other decyption passwords that will decrepty for users to easily 
            passwerd = decrypted.decode()


            self.NameOfAdminModi.setText(adname)
            self.LocationModi.setText(location)
            self.NumberOfAdminModi.setText(str(number))     #this sets the textboxes from what is stored in the DB
            self.UsernameAdminModi.setText(username)
            self.PasswordAdminModi.setText(passwerd)

            conn.commit()
            conn.close

        except:
            self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect    

    def update(self):

        name = self.NameOfAdminModi.text()		
        location = self.LocationModi.text()		
        number = self.NumberOfAdminModi.text()		        #line 174 to 179 create new instances of itself
        username = self.UsernameAdminModi.text()	    
        password = self.PasswordAdminModi.text()
        ID =self.AdminIDs

        file = open('key.key','rb')
        key = file.read()
        file.close()
        encoded = password.encode()
        f = Fernet(key)
        encrypted = f.encrypt(encoded) #this is the encrpyted form of the password

        try:

            conn = pymysql.connect(host = self.address,
                                       user = self.userDB,
                                       passwd = self.passDB ,
                                       db = self.dbname)	
        
            myCursor = conn.cursor()	
        
            if(len(str(number)) == 11): #if the number equals 11 characters it will continue
                query = ("UPDATE adminusers SET AdminName = %s,Location = %s,Number = %s,Username = %s,Password = %s WHERE AdminID = %s") #this is the SQL to update all fields
                
                data = myCursor.execute(query,(name,location,number,username,encrypted,ID))	
                conn.commit()
                conn.close()
            
                print("> Data Updated ")
                if self.mainsuperadmin != None: #send data back to the table to automatically be updated
                    self.mainsuperadmin.loadAdmin() 
                    self.modifyScreen.close() #willl close the window

            elif(len(str(number)) < 11 or len(str(number)) > 11 ): #if number is less than 11 or greater it will not allow to update

                self.messagebox("","Please enter correct length for phone number")

            elif(name == '' or location == '' or username == ''):   #similar if fields are left open it will not allow update
                self.messagebox("","Please enter all fields")

            else:
                self.messageebox("","Please enter all fields")

        except:
            self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect      
            
    def delete(self):
        
        IDdelete = self.AdminIDs;   #getting the ID to know which user to be deleted

        try:
            conn = pymysql.connect(host = self.address,
                                        user = self.userDB,
                                        passwd = self.passDB,
                                        db = self.dbname)		

            myCursor = conn.cursor()		

            query = ("DELETE FROM adminusers WHERE AdminID = %s" )		#SQL to delete the admin 
       
            data = myCursor.execute(query,(IDdelete))		
      
            print("> Data deleted ")		
            conn.commit()		
            conn.close()

            if self.mainsuperadmin != None: #send data back to the table to automatically be updated
                self.mainsuperadmin.loadAdmin()
                self.modifyScreen.close() #will close once deleted
        except:
                self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                              #lines 248 to 254 are the parameters set for the message box.
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def retranslateUi(self, ModifyAdminUI):
        _translate = QtCore.QCoreApplication.translate
        ModifyAdminUI.setWindowTitle(_translate("ModifyAdminUI", "Modify "))
        self.label_7.setText(_translate("ModifyAdminUI", "Update or Delete Admin"))
        self.UsernameAdminModi.setToolTip(_translate("ModifyAdminUI", "The username for the admin"))
        self.label_11.setText(_translate("ModifyAdminUI", "Password"))
        self.LocationModi.setToolTip(_translate("ModifyAdminUI", "The location of admin"))
        self.NumberOfAdminModi.setToolTip(_translate("ModifyAdminUI", "The admin phone number"))
        self.label_6.setText(_translate("ModifyAdminUI", "Name "))
        self.PasswordAdminModi.setToolTip(_translate("ModifyAdminUI", "The password for the admin"))
        self.label_9.setText(_translate("ModifyAdminUI", "Number"))
        self.NameOfAdminModi.setToolTip(_translate("ModifyAdminUI", "The name of the admin "))
        self.label_10.setText(_translate("ModifyAdminUI", "Username "))
        self.label_8.setText(_translate("ModifyAdminUI", "Location"))
        self.DeleteAdmin.setToolTip(_translate("ModifyAdminUI", "Click to delete admin"))
        self.DeleteAdmin.setText(_translate("ModifyAdminUI", "Delete"))
        self.UpdateAdmin.setToolTip(_translate("ModifyAdminUI", "Click to update admin"))
        self.UpdateAdmin.setText(_translate("ModifyAdminUI", "Update"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyAdminUI = QtWidgets.QDialog()
    ui = Ui_ModifyAdminUI()
    ui.setupUi(ModifyAdminUI)
    ModifyAdminUI.show()
    app.exec_()
