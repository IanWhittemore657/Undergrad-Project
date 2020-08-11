from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet
import os
from Add import Ui_AddWind
from ModifyAdmin import Ui_ModifyAdminUI
from ModifyUser import Ui_ModifyUserUI
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog

import pymysql

class Ui_AddAdmin(object):
    
    def __init__(self,tabID,addres,userdb,passdb,DBname):

        self.tabs = tabID
        self.address = addres
        self.userDB = userdb             #lines 16 to 20 are getting the detials from the login screen to call on the DB here
        self.passDB = passdb
        self.dbname = DBname


    def setupUi(self, AddAdmin):  #this sets the look and feel of the window
        self.adminscreen = AddAdmin
        AddAdmin.setObjectName("AddAdmin")
        AddAdmin.resize(720, 609)
        self.tabWidget = QtWidgets.QTabWidget(AddAdmin)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStyleSheet("background-color: rgb(3, 218, 197);""")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.LocationAdd = QtWidgets.QLineEdit(self.tab_2)
        self.LocationAdd.setGeometry(QtCore.QRect(220, 150, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LocationAdd.setFont(font)
        self.LocationAdd.setText("")
        self.LocationAdd.setObjectName("LocationAdd")
        self.NumberOfAdminAdd = QtWidgets.QLineEdit(self.tab_2)
        self.NumberOfAdminAdd.setGeometry(QtCore.QRect(220, 220, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumberOfAdminAdd.setFont(font)
        self.NumberOfAdminAdd.setText("")
        self.NumberOfAdminAdd.setObjectName("NumberOfAdminAdd")
        self.NameOfPersonAdd = QtWidgets.QLineEdit(self.tab_2)
        self.NameOfPersonAdd.setGeometry(QtCore.QRect(220, 80, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameOfPersonAdd.setFont(font)
        self.NameOfPersonAdd.setText("")
        self.NameOfPersonAdd.setObjectName("NameOfPersonAdd")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        
        self.label_2.setGeometry(QtCore.QRect(170, 20, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_2.setObjectName("label_2")
        self.AddAdmin_2 = QtWidgets.QPushButton(self.tab_2)
        self.AddAdmin_2.setGeometry(QtCore.QRect(560, 530, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddAdmin_2.setFont(font)
        self.AddAdmin_2.setObjectName("AddAdmin_2")
        self.UsernameAdmin = QtWidgets.QLineEdit(self.tab_2)
        self.UsernameAdmin.setGeometry(QtCore.QRect(220, 290, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UsernameAdmin.setFont(font)
        self.UsernameAdmin.setText("")
        self.UsernameAdmin.setObjectName("UsernameAdmin")
        self.PasswordAdmin = QtWidgets.QLineEdit(self.tab_2)
        self.PasswordAdmin.setGeometry(QtCore.QRect(220, 360, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordAdmin.setFont(font)
        self.PasswordAdmin.setText("")
        self.PasswordAdmin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordAdmin.setObjectName("PasswordAdmin")
        self.Cancelbtn = QtWidgets.QPushButton(self.tab_2)
        self.Cancelbtn.setGeometry(QtCore.QRect(40, 530, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Cancelbtn.setFont(font)
        self.Cancelbtn.setObjectName("Cancelbtn")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(400, 480, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 480, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(100, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(300, 430, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(100, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(100, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(100, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(100, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setObjectName("label_11")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("kisspng-writing-infographic-writer-homework-essay-admin-icon-5b46fc45988424.9295077215313787576247.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.Databasename = QtWidgets.QLineEdit(self.tab_5)
        self.Databasename.setGeometry(QtCore.QRect(320, 120, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Databasename.setFont(font)
        self.Databasename.setText("")
        self.Databasename.setObjectName("Databasename")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(120, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setObjectName("label_12")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(110, 30, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_5.setObjectName("label_5")
        self.Databaseuser = QtWidgets.QLineEdit(self.tab_5)
        self.Databaseuser.setGeometry(QtCore.QRect(320, 210, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Databaseuser.setFont(font)
        self.Databaseuser.setText("")
        self.Databaseuser.setObjectName("Databaseuser")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(120, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(120, 300, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setObjectName("label_14")
        self.databasepassword = QtWidgets.QLineEdit(self.tab_5)
        self.databasepassword.setGeometry(QtCore.QRect(320, 300, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.databasepassword.setFont(font)
        self.databasepassword.setText("")
        self.databasepassword.setObjectName("databasepassword")
        self.databasehost = QtWidgets.QLineEdit(self.tab_5)
        self.databasehost.setGeometry(QtCore.QRect(320, 390, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.databasehost.setFont(font)
        self.databasehost.setText("")
        self.databasehost.setObjectName("databasehost")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(120, 390, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setObjectName("label_15")
        self.saveDBtext = QtWidgets.QPushButton(self.tab_5)
        self.saveDBtext.setGeometry(QtCore.QRect(370, 480, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveDBtext.setFont(font)
        self.saveDBtext.setObjectName("SaveDBtext")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("kisspng-oracle-database-computer-icons-logo-encapsulated-p-storage-5ac32ed8635aa6.116548351522740952407.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon1, "")
       
       
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.AdminWidgetTable = QtWidgets.QTableWidget(self.tab_4)
        self.AdminWidgetTable.setGeometry(QtCore.QRect(30, 60, 501, 421))
        self.AdminWidgetTable.setToolTip("")
        self.AdminWidgetTable.setRowCount(0)
        self.AdminWidgetTable.setColumnCount(5)
        self.AdminWidgetTable.setObjectName("AdminWidgetTable")
        item = QtWidgets.QTableWidgetItem()
        self.AdminWidgetTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AdminWidgetTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AdminWidgetTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AdminWidgetTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.AdminWidgetTable.setHorizontalHeaderItem(4, item)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_3.setObjectName("label_3")

        self.LoadUser_3 = QtWidgets.QPushButton(self.tab_4)
        self.LoadUser_3.setGeometry(QtCore.QRect(220, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoadUser_3.setFont(font)
        self.LoadUser_3.setObjectName("LoadUser_3")
        self.StatusAdmin = QtWidgets.QLabel(self.tab_4)
        self.StatusAdmin.setGeometry(QtCore.QRect(210, 490, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StatusAdmin.setFont(font)
        self.StatusAdmin.setObjectName("StatusAdmin")
        self.ModiAmin = QtWidgets.QPushButton(self.tab_4)
        self.ModiAmin.setGeometry(QtCore.QRect(580, 230, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ModiAmin.setFont(font)
        self.ModiAmin.setAcceptDrops(False) 

        

        self.ModiAmin.setObjectName("ModiAmin")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("kisspng-gear-logo-computer-icons-setting-5b132e8306d092.0958083315279837470279.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        self.tabWidget.addTab(self.tab_4, icon2, "") 
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ModifyUser = QtWidgets.QPushButton(self.tab_3)
        self.ModifyUser.setGeometry(QtCore.QRect(570, 280, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ModifyUser.setFont(font)
        self.ModifyUser.setObjectName("ModifyUser")
        self.UserWidgetTable = QtWidgets.QTableWidget(self.tab_3)
        self.UserWidgetTable.setGeometry(QtCore.QRect(10, 40, 501, 451))
        self.UserWidgetTable.setRowCount(0)
        self.UserWidgetTable.setColumnCount(5)
        self.UserWidgetTable.setObjectName("UserWidgetTable")
        item = QtWidgets.QTableWidgetItem()
        self.UserWidgetTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserWidgetTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserWidgetTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserWidgetTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserWidgetTable.setHorizontalHeaderItem(4, item)
        self.AddUser = QtWidgets.QPushButton(self.tab_3)
        self.AddUser.setGeometry(QtCore.QRect(570, 190, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddUser.setFont(font)
        self.AddUser.setObjectName("AddUser")
        self.LoadUser = QtWidgets.QPushButton(self.tab_3)
        self.LoadUser.setGeometry(QtCore.QRect(210, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoadUser.setFont(font)
        self.LoadUser.setObjectName("LoadUser")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(60, 0, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_4.setObjectName("label_4")
        self.StatusPeople = QtWidgets.QLabel(self.tab_3)
        self.StatusPeople.setGeometry(QtCore.QRect(200, 500, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StatusPeople.setFont(font)
        self.StatusPeople.setObjectName("StatusPeople")
        icon3 = QtGui.QIcon() 
        icon3.addPixmap(QtGui.QPixmap("kisspng-silhouette-user-person-5af561e0d05e80.6195115515260308168535.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(130, 40, 481, 31))
        self.label.setObjectName("label")

        self.EnterSearch = QtWidgets.QLineEdit(self.tab)
        self.EnterSearch.setGeometry(QtCore.QRect(240, 100, 231, 31))
        font.setPointSize(14)
        self.EnterSearch.setFont(font)
        self.EnterSearch.setText("")
        self.EnterSearch.setObjectName("EnterSearch")
        font = QtGui.QFont()


        self.ListOfCars = QtWidgets.QTableWidget(self.tab)
        self.ListOfCars.setToolTip("")
        self.ListOfCars.setGeometry(QtCore.QRect(100, 220, 521, 241))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.ListOfCars.setFont(font)
        self.ListOfCars.setRowCount(7)
        self.ListOfCars.setObjectName("ListOfCars")
        self.ListOfCars.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListOfCars.setItem(0, 4, item)

        self.Load_Times = QtWidgets.QPushButton(self.tab)

        self.Load_Times.setGeometry(QtCore.QRect(310, 530, 111, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.Load_Times.setFont(font)
        self.Load_Times.setObjectName("Load_Times")
        self.StatusCars = QtWidgets.QLabel(self.tab)

        self.StatusCars.setGeometry(QtCore.QRect(300, 490, 131, 21))

        self.LocationAdd.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.NumberOfAdminAdd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AddAdmin_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UsernameAdmin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NameOfPersonAdd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cancelbtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordAdmin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Databasename.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Databaseuser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.databasepassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.databasehost.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.saveDBtext.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-color: rgb(0, 0, 0);")
        self.AdminWidgetTable.setStyleSheet("background-color: rgb(255, 255, 255);\n""\n""border-color: rgb(0, 0, 0);")
        self.LoadUser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ModiAmin.setStyleSheet("background-color: rgb(255, 255, 255);")
       
        self.ModifyUser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UserWidgetTable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AddUser.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.EnterSearch.setStyleSheet("background-color: rgb(255, 255, 255);")
     
        
    
        self.LoadUser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ListOfCars.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Load_Times.setStyleSheet("background-color: rgb(255, 255, 255);")
     

        font = QtGui.QFont()
        font.setPointSize(12)
        self.StatusCars.setFont(font)
        self.StatusCars.setObjectName("StatusCars")


        self.Searchbtn = QtWidgets.QPushButton(self.tab)
        self.Searchbtn.setGeometry(QtCore.QRect(310, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Searchbtn.setFont(font)
        self.Searchbtn.setObjectName("Searchbtn")

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon4, "")

        self.retranslateUi(AddAdmin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddAdmin)

        self.LoadUser.clicked.connect(self.loaddata)        #this will load the table function for user data when clicked
        self.Load_Times.clicked.connect(self.LoadTimeData)      #this will load the table function for times when clicked

        self.Cancelbtn.clicked.connect(self.clearadmin) #this button will clear inputs once clicked for adding admin
     
        self.LoadUser_3.clicked.connect(self.loadAdmin) #this button will load the table for the admin once clicked

        self.AddAdmin_2.clicked.connect(self.addadmins) #this button will run the addadmins function which will add admin

        self.AddUser.clicked.connect(self.openAddWindow)    #when this is clicked it will open the window to add users

        self.Searchbtn.clicked.connect(self.searching)  #clicking this button will allow for users to search for items in the time table

        self.UserWidgetTable.clicked.connect(self.on_click)

        self.AdminWidgetTable.clicked.connect(self.on_click_admin)      #lines 459 and 461 are used to get the user that the admin clicks on which will be stored to be sent to the modify windows.
         
        self.ModiAmin.clicked.connect(self.modifyAdmins)    #this will load the modifyadmin function once clicked

        self.ModifyUser.clicked.connect(self.modifyUsers)    #this will load the modify user function once clicked
    
        self.saveDBtext.clicked.connect(self.save_text)  #this will load the save_text function once clicked

        self.setDataFields() #this will set the fields in regards to the databse
    
        if(self.tabs == 1):
            self.hidetabs() #if a normal admin logs in then the hide functions will be called

    def keyPressEvents(self, event):
        if event.key() == QtCore.Qt.Key_Escape:     #this means that when the escape button is pressed it will close the main screen
            self.adminscreen.close()
 
    
    def setDataFields(self):
        self.Databasename.setText(self.dbname)
        self.databasepassword.setText(self.passDB)      #this sets the variables for the database fields to be eitehr updated or changed
        self.Databaseuser.setText(self.userDB);
        self.databasehost.setText(self.address);

    def hidetabs(self):     #this function will remove tabs if a normal admin logins

        self.tabWidget.removeTab(0)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(2)

    def save_text(self):        #this function will save the database settings into a file
        dataname = self.Databasename.text();
        datauser = self.Databaseuser.text();
        datapassword = self.databasepassword.text();        
        dataIP = self.databasehost.text();
  
        if(len(dataname) == 0 or len(datauser) == 0 or len(datapassword) == 0 or len(dataIP) == 0):     #this check is to ensure no field is left empty
            self.messagebox("Error","Please fill out all fields");
        else:
            try:
                filename = QFileDialog.getSaveFileName(None,'Save File', '','*.txt') 
                if filename[0].find('.txt') == -1:
                    filename[0] = filename[0] + '.txt'
                with open(filename[0],'w') as f:
                    f.write(dataname)
                    f.write("\n")
                    f.write(datauser)                                       #line 501 - 511 will store the infomration into a text file and only work with the extension of .txt
                    f.write("\n")
                    f.write(datapassword)
                    f.write("\n")
                    f.write(dataIP)
            except Exception as e:
                print(e)

    def on_click_admin(self):
        print("\n")
        print(self.AdminWidgetTable.selectedItems()[0].row(), self.AdminWidgetTable.selectedItems()[0].column(), self.AdminWidgetTable.selectedItems()[0].text())
        colIndx = 0 #this sets the colunmn to zero so that it alreadys gets from this column
        rowIndx = self.AdminWidgetTable.selectedItems()[0].row()    #this will get the ID from the row that has been selected
        
        self.adminID = self.AdminWidgetTable.item(rowIndx, colIndx).text() #this saves the id in a new variable 
                
    def modifyAdmins(self):

        self.modAdmin = QtWidgets.QMainWindow()
        try:                                    #try statement used to make sure a field has been selected
            self.adminIDmodi = self.adminID
            self.addres = self.address
            self.userdb = self.userDB
            self.passdb = self.passDB               #line 527 - 534  will send the details to the modify admin window and open the window
            self.DBname = self.dbname
            self.ui = Ui_ModifyAdminUI(self.adminIDmodi,self.addres,self.userdb,self.passdb,self.DBname)
            self.ui.setAdminUserInterfaces(self)
            self.ui.setupUi(self.modAdmin)
            self.modAdmin.show()
        except:
            self.messagebox("Error","Please either load the table and click on user or ensure a user has been selected")

    def modifyUsers(self):

        self.modUser = QtWidgets.QMainWindow()
      
        try: #try statement used to make sure a field has been selected

            self.normaluserID = self.peopleid;
            self.ui = Ui_ModifyUserUI(self.normaluserID,self.address,self.userDB,self.passDB,self.dbname)       #line 545 - 549 will send the details to modify user screen and open the window
            self.ui.setupUi(self.modUser)
            self.ui.setAdminUserInterface(self)
            self.modUser.show()

        except:

            self.messagebox("Error","Please either load the table and click on user or ensure a user has been selected")


    def clearadmin(self):               #this function is when the cancel button in the first tab is clicked and will reset all the fields to clear
        self.NameOfPersonAdd.setText("");
        self.LocationAdd.setText("");
        self.NumberOfAdminAdd.setText("");
        self.UsernameAdmin.setText("");
        self.PasswordAdmin.setText("");
        self.radioButton_2.setChecked(False);
        self.radioButton.setChecked(False);

    
    def searching(self):        #this is the search function to be used in the times tab

        while (self.ListOfCars.rowCount() > 0):     #if data has already been loaded then line 569 will remove data to allow correct searching
               self.ListOfCars.removeRow(0)
        searchingVal = self.EnterSearch.text()
        self.StatusCars.setText("        Loaded")
       
        try:
            conn = pymysql.connect(host = self.address,
                                       user = self.userDB,
                                       passwd = self.passDB ,
                                       db = self.dbname)	

            myCursor = conn.cursor()

            query =("SELECT * FROM timeprofiles WHERE Licence LIKE '%" + searchingVal  + "%'  OR Owner LIKE '%" + searchingVal + "%' OR Date LIKE '%" + searchingVal + "%' OR Time LIKE '%" + searchingVal + "%' OR Status LIKE '%"+searchingVal+"%'" )   #this sql will be used to get the values that are being searched for

            data = myCursor.execute(query)

            if(data > 0): #if there is a field that exists with this data then it will run
                myresult = myCursor.fetchall()
        
                for row_number,row_data in enumerate(myresult):

                    self.ListOfCars.insertRow(row_number)

                    for column_number , data in enumerate(row_data):

                        self.ListOfCars.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data))) #this will add all the data found in the search back into

               
                self.StatusCars.setText("      Loaded")
                      
            else:
                self.messagebox("Error","No field exists");
            conn.close()
        except:
            self.messagebox("Error","There is a problem connecting to the Database");

    def on_click(self): #this is the similar function used in on_click_Admin 

        colIndx = 0
        rowIndx = self.UserWidgetTable.selectedItems()[0].row() 
        
        self.peopleid = self.UserWidgetTable.item(rowIndx, colIndx).text()
       


    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)       #this sets the pararemters for the message box
        mess.exec_()   


    def addadmins(self):    #this is to add admin into the system and DB

        name = self.NameOfPersonAdd.text()
        location = self.LocationAdd.text()
        
        
        try: #to ensure number is in correct format

            number = self.NumberOfAdminAdd.text()
                
            if(int(number) < 0): #check is characters of number are greater than 0 
                self.messagebox("","Please ensure number is a positive")
                
                
            elif(len(number) < 11 ): #ensure number is greater than 11 characters

                self.messagebox("","Please enter correct length for phone number \n and not starting in the format of +44 ")

            elif(len(number) == 11): #check if characters are equal to 11

                if(self.radioButton.isChecked()):   #this will check which radio button is clicked 
                        field = self.radioButton.text(); #this sets the field to superadmin
                        

                elif(self.radioButton_2.isChecked): #this will check which radio button is clicked

                        field = self.radioButton_2.text() #this will set the field to normal admin
                        

                if(name == '' or location == ''):   #this will check if the name or location has been entered

                    self.messagebox("","Please ensure all fields are entered")
                else:

                    username = self.UsernameAdmin.text()
                    
                   
                    file = open('key.key','rb')
                    key = file.read()
                    file.close()
                    
                    password = self.PasswordAdmin.text()    
                    encoded = password.encode() #this will encode the password into the DB
                    f = Fernet(key)
                    encrypted = f.encrypt(encoded) #this is the encrpyted form of the password

                    conn = pymysql.connect(host = self.address,
                                            user = self.userDB,
                                            passwd = self.passDB ,
                                            db = self.dbname)	
                    myCursor = conn.cursor()

                    query =("INSERT INTO adminusers(AdminName,Location,Number,Field,Username,Password) VALUES (%s,%s,%s,%s,%s,%s)") #SQL to add it to the database
        
                    data = myCursor.execute(query,(name,location,number,field,username,encrypted))

                    print("> Data Inserted ")
                    

                    self.NameOfPersonAdd.setText("")
                    self.LocationAdd.setText("")
                    self.NumberOfAdminAdd.setText("")           #line 683 - 687 this will set the fields all to zero 
                    self.UsernameAdmin.setText("")
                    self.PasswordAdmin.setText("")

                    conn.commit()
                    self.loadAdmin() #this will update the admin table 
                    conn.close()

                
                

        except ValueError:
            self.messagebox("","Number is not in the correct format")

           
    def loadAdmin(self):
  

        while (self.AdminWidgetTable.rowCount() > 0):
                self.AdminWidgetTable.removeRow(0)      #if there is data it will remove the data to be reloaded
        conn = pymysql.connect(host = self.address,
                                   user = self.userDB,
                                   passwd = self.passDB ,
                                   db = self.dbname)	
        myCursor = conn.cursor()
        query =("SELECT AdminID,AdminName,Location,Number,Field FROM adminusers")
        myCursor.execute(query)
        myresult = myCursor.fetchall()
       
       #clear contant 
        for row_number,row_data in enumerate(myresult):
            self.AdminWidgetTable.insertRow(row_number)
            for column_number , data in enumerate(row_data):
                self.AdminWidgetTable.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))  #this will reload the data into the table 

        
        self.StatusAdmin.setText("       Loaded")
        self.LoadUser_3.setText("Re-Load")
       
        conn.close()

    def openAddWindow(self):

        self.addres = self.address
        self.userdb = self.userDB
        self.passdb = self.passDB
        self.DBname = self.dbname


        self.addWin = QtWidgets.QMainWindow()
        self.ui = Ui_AddWind(self.addres,self.userdb,self.passdb,self.DBname) #this will send the data to the add window
        self.ui.setUserinterfaces(self)
        self.ui.setupUi(self.addWin)
        self.addWin.show()
    
    def loaddata(self): #this function is similar to all the other previous load table functions

        while (self.UserWidgetTable.rowCount() > 0):
                self.UserWidgetTable.removeRow(0)
        
        conn = pymysql.connect(host = self.address,
                                   user = self.userDB,
                                   passwd = self.passDB ,
                                   db = self.dbname)	
        myCursor = conn.cursor()
        query =("SELECT * FROM userprofile")
        myCursor.execute(query)
        myresult = myCursor.fetchall()
    
        for row_number,row_data in enumerate(myresult):
            self.UserWidgetTable.insertRow(row_number)
            for column_number , data in enumerate(row_data):
                self.UserWidgetTable.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        

        self.StatusPeople.setText("       Loaded")
        self.LoadUser.setText("Re-Load")
        conn.close()

    def LoadTimeData(self): #this function is similar to all the other previous load table functions

        while (self.ListOfCars.rowCount() > 0):
                self.ListOfCars.removeRow(0)
        conn = pymysql.connect(host = self.address,
                                   user = self.userDB,
                                   passwd = self.passDB ,
                                   db = self.dbname)	
        myCursor = conn.cursor()
        query =("SELECT * FROM timeprofiles")
        myCursor.execute(query)
        myresult = myCursor.fetchall()
    
        for row_number,row_data in enumerate(myresult):
            self.ListOfCars.insertRow(row_number)
            for column_number , data in enumerate(row_data):
                self.ListOfCars.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
                
        
        self.StatusCars.setText("        Loaded")
        self.Load_Times.setText("Re-Load")

        
        conn.close()




    def retranslateUi(self, AddAdmin):
        _translate = QtCore.QCoreApplication.translate
        
        AddAdmin.setWindowTitle(_translate("AddAdmin", "Admin Screen"))
        
        self.LocationAdd.setToolTip(_translate("AddAdmin", "Enter the location of admin"))
        self.NumberOfAdminAdd.setToolTip(_translate("AddAdmin", "Enter here for admins phone number"))
        self.NameOfPersonAdd.setToolTip(_translate("AddAdmin", "Type here to enter a name "))
        self.label_2.setText(_translate("AddAdmin", "Please enter the details of a new admin"))
        self.AddAdmin_2.setToolTip(_translate("AddAdmin", "Click to add admin "))
        self.AddAdmin_2.setText(_translate("AddAdmin", "Add"))
        self.UsernameAdmin.setToolTip(_translate("AddAdmin", "Enter here the username for the admin"))
        self.PasswordAdmin.setToolTip(_translate("AddAdmin", "Enter here the password for the admin"))
        self.Cancelbtn.setToolTip(_translate("AddAdmin", "Cancel inputs"))
        self.Cancelbtn.setText(_translate("AddAdmin", "Cancel"))
        self.radioButton.setToolTip(_translate("AddAdmin", "Select as a super-admin"))
        self.radioButton.setText(_translate("AddAdmin", "Super-Admin"))
        self.radioButton_2.setText(_translate("AddAdmin", "Normal Admin"))
        self.radioButton_2.setToolTip(_translate("AddAdmin", "Select as a normal admin"))
        self.label_6.setText(_translate("AddAdmin", "Name "))
        self.label_7.setText(_translate("AddAdmin", "Type of Admin"))
        self.label_8.setText(_translate("AddAdmin", "Location"))
        self.label_9.setText(_translate("AddAdmin", "Number"))
        self.label_10.setText(_translate("AddAdmin", "Username "))
        self.label_11.setText(_translate("AddAdmin", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AddAdmin", "Admin"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("AddAdmin", "Tools to add admins"))
        
        self.Databasename.setToolTip(_translate("AddAdmin", "Enter the database name"))
        self.label_12.setText(_translate("AddAdmin", "Database name"))
        self.label_5.setText(_translate("AddAdmin", "Please enter the details of the database specifications"))
        self.Databaseuser.setToolTip(_translate("AddAdmin", "Enter database user name"))
        self.label_13.setText(_translate("AddAdmin", "Database user"))
        self.label_14.setText(_translate("AddAdmin", "Database password"))
        self.databasepassword.setToolTip(_translate("AddAdmin", "Enter the database password"))
        self.databasehost.setToolTip(_translate("AddAdmin", "Enter host IP"))
        self.label_15.setText(_translate("AddAdmin", "Database host IP"))
        self.saveDBtext.setToolTip(_translate("AddAdmin", "Click to save database"))
        self.saveDBtext.setText(_translate("AddAdmin", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("AddAdmin", "Database Settings"))
        item = self.AdminWidgetTable.horizontalHeaderItem(0)
        item.setText(_translate("AddAdmin", "ID"))
        item = self.AdminWidgetTable.horizontalHeaderItem(1)
        item.setText(_translate("AddAdmin", "Name"))
        item = self.AdminWidgetTable.horizontalHeaderItem(2)
        item.setText(_translate("AddAdmin", "Location"))
        item = self.AdminWidgetTable.horizontalHeaderItem(3)
        item.setText(_translate("AddAdmin", "Number"))
        item = self.AdminWidgetTable.horizontalHeaderItem(4)
        item.setText(_translate("AddAdmin", "Field"))
        self.label_3.setText(_translate("AddAdmin", "Select an admin and click on item to update"))
        self.LoadUser_3.setToolTip(_translate("AddAdmin", "Loads information to table"))
        self.LoadUser_3.setText(_translate("AddAdmin", "Load"))
        self.StatusAdmin.setText(_translate("AddAdmin", "       Status"))
        self.ModiAmin.setToolTip(_translate("AddAdmin", "Takes to modify page"))
        self.ModiAmin.setText(_translate("AddAdmin", "Modify"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("AddAdmin", "Modify"))
        self.ModifyUser.setToolTip(_translate("AddAdmin", "Click to modify exsiting user information"))
        self.ModifyUser.setText(_translate("AddAdmin", "Modify"))
        item = self.UserWidgetTable.horizontalHeaderItem(0)
        item.setText(_translate("AddAdmin", "ID"))
        item = self.UserWidgetTable.horizontalHeaderItem(1)
        item.setText(_translate("AddAdmin", "Name"))
        item = self.UserWidgetTable.horizontalHeaderItem(2)
        item.setText(_translate("AddAdmin", "Post code"))
        item = self.UserWidgetTable.horizontalHeaderItem(3)
        item.setText(_translate("AddAdmin", "Number"))
        item = self.UserWidgetTable.horizontalHeaderItem(4)
        item.setText(_translate("AddAdmin", "Licence"))
        
       
      
        self.AddUser.setToolTip(_translate("AddAdmin", "Takes to adding page"))
        self.AddUser.setText(_translate("AddAdmin", "Add"))
        self.LoadUser.setToolTip(_translate("AddAdmin", "Loads information to table"))
        self.LoadUser.setText(_translate("AddAdmin", "Load"))
        self.label_4.setText(_translate("AddAdmin", "Select a user and click on item to update"))
        self.StatusPeople.setText(_translate("AddAdmin", "       Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("AddAdmin", "People"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_3), _translate("AddAdmin", "Click to add People"))
       
        self.label.setText(_translate("AddAdmin", "<html><head/><body><p><span style=\" font-size:18pt;\">Please search via the column headers below</span></p></body></html>"))
        self.EnterSearch.setToolTip(_translate("AddAdmin", "Enter information here"))
       
        item = self.ListOfCars.horizontalHeaderItem(0)
        item.setText(_translate("AddAdmin", "Owner"))
        item = self.ListOfCars.horizontalHeaderItem(1)
        item.setText(_translate("AddAdmin", "Date"))
        item = self.ListOfCars.horizontalHeaderItem(2)
        item.setText(_translate("AddAdmin", "Time"))
        item = self.ListOfCars.horizontalHeaderItem(3)
        item.setText(_translate("AddAdmin", "Status"))
        item = self.ListOfCars.horizontalHeaderItem(4)
        item.setText(_translate("AddAdmin", "Licence"))
        __sortingEnabled = self.ListOfCars.isSortingEnabled()
        
       
       
        self.ListOfCars.setSortingEnabled(False)
        self.ListOfCars.setSortingEnabled(__sortingEnabled)
       
        self.Load_Times.setToolTip(_translate("AddAdmin", "Loads the information table"))
        self.Load_Times.setText(_translate("AddAdmin", "Load"))
        self.StatusCars.setText(_translate("AddAdmin", "         Status"))
        self.Searchbtn.setText(_translate("AddAdmin", "Search "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AddAdmin", "Times"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("AddAdmin", "Click to see times"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddAdmin = QtWidgets.QDialog()
    ui = Ui_AddAdmin()
    ui.setupUi(AddAdmin)
    AddAdmin.show()
    app.exec_()