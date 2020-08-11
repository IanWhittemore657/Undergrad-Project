#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

import time, sys

import pymysql

import datetime

continue_reading = True #will keep looping for tags

redPin = 11   #Set to appropriate GPIO
greenPin = 12 
bluePin = 13  

dbaddress = raw_input("Database settings-->")


GPIO.setwarnings(False)


def blink(pin):     #this will set the LED to turn on and operate 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):   #this will turn off the LED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def redOn():
    turnOff(redPin)
	
def redOff():
    blink(redPin)

def greenOn():
    turnOff(greenPin)

def greenOff():
	blink(greenPin)
    
def blueOn():
    turnOff(bluePin)

def blueOff():
	blink(bluePin)


# Capture code for cleanup when the program is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending RFID."
    continue_reading = False
    GPIO.cleanup()

# gather the signals
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522 to call libary
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to Disabled Parking Management example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        
        cardID = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        
        print "Card read UID: "+ cardID
        
 
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        conn = pymysql.connect(host = dbaddress,user = "RFID",passwd = "1234",db = "disableddatabase")  #create connection for to the DB
         
        myCursor = conn.cursor()
        
        try:#try see if connection can occur otherwise print error
            Query = ("SELECT * FROM userprofile WHERE TagID = %s")
                
            data = myCursor.execute(Query,(cardID))
            myresult = myCursor.fetchall()
            
            name = '';
            licence = '';
            tagID = '';
                
            for x in myresult:
                name = x[1];
                licence = x[4];
                tagID = x[5];
            print(name + " " + licence + " " + tagID)#get the detials from the DB
        except:
            print("Error")            
        
        
      # need to do a check to ensure tag id in DB matches 
        if(cardID == tagID):
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
            
            redOff() #red LED switches off
            greenOn() #green LED switches on for authorisation
            
            currentDT = datetime.datetime.now()
    
            authorised = "Authorised"     
            
            year = currentDT.year
            month = currentDT.month     #line 134 - 137 gets the time that will be stored in the DB
            day = currentDT.day
            
            if(month < 10):
                month = "0" + str(month) #this will see if the month is less than 10 then it will add a 0 infront 
                
            if(day < 10):
                day = "0" +str(day) #so too will this check see if day is less than 10 and add a 0 infront
            
            yymmdd = str(year) + "-" + str(month) + "-" + str(day) #this add all date details together
            
            print(yymmdd)
            
            hour = currentDT.hour
            minute = currentDT.minute
            
            
            if(hour < 10):
                hour = "0" + str(hour)#this will see if the hor is less than 10 then it will add a 0 infront 
            if(minute < 10):
                minute = "0" + str(minute)#this will see if the minute is less than 10 then it will add a 0 infront 
                
            hhmm =str(hour) + ":" + str(minute)   #this will add all time together 
            print(hhmm) 

            conn = pymysql.connect(host = dbaddress,user = "RFID",passwd = "1234",db = "disableddatabase")
         
            myCursor = conn.cursor()
            
            Query = ("INSERT INTO timeprofiles(Owner,Date,Time,Status,Licence) VALUES (%s,%s,%s,%s,%s)") #this is the sql query to add into the DB
            
            
            data = myCursor.execute(Query,(name,yymmdd,hhmm,authorised,licence)) #this will run the query
            print("data inserted")
            myresult = myCursor.fetchall()

            conn.commit()
            conn.close()
            

        # Check if authenticated
            if status == MIFAREReader.MI_OK: #this will turn the green LED on
                MIFAREReader.MFRC522_Read(8)
                MIFAREReader.MFRC522_StopCrypto1()
                redOff()
                greenOn()
                time.sleep(5) #5 seconds after and will turn LED off
                redOff()
                greenOff()
                blueOff()
                
            else: #this will turn the Red light for authentication failure
                print "Authentication error"
                authorised = "Not Authorised"
                greenOff()
                redOn()
                time.sleep(5) #5 seconds after and will turn LED off
                redOff()
                greenOff()
                blueOff()

        else:#this will turn the Red light for authentication failure
            print "Authentication error"
            authorised = "Not Authorised"
            greenOff()
            redOn()
            time.sleep(5) #5 seconds after and will turn LED off
            redOff()
            greenOff()
            blueOff()
