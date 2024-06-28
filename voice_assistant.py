import pyttsx3
import os
import speech_recognition as sr
import controller as cnt  #importing the controller module to control the led
import time
import datetime
import wikipedia
import webbrowser
import pyautogui
from pynput.keyboard import Key,Controller
import keyboard
import dictapp
import smtplib
import warnings
warnings.filterwarnings("ignore")
#import playsound
import smtplib
import subprocess
import pyjokes




BOSS ="Sir" 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 175)
def speak(text):
    engine.say(text)  
    engine.runAndWait()
#speak('Allow me to introduce myself ') 
#speak("i am ASH")

def wishMe():
    hour=int(datetime.datetime.now().hour)
    #print(hour)
    if hour>=0 and hour <12:
        speak("Good Morning  " + BOSS)
    elif hour>=12 and hour<18:
        speak("Good Afternoon "+ BOSS)
    else:
        speak("Good Evening"+ BOSS)
    speak(" ASH ,at your service  ")
    speak("your AI Assistant ")
    speak("How may I help you?")


#Just A Really Very Intelligent System

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source,duration=0.2)
      print("Listening.......................")
      audio=r.listen(source)
      
      r.adjust_for_ambient_noise(source)
      r.pause_threshold=0.5
      r.energy_threshold=300
      try:
            print("Voice Recognize................")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")
      except Exception as e:
          speak("i didn't here that, sir ")
          
          speak(' your voice was too fast ')
          ##speak('or low')
          
          print("please Try Again.....................")
          return "None"
      return query
  
# remember to turn on less secure apps on your mail before
  #fill the details
def sendEmail(to,content):
      server=smtplib .SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.login('seyram1570@gmail.com', 'my password')
      server.sendmail('receiver', to, content)
      server.close()  
  
def note(text):       
      date=datetime.datetime.now()
      file_name=str(date).replace(":","-")+"-note.text"
      with open(file_name,'w') as f:
          f.write(query)
      
      subprocess.Popen(["notepad.exe",file_name]) 
  
  #speak('Allow me to introduce myself ') 
speak("i am ASH")

speak("A virtual Artificial intelligence")
speak("And i am here to assist you variety of task as best as i can")
speak(" 24 hours a day,7 days a week")
speak("initializing ASH.....")
print("initializing ASH.....")
#speak("importing all preferences........")
  
