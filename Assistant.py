#در اینجا کتابخانه هارو  وارد می کنیم 
from math import trunc
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
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
engine.setProperty('voice', voices[1].id)
engine. setProperty("rate", 170)

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Email address', 'Passwords')
    server.sendmail('Email address' ,to, content)
    server.close()
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
        if 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "example@domain.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Unity buddy. I am not able to send this email") # If you email and password is incorrect.
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
        elif "log off" in query or "sign out" in query or "signout" in query or "logoff" in query:
         speak('Are you sure you want to logout your Windows PC?')
         while True:
           query = takeCommand().lower()
           if 'yes' in query:
               subprocess.call(["shutdown", "/l", "/t", "5"])
               break
           else:
                break
        elif "shutdown" in query or "shut down" in query:
             speak('Are you sure you want to shutdown your Windows PC?')
             while True:
              query = takeCommand().lower()
              if 'yes' in query:
                subprocess.call(["shutdown", "/s", "/t", "5"]) 
                break
              else:
                break
        elif "restart" in query:
             speak('Are you sure you want to restart your windows PC?')
             while True:
              query = takeCommand().lower()
              if 'yes' in query:
               subprocess.call(["shutdown", "/r" , "/t", "5"])
               break
              else:
                
                break       
      
        #17-Roll a die or roll two dice
        elif 'roll dice' in query  or 'roll two die' in query or 'two dice'in query:
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
        elif ('Search'and'youtube') in query:

            driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
            driver.get('https://www.youtube.com/')
            search_box = driver.find_element_by_xpath('//button[@aria-label="Search with your voice"][@class="style-scope yt-icon-button"][@id="button"]')
            search_box.click()
            speak('okay what do you want to search')
            while True:
                msg = driver.find_element_by_xpath('//div[@id="prompt"][@class="style-scope ytd-voice-search-dialog-renderer"]').text
                if msg == 'Listening...':
                    continue
                elif msg == "Didn't hear that. Try again.":
                     mic = driver.find_element_by_xpath('//div[@class="style-scope ytd-voice-search-dialog-renderer"][@id="microphone-circle"][@role="button"]')
                     mic.click()
                     continue
                else:
                    speak('Here is the results')
                    break

        #25-YouTube Video Downloader

        #26-Speed Test
        elif 'net speed' in query or 'speed test' in query or 'test speed' in query or ('internet' and 'speed') in query:
            speak('Testing the speed of your internet connection')
            try:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
                driver.get('https://www.speedtest.net')
                try:
                    GO_btn = driver.find_element_by_xpath('//span[@class="start-text"]')
                    GO_btn.click()
                    time.sleep(2)
                except:
                    pass

                while True:
                    PING  = driver.find_element_by_xpath('//span[@class="result-data-large number result-data-value ping-speed"]').text
                    DOWNLOAD = driver.find_element_by_xpath('//span[@class="result-data-large number result-data-value download-speed"]').text
                    UPLOAD = driver.find_element_by_xpath('//span[@class="result-data-large number result-data-value upload-speed"]').text
                    if PING != ' ' and DOWNLOAD != ' ' and UPLOAD!= ' ':
                        break

                speak('your Ping speed is' + PING)
                speak('your Download  speed is' + DOWNLOAD)
                speak('your  Upload speed is' + UPLOAD)
                driver.close()
            except:
                speak('Something went wrong Please check your internet connection and try again')

        #27-Corona Tracker
        elif ('corona tracker' or 'covid tracker') in query or ('corona statistics' or 'covid statistics') in query:
            try:
                speak('which country')
                country = takeCommand()
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
                if country != 'global':

                 driver.get('https://www.coronatracker.com/country/'+country )

                 if 'Page Not Found' in driver.page_source:
                     speak('Country Not Found Please try again')
                     driver.close()
                     

                 else:
                  time.sleep(3)

                  speak('Confirmed')

                  Confirmed = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-red-600"]').text
                  speak(Confirmed)

                  new_cases = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-xs font-bold text-red-600"]').text
                  speak(new_cases)
 
                  speak('Recovered')

                  Recovered = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-green-600"]').text
                  speak(Recovered)

                  speak('Deaths')

                  Deaths = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-gray-600"]').text
                  speak(Deaths)

                  new_deaths = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-xs font-bold text-gray-600"]').text
                  speak(new_deaths)
                  driver.close()
                else:
                  driver.get('https://www.coronatracker.com/')

                  speak('Confirmed')

                  Confirmed = driver.find_elements_by_xpath('//span[@class="mx-2"]')[0].text
                  speak(Confirmed)
 
                  speak('Recovered')

                  Recovered = driver.find_elements_by_xpath('//span[@class="mx-2"]')[2].text
                  speak(Recovered)

                  speak('Deaths')

                  Deaths =  driver.find_elements_by_xpath('//span[@class="mx-2"]')[4].text
                  speak(Deaths)

                  driver.close()                    
  
            except:
                speak('Something went wrong Please check your internet connection and try again')
        #28-Goodbye