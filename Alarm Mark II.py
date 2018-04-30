'''
Title: This is an alarm that goes off every 5 minutes
Author: Riley Carpenter
TODO: have the volume get louder when it goes off and quieter afterwards, Make it so that the songs are in a folder and it just scans that folder
'''
from pygame import mixer
import time
import os
import sys
import random
import getpass
import alsaaudio
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#VOLUME CONTROL AREA

#VOLUME CONTROL AREA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hours3 = 5
Minutes3 = 5
endorno = ""
Currenttime = time.ctime()
Hours1 = int(Currenttime[11:13])
Minutes1 = int(Currenttime[14:16])
Seconds = int(Currenttime[17:19])
startinghour = int(Currenttime[11:13])
if startinghour >= 22 or startinghour <= 4:
    timeofday = "Bedtime"
elif startinghour >= 6 and startinghour <= 8:
    timeofday = "Morning"
elif startinghour >= 9 and startinghour <= 11:
    timeofday = "Day"
elif startinghour == 12:
    timeofday = "Noon"
elif startinghour >= 13 and startinghour <= 18:
    timeofday = "Afternoon"
elif startinghour >= 17 and startinghour <= 22:
    timeofday = "Night"
if timeofday == "Bedtime":
    phrases = ["Wake up Riley!!!!","It's time to wake up it's time to wake up","HEEEEYYY WAKE UP","RILEY RILEY RILEY WAKE UP","1 2 3 4 5 6 7 8 9 it is time to wake up","Riley more alarms are to come UNLESS you get up","OH WHEN SHALL I SEE JESUS you wanna not hear this again? Wake up","I'm so tired of telling you to wake up just wake up","A friend of the devil is somehow who doesn't wake up","Babe babe bae wake up"]
elif timeofday == "Morning":
    phrases = ["Your morning alarm is going off!!!!! I suggest you answer it!","This is your slightly later than morning alarm but still in the morning area!!!!","Good morning but like in a different way!!!!","It's time to cancel this alarm as it's going off but not in the way you wanted!!!","HELLLO TIME TO CONTINUE IN YOUR DAY"]
elif timeofday == "Day":
    phrases = ["You are usually at school like what why are you using this?","BEEEP BEEP BEEP is what a normal alarm says but I do not as I'm #NOTNORMAL","Hey user this is a really good alarm clock I wonder if their is a reason for that HMMMMMMMMMMM","OHH it's time for the ALARM GAME the goal of this game is to have your alarm go off, YOU WON!"]
elif timeofday == "Noon":
    phrases = ["You started at noon and you end here, congratulations you bastard","I don't know why I set noon as a time like you probably aren't setting it off at noon.. Unless you are"]
elif timeofday == "Afternoon":
    phrases = ["It's the afternoon!! When you have homemade snacks and nice delicious foods and your alarm goes off","Afternoon time!","ALARM ALARM ALARM IT IS IN THE AFTERNOON","Hey buddy your alarm is going off","Hey!!!! Do the thing!"]
elif timeofday == "Night":
    phrases = ["Goodnight! But like in a different way goodnight!","Hey it's the nighttime! AND your alarm is going off!! SOOO weird!!!!!!"]
optionalsongs = ["Pink Floyd Time.wav","Alarm2.wav","Alarm3.wav","Alarm4.wav","Alarm5.wav","Alarm6.wav","Alarm7.wav","Alarm8.wav","Alarm9.wav","Alarm10.wav","Alarm11.wav"]
if timeofday == "Night":
    soundsorno = input("Hey I saw that this is Night so I wanted to know if you want to play the city sounds? Y/N ")
def playsound(soundfile):
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play(-1)
def alarmsystem(Hours2, Minutes2):
    Currenttime = time.ctime()
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
    if timeofday == "Bedtime":
        playsound("Citys Night ambience sounds.wav")
    elif soundsorno == "Y" or soundsorno == "Yes" or soundsorno == "y" or soundsorno == "yes":
        playsound("Citys Night ambience sounds.wav")
    else:
        playsound("soundthatneedstoplayatthebeginningforaveryspecificreasonthatidontknow-49490711.wav")
    while Hours1 != Hours2 or Minutes1 != Minutes2:
        Currenttime = time.ctime()
        Hours1 = int(Currenttime[11:13])
        Minutes1 = int(Currenttime[14:16])
        Seconds = int(Currenttime[17:19])
        time.sleep(1)
    else:
        mixer.music.stop()
        print(random.choice(phrases))
        playsound(random.choice(optionalsongs))
        endorno = input("Press enter to stop the music and snooze for 5 minutes or type stop ")
        if endorno == "stop":
            if getpass.getuser() == "rileyball2":
                name = ["Riles","Riley Carpenter","Riley Mitchel Carpenter","Rileybug","Rileyball","Rile","Michelle","Riley Michelle Carpenter","Diane","Comrade"]
            else:
                name = [getpass.getuser()]
            if timeofday == "Bedtime":
                print("Good morning",name)
            elif timeofday == "Day":
                print("Goodbye and semi-Good morning",name)
            elif timeofday == "Noon":
                print("Good probably not noon anymore but was noon",name)
            elif timeofday == "Afternoon":
                print("Good afternoon",name)
            elif timeofday == "Night":
                print("Goodbye and semi-good night",name)
            else:
                print("Goodbye",name)
            time.sleep(1)
            sys.exit()
def nexttime():
    Currenttime = time.ctime()
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
    if Minutes1 >= 55:
        print("The alarm will go off at",Hours1 + 1,":",00)
        Hours3 = Hours1 + 1
        Minutes3 = 0
        alarmsystem(Hours3,Minutes3)
    elif Minutes1 == 10:
        print("The alarm will go off at",Hours1,":",15)
        Hours3 = Hours1
        Minutes3 = 15
        alarmsystem(Hours3,Minutes3)
    else:
        Currenttime = time.ctime()
        Hours1 = int(Currenttime[11:13])
        Minutes1 = int(Currenttime[14:16])
        Seconds = int(Currenttime[17:19])
        if Minutes1 >= 50:
            checkminutes = Minutes1 - 50
        elif Minutes1 >= 40:
            checkminutes = Minutes1 - 40
        elif Minutes1 >= 30:
            checkminutes = Minutes1 - 30
        elif Minutes1 >= 20:
            checkminutes = Minutes1 - 20
        elif Minutes1 >= 10:
            checkminutes = Minutes1 - 10
        else:
            checkminutes = Minutes1
        for i in range(0,10):
            if i < 5 and i == checkminutes:
                timetogo = 5 - i
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
            elif i == 5 and i == checkminutes:
                timetogo = 5
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
            elif i > 5 and i == checkminutes:
                timetogo = 10 - i
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
firsthour = int(input("What hour do you want this to start going off? "))
firstminute = int(input("What minute do you want this to start going off? "))
alarmsystem(firsthour,firstminute)
while 1 == 1:
    nexttime()