
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtCore import pyqtSlot

from cryptography.fernet import Fernet

class Ui_ModifyUserUI(object):

   
    def __init__(self,namess,addres,userdb,passdb,DBname):
        self.USerIDs = namess;
        self.address = addres
        self.userDB = userdb        #lines 12 to 16 are getting the detials from the adminscreen to call on the DB here
        self.passDB = passdb
        self.dbname = DBname

    def setAdminUserInterface(self,Ui_AddAdmin):

        self.mainadmin = Ui_AddAdmin  #18 - 20 will be used to reload data into the adminscreen without the user clicking on reload

    def setupUi(self, ModifyUserUI):  #this sets the look and feel of the window

        self.modScreen = ModifyUserUI  #this will be used to close the screen once modifying is complete

        ModifyUserUI.setObjectName("ModifyUserUI")
        ModifyUserUI.resize(468, 394)
        ModifyUserUI.setStyleSheet("background-image: url(NewYork.png);")
        self.label_8 = QtWidgets.QLabel(ModifyUserUI)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(ModifyUserUI)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.NameOfPersonAdd = QtWidgets.QLineEdit(ModifyUserUI)
        self.NameOfPersonAdd.setGeometry(QtCore.QRect(150, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameOfPersonAdd.setFont(font)
        self.NameOfPersonAdd.setText("")
        self.NameOfPersonAdd.setObjectName("NameOfPersonAdd")
        self.NumberOfPersonAdd = QtWidgets.QLineEdit(ModifyUserUI)
        self.NumberOfPersonAdd.setGeometry(QtCore.QRect(150, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumberOfPersonAdd.setFont(font)
        self.NumberOfPersonAdd.setText("")
        self.NumberOfPersonAdd.setObjectName("NumberOfPersonAdd")
        self.label_9 = QtWidgets.QLabel(ModifyUserUI)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.PostCodeAdd = QtWidgets.QLineEdit(ModifyUserUI)
        self.PostCodeAdd.setGeometry(QtCore.QRect(150, 130, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PostCodeAdd.setFont(font)
        self.PostCodeAdd.setText("")
        self.PostCodeAdd.setObjectName("PostCodeAdd")
        self.LicenceAdd = QtWidgets.QLineEdit(ModifyUserUI)
        self.LicenceAdd.setGeometry(QtCore.QRect(150, 270, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LicenceAdd.setFont(font)
        self.LicenceAdd.setText("")
        self.LicenceAdd.setObjectName("LicenceAdd")
        self.label_10 = QtWidgets.QLabel(ModifyUserUI)
        self.label_10.setGeometry(QtCore.QRect(30, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(ModifyUserUI)
        self.label_7.setGeometry(QtCore.QRect(180, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.Back = QtWidgets.QPushButton(ModifyUserUI)
        self.Back.setGeometry(QtCore.QRect(580, 390, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.DeleteUser = QtWidgets.QPushButton(ModifyUserUI)
        self.DeleteUser.setGeometry(QtCore.QRect(150, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteUser.setFont(font)
        self.DeleteUser.setObjectName("DeleteUser")
        self.UpdateUser = QtWidgets.QPushButton(ModifyUserUI)
        self.UpdateUser.setGeometry(QtCore.QRect(330, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UpdateUser.setFont(font)
        self.UpdateUser.setObjectName("UpdateUser")

        self.retranslateUi(ModifyUserUI)
        QtCore.QMetaObject.connectSlotsByName(ModifyUserUI)


        self.UpdateUser.clicked.connect(self.update)  #clicking the update button will run the update function
        

        self.DeleteUser.clicked.connect(self.delete)#clicking on this delete a user
        self.DeleteUser.clicked.connect(ModifyUserUI.close) #while it deletes it will close the window


        self.setVariables()  #this functions sets the data into the input for user to easily modify

     
    def setVariables(self):
        try:

            conn = pymysql.connect(host = self.address,
                                       user = self.userDB,
                                       passwd = self.passDB ,
                                       db = self.dbname)
   
            myCursor = conn.cursor()		
            Query = ("SELECT * FROM userprofile WHERE UserID = %s")		
       
            data = myCursor.execute(Query,(self.USerIDs))		
            myresult = myCursor.fetchall()

            for x in myresult:
                name = x[1];
                postcode = x[2];
                number = x[3];                       #lines 141 - 145 will gather all the details from DB and create new variables of itself.
                licence = x[4];

            self.NameOfPersonAdd.setText(name)
            self.PostCodeAdd.setText(postcode)               #Lines 147 - 150  sets the textboxes from what is stored in the DB
            self.NumberOfPersonAdd.setText(str(number))
            self.LicenceAdd.setText(licence)

            conn.commit()		
            conn.close

        except:
            self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect    
        
    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)                                   #Lines 158-164 set the parametres of the message box
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()    

    def update(self):

        nameupdate = self.NameOfPersonAdd.text()		
        postcodeupdate = self.PostCodeAdd.text()		
        numberupdate = self.NumberOfPersonAdd.text()		 #line 168 to 172 create new instances of itself
        licenceupdate = self.LicenceAdd.text()		
        IDupdate = self.USerIDs;

        try:

            conn = pymysql.connect(host = self.address,
                                       user = self.userDB,
                                       passwd = self.passDB ,
                                       db = self.dbname)
            myCursor = conn.cursor()		

      
            query = ("UPDATE userprofile SET UserName = %s,PostCode = %s,Number = %s,Licence = %s WHERE UserID = %s")	#this is getting the SQL query ready for use to update
       
            if(len(str(numberupdate)) == 11): #if the number equals 11 characters it will continue

                data = myCursor.execute(query,(nameupdate,postcodeupdate,numberupdate,licenceupdate,IDupdate)) #this will execute the query 
                conn.commit()	
            
                print("> Data Updated ")
                if self.mainadmin != None: #send data back to the table to automatically be updated
                    self.mainadmin.loaddata()
                    self.modScreen.close()
                 
       
            elif(len(str(numberupdate)) < 11 or len(str(numberupdate)) > 11):  #if number is less than 11 or greater it will not allow to update
                 self.messagebox("","Please enter correct length for phone number")
             
        

            elif(nameupdate == '' or postcodeupdate == '' or licenceupdate == ''):#similar check on if fields are left open it will not allow update

                self.messagebox("","Please enter all the fields")

        
            conn.close()
        except:
             self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect    

    def delete(self):

        	
        IDdelete = self.USerIDs; #getting the ID to know which user to be deleted
        try:

            conn = pymysql.connect(host = self.address,
                                       user = self.userDB,
                                       passwd = self.passDB ,
                                       db = self.dbname)

            myCursor = conn.cursor()		

            query = ("DELETE FROM userprofile WHERE UserID = %s" )		#SQL to delete the user 
       
            data = myCursor.execute(query,(IDdelete))		
      
            print("> Data deleted ")		
            conn.commit()		
            conn.close()

            if self.mainsuperadmin != None: #send data back to the table to automatically be updated
                self.mainsuperadmin.loadAdmin()
                self.modifyScreen.close() #will close once deleted

        except:
            self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect
            

    def retranslateUi(self, ModifyUserUI):
        _translate = QtCore.QCoreApplication.translate
        ModifyUserUI.setWindowTitle(_translate("ModifyUserUI", "ModifyUser"))
        self.label_8.setText(_translate("ModifyUserUI", "Post Code"))
        self.label_6.setText(_translate("ModifyUserUI", "Name "))
        self.NameOfPersonAdd.setToolTip(_translate("ModifyUserUI", "This is the name of user  "))
        self.NumberOfPersonAdd.setToolTip(_translate("ModifyUserUI", "Ther number of the user"))
        self.label_9.setText(_translate("ModifyUserUI", "Number"))
        self.PostCodeAdd.setToolTip(_translate("ModifyUserUI", "This is the post code of user"))
        self.LicenceAdd.setToolTip(_translate("ModifyUserUI", "The licence plate of the user "))
        self.label_10.setText(_translate("ModifyUserUI", "Licence"))
        self.label_7.setText(_translate("ModifyUserUI", "Update or Delete User"))
        self.Back.setToolTip(_translate("ModifyUserUI", "Click to return to home"))
        self.Back.setText(_translate("ModifyUserUI", "Update"))
        self.DeleteUser.setToolTip(_translate("ModifyUserUI", "Click to delete the user"))
        self.DeleteUser.setText(_translate("ModifyUserUI", "Delete"))
        self.UpdateUser.setToolTip(_translate("ModifyUserUI", "Click to update"))
        self.UpdateUser.setText(_translate("ModifyUserUI", "Update"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyUserUI = QtWidgets.QDialog()
    ui = Ui_ModifyUserUI()
    ui.setupUi(ModifyUserUI)
 
    ModifyUserUI.show()
    app.exec_()