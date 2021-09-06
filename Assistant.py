#در اینجا کتابخانه هارو  وارد می کنیم 
from math import trunc
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess
#---------------------------------------
#ست پروپرتی: setProperty
# پایتسک3: pyttsx3
#سپی5 : sapi5
#گت پروپرتی : getProperty
#------------------------------------------

#engine :  در حین ساخت موتور مقدار اولیه  (پایتسک3)را فعال میکند تولید و توقف گفتار دریافت و تنظیم ویژگی های موتور گفتار و شروع و توقف حلقه های رویداد
#13: یک برنامه (پایتتسک3) را فراخوانی میکند و کار اصلیش تبدیل که متن وارد شده را به گفتار تبدیل میکند و ماژول (پایتتسک3) دو صدا پشتیبانی میکند که اول زن است و دیگری نر است که توسط (سپی5) برای ویندوز هستش)
engine = pyttsx3.init('sapi5')
# گت پروپرتی مقدار فعلی یک ویژگی موتور را بدست می اورد  اما ست پروپرتی دستور را برای تنظیم ویژگی موتور قرار میدهد و متن گفته شده به استرینگ است 
voices = engine.getProperty('voices')
# print(voices[1].id)
#گت پروپرتی مقدار فعلی یک ویژگی موتور را بدست می اورد  اما ست پروپرتی دستور را برای تنظیم ویژگی موتور قرار میدهد و متن گفته شده به استرینگ است
engine.setProperty('voice', voices[0].id)

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")
#driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #===================================================
 
        #1-Set an alarm

        #2-Sending emails

        #3-Sending Whatsapp massage

        #4-Weather

        #5-Math

        #6-Time zone conversions

        #7-Definitions, synonyms, antonyms, or etymologies of words

        #8-Site searches
        
        #9-Open app

        #10-Play music from system

        #11-Play music from soundcloud

        #12-Identify songs

        #13-Take a picture

        #14-What time is it

        #15-Read news

        #16-Shutdown	
        if "log off" in query or "sign out" in query:
         speak('Are you sure you want to logout your Windows PC?')
         while True:
           query = takeCommand().lower()
           if 'yes' in query:
               subprocess.call(["shutdown", "/l", "/t", "5"])
               break
           else:
                break
        if "Shutdown" in query or "Shut down" in query:
             speak('Are you sure you want to shutdown your Windows PC?')
             while True:
              query = takeCommand().lower()
              if 'yes' in query:
                subprocess.call(["shutdown", "/s", "/t", "5"]) 
                break
              else:
                break
        if "log off" in query or "sign out" in query:
             speak('Are you sure you want to restart your windows PC ?')
             while True:
              query = takeCommand().lower()
              if 'yes' in query:
               subprocess.call(["shutdown", "/r" , "/t", "5"])
               break
              else:
                
                break

         
        #17-Roll a die or roll two dice

        if 'roll dice' in query  or 'roll two die' in query or 'two dice'in query:
           dice1 =  random.choice(['One','Two','Three','Four','Five','Six'])
           dice2 =  random.choice(['One','Two','Three','Four','Five','Six'])
           say = random.choice([('its' + dice1 + 'and,' + dice2) , (dice1 + 'and,' + dice2) ,('its'+ dice1 + 'and,' + dice2 + 'this time') , ('ok...'+ dice1 + 'and,' + dice2)])
           speak('Rolling...,')
           time.sleep(1)
           speak(say)

        elif 'roll a dice' in query  or 'roll a die' in query or 'roll die' in query or 'dice' in query:
           dice =  random.choice(['One','Two','Three','Four','Five','Six'])
           say = random.choice(['its'+ dice,dice,'its'+ dice + 'this time','ok...'+dice])
           speak('Rolling...,')
           time.sleep(1)
           speak(say)
        
        #18-Flip a coin

        elif 'flip a coin' in query or 'coin' in query or 'flip coin' in query:
           coin =  random.choice(['Tails','Heads'])
           say = random.choice(['its'+ coin,coin,'its'+ coin + 'this time'])
           speak(say)
        
        #19-What is your favorite color

        #20-Tell me a joke

        #21-Learn how to say my name

        #22-repeat after me

        #23-Reminder

        #24-YouTube Search

        #25-YouTube Video Downloader

        #26-Speed Test

        #27-Corona Tracker

        #28-Goodbye