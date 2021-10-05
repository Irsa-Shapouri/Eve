#####################
# IMPORTING MODULES #
##################### 

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from difflib import get_close_matches
import speech_recognition as sr
from playsound import playsound
from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
from random import choice
import pyautogui as pg
from tkinter import *
import webbrowser
import datetime
import requests
import random
import time
import json
import cv2
import os



#data directory
cwd = os.getcwd()
dir1 = str(cwd) + "\\Chrome_data\\Soundcloud"
dir2 = str(cwd) + "\\Chrome_data\\YouTube"


#browser settings
Soundcloud_options = Options()
Soundcloud_options.add_argument(f"user-data-dir={dir1}")

#browser settings
YouTube_options = Options()
YouTube_options.add_argument(f"user-data-dir={dir2}")





####################################### CHAT BOT ####################################################

data = json.load(open('data/chat.json', encoding='utf-8'))
def reply(query):
	if query in data:
		response =  data[query]
	else:
		query = get_close_matches(query, data.keys(), n=2, cutoff=0.6)
		if len(query)==0: return "None"
		return choice(data[query[0]])

	return choice(response)

####################################### SET UP SPEECH TO TEXT #######################################

def record(clearChat=True, iconDisplay=True):
    print('\nListening...')
    AITaskStatusLbl['text'] = 'Listening...'
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        AITaskStatusLbl['text'] = 'Waiting...'
        try:
         said = r.recognize_google(audio , language= "fa_IR")
        except:
           said = r.recognize_google(audio)
        print(f"\nUser said: {said}")
        if clearChat:
            clearChatScreen()
            attachTOframe(said)
    return said.lower()

def record2(clearChat=True, iconDisplay=True):
	print('\nListening...')
	AITaskStatusLbl['text'] = 'Listening...'
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False
	r.energy_threshold = 4000
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		said = ""
		AITaskStatusLbl['text'] = 'Waiting...'
		said = r.recognize_google(audio ,)
		print(f"\nUser said: {said}")
		if clearChat:
			clearChatScreen()
			attachTOframe(said)
	return said.lower()
    
def voiceMedium():
    wishMe()
    while True:
        try:
         q = record()
        except:
            attachTOframe('لطفا دوباره تکرار کنید',True)
            playsound('sound\\say_again.mp3')
            q = record2()
        if q == 'None': continue
        else: main(q.lower())

####################################### WISH USER ACCORDING TO TIME #################################

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        attachTOframe("صبح بخیر " , True)
        playsound('sound\\Good Morning.mp3')

    elif hour>=12 and hour<18:
        
        attachTOframe("ظهر بخیر " , True) 
        playsound('sound\\Good Afternoon.mp3')

    else:
        attachTOframe("شب بخیر " , True)  
        playsound('sound\\Good Evening.mp3')
    
    time.sleep(1)
    attachTOframe("چطور میتونم کمکتون کنم؟" , True)
    playsound('sound\\Help.mp3')

####################################### ATTACHING BOT/USER CHAT ON CHAT SCREEN ######################

def attachTOframe(text,bot=False):
	if bot:
		botchat = Label(chat_frame,text=text, bg="#810000", fg="white", justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
		botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)
	else:
		userchat = Label(chat_frame, text=text, bg="#CE1212", fg='white', justify=RIGHT, wraplength=250, font=('Montserrat',12, 'bold'))
		userchat.pack(anchor='e',ipadx=2,ipady=2,pady=5)

####################################### CLEAR CHAT SCREEN ###########################################

def clearChatScreen():
	for wid in chat_frame.winfo_children():
		wid.destroy()

####################################### SWITCHING BETWEEN FRAMES ####################################

def raise_frame(frame):
	frame.tkraise()
	clearChatScreen()

####################################### TASK/COMMAND HANDLER ########################################

