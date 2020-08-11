from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_AddWind(object):

    def __init__(self,address,userDB,passDB,dbname):    #this is getting the DB values to be used in the adding

        self.address = address
        self.userDB = userDB
        self.passDB = passDB
        self.dbname = dbname

    def setUserinterfaces(self,Ui_AddAdmin):

        self.mainuser = Ui_AddAdmin     #this will be used later on to reload the table in the admin screen

    def setupUi(self, AddWind): #this creates the look and feel of the window
        AddWind.setObjectName("AddWind")
        self.mainWin = AddWind
        AddWind.resize(520, 489)
        AddWind.setStyleSheet("background-image: url(NewYork.png);")
        self.centralwidget = QtWidgets.QWidget(AddWind)
        self.centralwidget.setObjectName("centralwidget")
        self.NumberOfPersonAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.NumberOfPersonAdd.setGeometry(QtCore.QRect(150, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumberOfPersonAdd.setFont(font)
        self.NumberOfPersonAdd.setText("")
        self.NumberOfPersonAdd.setObjectName("NumberOfPersonAdd")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.TagID = QtWidgets.QLineEdit(self.centralwidget)
        self.TagID.setGeometry(QtCore.QRect(150, 340, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TagID.setFont(font)
        self.TagID.setText("")
        self.TagID.setObjectName("TagID")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setObjectName("label_10")
        self.NameOfPersonAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.NameOfPersonAdd.setGeometry(QtCore.QRect(150, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameOfPersonAdd.setFont(font)
        self.NameOfPersonAdd.setText("")
        self.NameOfPersonAdd.setObjectName("NameOfPersonAdd")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.PostCodeAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.PostCodeAdd.setGeometry(QtCore.QRect(150, 130, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PostCodeAdd.setFont(font)
        self.PostCodeAdd.setText("")
        self.PostCodeAdd.setObjectName("PostCodeAdd")
        self.LicenceAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.LicenceAdd.setGeometry(QtCore.QRect(150, 270, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LicenceAdd.setFont(font)
        self.LicenceAdd.setText("")
        self.LicenceAdd.setObjectName("LicenceAdd")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 340, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.AddUsers = QtWidgets.QPushButton(self.centralwidget)
        self.AddUsers.setGeometry(QtCore.QRect(230, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddUsers.setFont(font)
        self.AddUsers.setObjectName("AddUsers")
        AddWind.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddWind)
        QtCore.QMetaObject.connectSlotsByName(AddWind)

        self.AddUsers.clicked.connect(self.addthem)		#if user clicks on add button it will preform the add function 

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          #lines 117 - 123 set the parametres for the message box
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def addthem(self):
        
        name = self.NameOfPersonAdd.text()		
        postcode = self.PostCodeAdd.text()		
        number = self.NumberOfPersonAdd.text()		    #lines 127 to 132 create new instance of information entered 
        licence = self.LicenceAdd.text()		
        tagId = self.TagID.text()	
        

        if(len(number) < 11): #check to see if number is less than 11 characters
             self.messagebox("","Please enter correct length for phone number \n and not starting in the format of +44 ")

        elif(len(number) == 11): #if umber is equal to 11 it will continue to next check

            if(name == '' or licence == '' or postcode == '' or tagId == ''): #if fields are left empty then it will not continue.

                self.messagebox("","Please ensure all fields are entered")

            else:

                try:

                    conn = pymysql.connect(host = self.address,		
                                   user = self.userDB,		
                                   passwd = self.passDB ,		
                                   db = self.dbname)		

                    myCursor = conn.cursor()		
                    query =("INSERT INTO userprofile(UserName,PostCode,Number,Licence,TagID) VALUES (%s,%s,%s,%s,%s)")		#SQL to add
                    data = myCursor.execute(query,(name,postcode,number,licence,tagId))		#values to add into DB
                    self.messagebox("","Data Inserted")
                    conn.commit()

                    if self.mainuser != None: #send data back to the table to automatically be updated
                        self.mainuser.loaddata()

                    conn.close()
                    self.NameOfPersonAdd.setText("")
                    self.PostCodeAdd.setText("")
                    self.NumberOfPersonAdd.setText("")          #this will clear all the input fields in the case that the user wants to add more
                    self.LicenceAdd.setText("")
                    self.TagID.setText("")

                except:
                     self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect
    
        else:
            self.messagebox("","Please enter all the fields \n \t    Or \n Make sure values are valid ")


    def retranslateUi(self, AddWind):
        _translate = QtCore.QCoreApplication.translate
        AddWind.setWindowTitle(_translate("AddWind", "Adding Window"))
        self.NumberOfPersonAdd.setToolTip(_translate("AddWind", "Enter here for users phone number"))
        self.label_6.setText(_translate("AddWind", "Name "))
        self.TagID.setToolTip(_translate("AddWind", "Enter the RFID tag ID manually "))
        self.label_10.setText(_translate("AddWind", "Licence"))
        self.NameOfPersonAdd.setToolTip(_translate("AddWind", "Type here to enter name "))
        self.label_8.setText(_translate("AddWind", "Post Code"))
        self.PostCodeAdd.setToolTip(_translate("AddWind", "Enter the post code of user"))
        self.LicenceAdd.setToolTip(_translate("AddWind", "Enter the licence plate of user"))
        self.label_11.setText(_translate("AddWind", "Tag ID"))
        self.label_9.setText(_translate("AddWind", "Number"))
        self.label_7.setText(_translate("AddWind", "Add User"))
        self.AddUsers.setToolTip(_translate("AddWind", "Click to add the user"))
        self.AddUsers.setText(_translate("AddWind", "Add"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddWind = QtWidgets.QMainWindow()
    ui = Ui_AddWind()
    ui.setupUi(AddWind)
    AddWind.show()
    app.exec_()