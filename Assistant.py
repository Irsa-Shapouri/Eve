#در اینجا کتابخانه هارو  وارد می کنیم 
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

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
        if '' in query:
            print('')

        #2-Sending emails
        elif '' in query:
            print('')

        #3-Sending Whatsapp massage
        elif '' in query:
            print('')

        #4-Weather
        elif '' in query:
            print('')

        #5-Math
        elif '' in query:
            print('')

        #6-Time zone conversions
        elif '' in query:
            print('')


        #7-Definitions, synonyms, antonyms, or etymologies of words
        elif '' in query:
            print('')

        #8-Site searches
        elif '' in query:
            print('')

        #9-Open app
        elif '' in query:
            print('')

        #10-Play music from system
        elif '' in query:
            print('')

        #11-Play music from soundcloud
        elif '' in query:
            print('')

        #12-Identify songs
        elif '' in query:
            print('')

        #13-Take a picture
        elif '' in query:
            print('')

        #14-What time is it
        elif '' in query:
            print('')

        #15-Read news
        elif '' in query:
            print('')

        #16-Shutdown
        elif '' in query:
            print('')

        #17-Roll a die or roll two dice
        elif '' in query:
            print('')

        #18-Flip a coin
        elif '' in query:
            print('')

        #19-What is your favorite color
        elif '' in query:
            print('')

        #20-Tell me a joke
        elif '' in query:
            print('')

        #21-Learn how to say my name
        elif '' in query:
            print('')

        #22-repeat after me
        elif '' in query:
            print('')

        #23-Reminder
        elif '' in query:
            print('')

        #24-YouTube Search
        elif '' in query:
            print('')


        #25-YouTube Video Downloader
        elif '' in query:
            print('')

        #26-Speed Test
        elif '' in query:
            print('')

        #27-Corona Tracker
        elif '' in query:
            print('')

        #28-Goodbye
        elif '' in query:
            print('')