wishMe() 
  
      
if __name__ == '__main__':
     while True:
        query= takeCommand().lower()
        if 'the room is dark' in query:
            print("Turning light on..............")
            speak("okay sir,")
            speak("Turning on light.")
            cnt.led(1)
            
        elif 'turn off light' in query:
            print("light off..............")
            speak('light off..............')
            cnt.led(0)
            
            
        elif 'stage light' in query:
            print("led display..............")
            
            speak('party mode activated..............')
            cnt.lEd(2)
            
            
            
        if'close the system' in query:
            speak("Good bye..............")
            speak("Thank you for using me..............")
            print("The system is off")
            break
        
        elif 'play music'in query.lower():
            songs_dir=("D:\\SEYRAM\\Music(1)")
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'wikipedia' in query.lower():
            speak('searching wikipedia......')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2) 
            print(results)
            speak("According to Wikipedia")
            speak(results)
            
        elif 'ash'in query.lower():
            speak(("please sir,"))
            speak(("speak i'm listening"))
        elif 'open youtube'in query.lower():
            speak(("opening youtube sir"))
            #webbrowser.open("youtube.com")
            url="youtube.com"
          
            
                #chrome_path = 'C:/Program Files /Google/Chrome/Application/chrome.exe %s'
            chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        
        elif 'open google' in query.lower():
         print ("opening google................")
         speak("opening google..............")
         url="google.com"
         chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
         webbrowser.get(chrome_path).open(url)
            

        elif 'play a video online'in query.lower():
            speak(("opening youtube sir"))
            #webbrowser.open("youtube.com")
            url="https://www.youtube.com/watch?v=fNzpcB7ODxQ"
                                   #chrome_path = 'C:/Program Files /Google/Chrome/Application/chrome.exe %s'
            chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)


        elif 'gmail'in query.lower():
            speak("opening your mail sir")
            url="gmail.com"
        
           
            chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            
            
        elif 'my student portal'in query.lower():
            speak("opening your portal sir")   
            url="https://portal.umat.edu.gh/auth/Account/Login?ReturnUrl=%2Fauth%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DSTUDENT_PORTAL_PROD%26redirect_uri%3Dhttps%253A%252F%252Fportal.umat.edu.gh%252Fstudents%252Fsignin-oidc%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520api1.read%26code_challenge%3DwD4AgJPjjHN8Xotkp8h0vfubZi1xc2dTMYjOMplpTFw%26code_challenge_method%3DS256%26nonce%3D637905072682809002.NjBmY2RjYWUtYmZkNy00Y2I2LWIzZmMtYzFmNWQwOTJlNTk3ZDVlMzU1NTEtNWQ2Zi00NTlmLTk0MjktY2IzNGRkYjhhZWI4%26state%3DCfDJ8D94Vc7kT9JGtakwKfy00bu_iJEkeze1rpj8Vy4C1S8DwazfgUwx_mvh0XrNkGixS93A6slrQIkWpcxVvFFp89UPP07JK1YfZNjIIYA1TfZkOkfnNikYjZMp8V0ctJSP8RpVpGa9cCMWAhKr_SQpQZizM8A-mROHleZBNeVaKv_VzSYisUt-SQwMlE1lA2E-0CK0XYzxGqijcbhd1OmxTTrj6RsdNU38XEE-Fs8Vlhoc6faM9TPEMxXdElVkCrAAPDxcJfqAG9BLlNgL_oseScbg_WLwJ5GVnnUS_SNbXHCAxQOFk360un4GCk6a4228KPoOpSdjzL7n9Ks0xvEbqryUBo7ZdcNwZXDfkBy4PjXsYlXjG6er1bL2ooi9FRkf_JQU9vDF76eRdqjRtqt9-H4%26x-client-SKU%3DID_NETSTANDARD2_0%26x-client-ver%3D6.7.1.0"
                   
            chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            

        elif 'virtual learning platform'in query.lower():
                    
            url="https://foevle.umat.edu.gh"
            speak("opening your virtual learning platform sir")
            chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music'in query.lower():
            songs_dir=("D:\\SEYRAM\\Music(1)")
            songs=os.listdir(songs_dir)
            #d=random.choice(songs)
            speak("playing music for you sir")
            
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif 'the time' in query.lower():
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{BOSS}the time is {strTime}")
            
            
        elif "open code" in query.lower():
            codePath="C:\\Users\\SEYRAM\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
            
                     
        elif 'email to harry' in query.lower():
            try:
                speak("what should i send")
                content=takeCommand()
                to="ankahharrison@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
        
        elif "hello, Ash " in query.lower():
                    speak("Hello sir,how are you")
                    speak("at your service")
                  
               
        elif "i am fine" in query:
                    speak("We thank God sir")
                    speak(" am at your service,sir")
        elif "how are you"in query:
                    speak("i am fine sir")
                    speak("and you?")
                   # speak("at your service")
        elif"who created you" in query:
                    speak("My master is Ankah Harrison")
                    speak("i am always at his service ")
        elif "who are you?"in query:
                    speak("my masters Al Assistant")
        elif "i am bored"in query:
                    speak("try coding sir")
        elif "I'm bored"in query.lower():
                    speak("try coding sir")
        elif "can i be your friend "in query:
                    speak("it will be a great pleasure sir")
                
        elif"thank you" in query:
                    speak("you are welcome sir")
        elif" Ash who is Thomas"in query:
                    speak("Thomas is you best friend sir") 
        
        elif" remember that"in query:
            rememberMessage =query.replace("remember that","")
            rememberMessage =query.replace("Jarvis","")
            speak("you told me to remind you that"+rememberMessage)
            remember= open("Remember.txt","w")
            remember=open("Remember.txt","w")
            remember=write( rememberMessage)
            remember.close()
            
        elif "what do you remember" in query:
            remember=open("Remember.txt","r")
            speak("Your reminder"+remember.read())
            
            
        elif "note" in query or "remember this" in query:
                speak(" what wil you like me to keep")
                note_text=takeCommand
                note(note_text)
                speak(" i have taken note")     
            
        elif "pause" in query:
            pyautogui.press("k")
            speak("your video has been paused sir")
        
        elif"play" in query:
            pyautogui.press("k")
            speak("playing video sir")
        
        elif"mute" in query:
            pyautogui.press("m")
            speak("your video has been muted sir")
            
        elif"unmute" in query:
                pyautogui.press("um")
                speak("your video has been muted sir")
                
        elif"increase my volume" in query:
                from keyboard import volumeup
                speak("increasing your volume sir")
                volumeup()
                
        elif"decrease my volume" in query:
                from keyboard import volumedown
                speak("decreasing your volume sir")
                volumedown()
                
        elif "open" in query:
                from dictapp import openappweb
                openappweb(query)
        elif "joke" in query or" jokes"in query:
                speak(pyjokes.get_joke )
                
        # elif "play music " in query or "play a song" in query:
        #      talk("D:\\SEYRAM\\Music(1)")
        #      music_dir=" path"
        #      songs=os.listdir(music_dir)
        #      d=random.choice(songs)
        #      random=os.path.join(music_dir,d)
        #      playsound.playsound(random)       
                
        elif "close application" in query:
                from dictapp import openappweb
                openappweb(query)  
        
        elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
        
        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)        
                
        elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("Ash","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")   
                    
        elif "finally sleep" in query:
                    speak("Going to sleep, Boss")
                    speak("Let me know if you need anything")
                    speak("Good bye..............")                            
                    exit()

            
       
      