def main(text):
       
        #open wikipedia
        if 'ویکی پدیا' in text:
            webbrowser.open("https://www.wikipedia.org/")
            attachTOframe("انجام شد",True)
            playsound('sound\\done.mp3')

        #open stackoverflow  
        elif 'stack overflow' in text:
            webbrowser.open("https://www.stackoverflow.com") 
            attachTOframe("انجام شد",True)
            playsound('sound\\done.mp3')
      
        #open github  
        elif 'github' in text or 'گیت هاب' in text:
            webbrowser.open("https://github.com/") 
            attachTOframe("انجام شد",True)
            playsound('sound\\done.mp3')

        #open facebook  #A#
        elif 'فیسبوک' in text:
            webbrowser.open("https://www.facebook.com")
            attachTOframe("انجام شد",True)
            playsound('sound\\done.mp3')

        #open telegram 
        elif 'تلگرام' in text:

            webbrowser.open("https://web.telegram.org/z/")
            attachTOframe("انجام شد",True)
            playsound('sound\\done.mp3')

        #Soundcloud
        elif 'ساند کلود' in text or 'سانکلود' in text:
         try:
            driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=Soundcloud_options)

            attachTOframe('چه چیزی را میخواهید جستجو کنید؟' , True)
            playsound('sound\\search.mp3')
                

            search_soundcloud = record(False)
            attachTOframe(search_soundcloud)

            driver.get('https://soundcloud.com/search/sounds?q=' + search_soundcloud)
            
            play_btn = driver.find_elements_by_xpath('//li[@class="searchList__item"]/div[@class="searchItem"]/div[@class="sound searchItem__trackItem track streamContext"]/div/div[@class="sound__content"]/div[@class="sound__header sc-mb-1.5x sc-px-2x"]/div/div/div/a')
            play_btn[0].click()

            
            while True: 
                soundcloud = record(False)  
                attachTOframe(soundcloud) 
            
                if 'بعدی' in soundcloud:
                    next_btn = driver.find_element_by_xpath('//div[@class="playControls__elements"]/button[@class="skipControl sc-ir playControls__control playControls__next skipControl__next"]')
                    next_btn.click()
            


                elif 'خارج شو' in soundcloud or 'خروج' in soundcloud:
                    driver.close()
                    break
              
                else:
                   break
         except:
              try:
                  driver.close()
              except:
                  pass
              #For handle errors
              attachTOframe('.مشکلی پیش آمده، لطفا اتصال اینترنت خود را بررسی کنید و دوباره امتحان کنید' , True)
              playsound('sound\\wrong.mp3')

        #YouTube Search
        elif  'یوتیوب' in text or 'youtube' in text:
          try:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=YouTube_options)
                #Get youtube url
                driver.get('https://www.youtube.com/')
                #put text on search box
                search_form = driver.find_element_by_xpath('//form[@class="style-scope ytd-searchbox"][@id="search-form"]/div/div/input')
                
                attachTOframe('چه چیزی را میخواهید جستجو کنید؟' , True)
                playsound('sound\\search.mp3')
               
                User_search = record(False)

                attachTOframe(User_search )
                search_form.send_keys(User_search)
                search_button = driver.find_element_by_xpath('//button[@class="style-scope ytd-searchbox"][@id="search-icon-legacy"]')
                search_button.click()

                attachTOframe('در اینجا نتایج را می بینید' , True)
                playsound('sound\\results.mp3')
          except:
                #For handle errors
                attachTOframe('.مشکلی پیش آمده، لطفا اتصال اینترنت خود را بررسی کنید و دوباره امتحان کنید' , True)
                playsound('sound\\wrong.mp3')

        #Speed Test
        elif 'سرعت اینترنت' in text:

            attachTOframe('...در حال تست کردن سرعت اینترنت' , True)
            playsound('sound\\internet speed.mp3')
            try:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
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

                attachTOframe(':سرعت پینگ ', True)
                attachTOframe(PING, True)
                playsound('sound\\PING.mp3')
                
                time.sleep(2)

                attachTOframe(':سرعت دانلود ' , True)
                attachTOframe(DOWNLOAD, True)
                playsound('sound\\DOWNLOAD.mp3')

                time.sleep(2)

                attachTOframe(':سرعت آپلود ', True)
                attachTOframe(UPLOAD, True)
                playsound('sound\\UPLOAD.mp3')

                driver.close()
            except:
                #For handle errors
                attachTOframe('.مشکلی پیش آمده، لطفا اتصال اینترنت خود را بررسی کنید و دوباره امتحان کنید' , True)
                playsound('sound\\wrong.mp3')

        #Corona Tracker#
        elif 'آمار کرونا' in text:
            try:
                attachTOframe('کدام کشور؟',True)
                playsound('sound\\which country.mp3')
                #Get country
                country = record2(False)
                attachTOframe(country)
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                if country != 'jahan':
                 driver.get('https://www.coronatracker.com/country/'+ country )

                 if 'Page Not Found' in driver.page_source:
                     attachTOframe('.کشور  مورد نظر یافت نشد. لطفا دوباره تلاش کنید' , True)
                     playsound('sound\\Not Found.mp3')
                     driver.close()
                     
                 else:

                  attachTOframe(':تعداد موارد ابتلا' , True)
                  playsound('sound\\Confirmed.mp3')
                  Confirmed = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-red-600"]').text
                  attachTOframe(Confirmed , True)

                  time.sleep(2)

                  attachTOframe(':بهبود یافتگان' , True)
                  playsound('sound\\Recovered.mp3')
                  Recovered = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-green-600"]').text
                  attachTOframe(Recovered , True)
                  
                  time.sleep(2)

                  attachTOframe(':جانباختگان' , True)
                  playsound('sound\\Deaths.mp3')
                  Deaths = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-gray-600"]').text
                  attachTOframe(Deaths , True)

                  driver.close()

                else:
                  #If user choose global
                  driver.get('https://www.coronatracker.com/')

                  attachTOframe(':تعداد موارد ابتلا' , True)
                  playsound('sound\\Confirmed.mp3')
                  Confirmed = driver.find_elements_by_xpath('//span[@class="mx-2"]')[0].text
                  attachTOframe(Confirmed , True)
 
                  time.sleep(2)

                  attachTOframe(':بهبود یافتگان' , True)
                  playsound('sound\\Recovered.mp3')
                  Recovered = driver.find_elements_by_xpath('//span[@class="mx-2"]')[2].text
                  attachTOframe(Recovered , True)

                  time.sleep(2)

                  attachTOframe(':جانباختگان' , True)
                  playsound('sound\\Deaths.mp3')
                  Deaths =  driver.find_elements_by_xpath('//span[@class="mx-2"]')[4].text
                  attachTOframe(Deaths , True)

                  driver.close()                    
  
            except:
                #For handle errors
                attachTOframe('.مشکلی پیش آمده، لطفا اتصال اینترنت خود را بررسی کنید و دوباره امتحان کنید' , True)
                playsound('sound\\wrong.mp3')
         
        #Roll a die or roll two dice
        elif 'دو' in text and 'تاس' in text:
           #Random number
           dice1 =  random.choice(['1','2','3','4','5','6'])
           dice2 =  random.choice(['1','2','3','4','5','6'])
           attachTOframe(dice1 + ' , ' + dice2 , True)
           playsound(f'sound\\{dice1}.mp3')
           playsound('sound\\and.mp3')
           playsound(f'sound\\{dice2}.mp3')
        elif 'تاس' in text:
           #Random number
           dice =  random.choice(['1','2','3','4','5','6'])
           attachTOframe( dice , True)
           playsound(f'sound\\{dice}.mp3')   

        #Flip a coin
        elif 'سکه' in text:
           #Random choice
           coin =  random.choice(['خط','شیر'])
           attachTOframe(coin , True)
           if coin == 'شیر':
            playsound('sound\\Heads.mp3') 
           else:
            playsound('sound\\Tails.mp3') 

        #What is your favorite color
        elif 'رنگ مورد علاقه' in text:
            #Random color
            color = random.choice([ ' سبز ' , ' قرمز ' , ' آبی '])

            if color == ' قرمز ':
             attachTOframe(' نرم افزارها معمولا علایق خاصی ندارند ولی من میگم '+ color + 'رنگ مورد علاقه ی تو چیه', True)
             playsound('sound\\favorite color.mp3') 
             playsound('sound\\RED.mp3') 
             playsound('sound\\your color.mp3') 

            if color == ' آبی ':
             attachTOframe(' نرم افزارها معمولا علایق خاصی ندارند ولی من میگم '+ color + 'رنگ مورد علاقه ی تو چیه', True)
             playsound('sound\\favorite color.mp3') 
             playsound('sound\\BLUE.mp3') 
             playsound('sound\\your color.mp3')             

            if color == ' سبز ':
             attachTOframe(' نرم افزارها معمولا علایق خاصی ندارند ولی من میگم '+ color + 'رنگ مورد علاقه ی تو چیه', True)
             playsound('sound\\favorite color.mp3') 
             playsound('sound\\GREEN.mp3') 
             playsound('sound\\your color.mp3') 
             
            #Get user color

            user_color = record(False)
            attachTOframe(user_color)
            
            attachTOframe('انتخاب خوبیه' , True)
            playsound('sound\\nice.mp3') 
      
        ##Rock Paper Scissors
        elif 'بازی' in text and 'سنگ' in text or 'کاغذ' in text or 'قیچی' in text:

                attachTOframe("شروع بازی سنگ کاغذ قیچی",True)
                playsound('sound\\start game.mp3')
                attachTOframe("یکی رو انتخاب کن (سنگ , کاغذ , قیچی)",True)
                playsound('sound\\game choice.mp3')
                user_action = record(False)
                attachTOframe(user_action)
                possible_actions = ["rock", "paper", "scissors"]
                computer_action = random.choice(possible_actions)


                if user_action == computer_action:
                    attachTOframe("انتخاب هر دویمان یکی بود, بازی مساوی شد",True)
                    playsound('sound\\tie.mp3')
            
                elif user_action == "سنگ":
                    if computer_action == "scissors":
                        attachTOframe("سنگ قیچی را خورد میکند !شما برنده شدید",True)
                        playsound('sound\\S vs R.mp3')
                
                    else:
                        attachTOframe("کاغذسنگ را میپوشاند ! شما باختید",True)
                        playsound('sound\\R vs P.mp3')
                
                elif user_action == "کاغذ":
                    if computer_action == "rock":
                        attachTOframe("کاغذ سنگ را میپوشاند ! شما برنده شدید",True)
                        playsound('sound\\P vs R.mp3')
                
                    else:
                        attachTOframe("قیچی کاغذ را می برد! شما باختید",True)
                        playsound('sound\\P vs S.mp3')

                elif user_action == "قیچی":
                    if computer_action == "paper":
                        attachTOframe("قیچی کاغذ را می برد! شما برنده شدید",True)
                        playsound('sound\\S vs P.mp3')
                
                    else:
                        attachTOframe("سنگ قیچی را خورد میکند !شما باختید",True)
                        playsound('sound\\R vs S.mp3')           

        #space game 
        elif 'بازی' in text and 'فضا' in text:
            import gamespace
        
        #time
        elif 'ساعت' in text:
            strTime = datetime.datetime.now().strftime("%H:%M")
            attachTOframe(strTime , True)
        
        #temperature
        elif 'دما' in text:
            search = "temperature"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_ = "BNeawe").text
            attachTOframe(f"{temperature} ",True)   
        
        #date
        elif 'امروز' in text or 'تاریخ' in text:
            t_date = datetime.datetime.now()
            attachTOframe(t_date.strftime('%D'),True)

        #open cmd
        elif 'cmd' in text:
            attachTOframe("درحال باز کردن برنامه" , True)
            playsound('sound\\open.mp3')
            os.system("start cmd")
        
        #open notepad
        elif 'notepad' in text or 'نوت پد' in text:
            path=("C:\\Windows\\system32\\notepad.exe")
            os.startfile(path)
            attachTOframe("درحال باز کردن برنامه",True)
            playsound('sound\\open.mp3')

        #take screenshot
        elif 'اسکرین شات' in text:
            screenshot = pg.screenshot()
            screenshot.save("Screenshot.png")
            attachTOframe("اسکرین شات گرفته شد",True)
            playsound('sound\\Screenshot.mp3')

        #take picture  
        elif 'عکس بگیر' in text:
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("Picture.jpg",frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            attachTOframe("انجام شد",True)
            playsound('sound\\done.mp3')
        
        #Shutdown
        elif "سیستم" in text and "خروج" in text or 'خارج' in text and 'سیستم' in text:
         attachTOframe('آیا مطمئنید که می خواهید از سیستم خود خارج شوید؟',True)
         #Get confirmed
         Confirmed = record(False)
         if 'بله' in Confirmed:
            attachTOframe('بسیار خوب' , True)
            playsound('sound\\Okay.mp3')
            #Sign out Windows
            os.system("shutdown -l")
        elif "خاموش" in text:
            attachTOframe('آیا مطمئنید که میخواهید سیستم خود را خاموش کنید؟ ',True)
            playsound('sound\\shutdown.mp3')
            #Get confirmed
            Confirmed = record(False)
            if 'بله' in Confirmed:
                attachTOframe('بسیار خوب' , True)
                playsound('sound\\Okay.mp3')
                #Shutdown Windows
                os.system("shutdown -s")
        elif "راه اندازی" in text:
            attachTOframe('آیا مطمئنید که میخواهید سیستم خود را دوباره راه اندازی کنید؟',True)
            playsound('sound\\restart.mp3')
            #Get confirmed
            Confirmed = record(False)
            if 'بله' in Confirmed:
                attachTOframe('بسیار خوب' , True)
                playsound('sound\\Okay.mp3')
                #Restart Windows
                os.system("shutdown -r")    
        
        #Alarm
        elif 'الارم' in text or 'هشدار' in text or 'تنظیم الارم' in text or 'تنظیم هشدار' in text:

            attachTOframe('برای چه ساعتی هشدار رو تنظیم کنم' , True)
            playsound('sound\\alarm.mp3')
            alarm_time = record(False)
            attachTOframe(alarm_time)
            if ":" in alarm_time:
               
                if len(alarm_time) == 4:
                            driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                            driver.get('https://kukuklok.com/')
                            sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                            sound.click()
                            sound.click()     
                            hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                            min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                            h = alarm_time[0]
                            m = alarm_time[2:]
                            for i in range(int(h)):
                                hour_bt.click()
                            for i in range(int(m)):
                                min_bt.click()     
                            set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                            set_Alarm.click()
                            driver.minimize_window()
                            speak('Done')

                elif len(alarm_time) == 5:

                        driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                        driver.get('https://kukuklok.com/')
                        sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                        sound.click()
                        sound.click()     
                        hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                        min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                        h = alarm_time[:2]
                        m = alarm_time[3:]
                        for i in range(int(h)):
                            hour_bt.click()
                        for i in range(int(m)):
                            min_bt.click()     
                        set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                        set_Alarm.click()
                        driver.minimize_window()


            elif ":" not in alarm_time:
           
             if len(alarm_time) == 3:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                driver.get('https://kukuklok.com/')
                sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                sound.click()
                sound.click()     
                hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                h = alarm_time[0]
                m = alarm_time[1:]
                for i in range(int(h)):
                 hour_bt.click()
                for i in range(int(m)):
                 min_bt.click()     
                set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                set_Alarm.click()
                driver.minimize_window()

          
             elif len(alarm_time) == 4:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                driver.get('https://kukuklok.com/')
                sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                sound.click()
                sound.click()     
                hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                h = alarm_time[:2]
                m = alarm_time[2:]
                for i in range(int(h)):
                 hour_bt.click()
                for i in range(int(m)):
                 min_bt.click() 
                set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                set_Alarm.click()
                driver.minimize_window()

     
      
            else:
                attachTOframe('لطفا فقط ساعت را بگویید',True)
                playsound('sound\\saytime.mp3')

        #play music
        elif 'آهنگ'in text or 'لیست پخش ' in text:
            music_dir = 'playlist'
            songs = os.listdir(music_dir)
            if songs == []:
                os.startfile('playlist')
                attachTOframe("من هیچ آهنگی پیدا نکردم لطفا لیست پخش خود را به اینجا انتقال دهید" ,True)
                playsound('sound\\song_notfound.mp3')
            else:
                counter = 0
                for li in songs:
                    s = (songs[counter])
                    playsound(f'playlist\\{s}')
                    counter +=1      

        #control volume #I#
        elif 'صدا' in text or 'زیاد' in text:
            pg.press("volumeup")
            pg.press("volumeup")
            pg.press("volumeup")
        elif 'صدا' in text or 'کم' in text:
            pg.press("volumedown")
            pg.press("volumedown")
            pg.press("volumedown")
        elif 'صدا' in text or 'قطع' in text:
            pg.press("volumemute")
           
        #Exit  
        elif 'خارج شو' in text or 'خداحافظ' in text or 'بدرود' in text:          
          attachTOframe('بدرود',True)
          playsound('sound\\Exit.mp3')
          root.destroy()
    

        #search on google
        else:
         result = reply(text)
         if result != "None": attachTOframe(result , True)
         else:      
                webbrowser.open("https://www.google.com/search?q=" + text)
                attachTOframe("این چیزیست که من در  وب پیدا کردم" , True)
                playsound('sound\\google_search.mp3')

       


############################################## GUI #############################################


root = Tk()
root.title('Eve')

root.geometry('400x640+1320+200')
root.resizable(False, False) 

root.iconphoto(False, PhotoImage(file='images/icon.png'))
root.pack_propagate(0)
root1 = Frame(root, bg='#170903')

for f in (root1,):
    f.grid(row=0, column=0, sticky='news')	
chat_frame = Frame(root1, width=380,height=551,bg='#170903')
chat_frame.pack(padx=10)
chat_frame.pack_propagate(0)
bottomFrame = Frame(root1,height=100)
bottomFrame.pack(fill=X, side=BOTTOM)
VoiceModeFrame = Frame(bottomFrame)
VoiceModeFrame.pack(fill=BOTH)

box = PhotoImage(file='images/box.png')
cbl = Label(VoiceModeFrame, fg='white', image=box,)
cbl.pack(pady=17)
AITaskStatusLbl = Label(VoiceModeFrame, text='Waiting...', fg='white', bg='#940A0A', font=('montserrat', 16))
AITaskStatusLbl.place(x=140,y=32)

Thread(target=voiceMedium).start()

raise_frame(root1)
root.mainloop()
