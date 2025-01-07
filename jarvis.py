
import speech_recognition as sr
import webbrowser 
import win32com.client
import pyttsx3 as audio 
import openai 
import os
import datetime
import subprocess
import openai
from key import apiKey
import pywhatkit as pywhat
try:
    from googlesearch import search
except ImportError:
    print("sorry error found")
 
import random #for random sleep to avoid DOS

#USER AGENTS used to randomize searches in order to avoid error 503
#Currently 23 different generic user agents
TLDS = [
"com","ad","ae","com.af","com.ag","al","am","co.ao","com.ar","as","at","com.au","az","ba","com.bd","be","bf","bg","com.bh","bi","bj","com.bn","com.bo","com.br","bs","bt","co.bw","by","com.bz","ca","cd","cf","cg","ch","ci","co.ck","cl","cm","cn","com.co","co.cr","com.cu","cv","com.cy","cz","de","dj","dk","dm","com.do","dz","com.ec","ee","com.eg","es","com.et","fi","com.fj","fm","fr","ga","ge","gg","com.gh","com.gi","gl","gm","gr","com.gt","gy","com.hk","hn","hr","ht","hu","co.id","ie","co.il","im","co.in","iq","is","it","je","com.jm","jo","co.jp","co.ke","com.kh","ki","kg","co.kr","com.kw","kz","la","com.lb","li","lk","co.ls","lt","lu","lv","com.ly","co.ma","md","me","mg","mk","ml","com.mm","mn","com.mt","mu","mv","mw","com.mx","com.my","co.mz","com.na","com.ng","com.ni","ne","nl","no","com.np","nr","nu","co.nz","com.om","com.pa","com.pe","com.pg","com.ph","com.pk","pl","pn","com.pr","ps","pt","com.py","com.qa","ro","ru","rw","com.sa","com.sb","sc","se","com.sg","sh","si","sk","com.sl","sn","so","sm","sr","st","com.sv","td","tg","co.th","com.tj","tl","tm","tn","to","com.tr","tt","com.tw","co.tz","com.ua","co.ug","co.uk","com.uy","co.uz","com.vc","co.ve","co.vi","com.vn","vu","ws","rs","co.za","co.zm","co.zw","cat"
]


speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Set sapi.voice = sapi.GetVoices.Item(0) 

# Dim sapi 
# Set sapi = CreateObject("sapi.spvoice") 
# Set sapi.voice = sapi.GetVoices.Item(0) 
# sapi.speak "Welcome to Windows 11"


engine=audio.init()

def speak(text):
    speaker.Speak(text)

# def speak2(text):
    # engine.say(text)
    # engine.runAndWait()
     



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.pause_threshold = 0.8
        print("jarvis listening....")
        audio = r.listen(source)
      
        try:
            query = r.recognize_google(audio, language = 'en-in')
            print(query)
            return query
        except Exception as e:
            print("some error occured")
            return("some error occured")
        

print("This is jarvis ai")
speak("This is jarvis ai")
sites=[["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],["instagram","https://www.instagram.com/"],["facebook","https://www.facebook.com/"],["wikipedia","https://www.wikipedia.com/"]]
var = takeCommand()
# for site in sites:
#     if  (f"Open {site[0]}").lower() in var.lower():
#             speak(f"opening{site[0]} sir")
#             webbrowser.open(site[1])
if "the time" in var.lower():
        strfTime=datetime.datetime.now().strftime("%H:%M:%S") 
        timestr = f"The time is {strfTime}"
        print(timestr)
        speak(timestr)
elif "open " in var.lower():
    toOpen = var.lower().replace("open ","")
    i=True
    while(i):
        try:
            for j in search(toOpen, tld=random.choice(TLDS)):
                    print(j)
                    speak("Opening " + toOpen)
                    webbrowser.open(j)
                    i = False
                    break
        except:
            print("SOME ERR....")


elif "open code"in var.lower():
     vsCode= "C:\\Users\\bibha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
     print("opening code")
     speak("opening code") 
     subprocess.call([vsCode])

elif "open downloads" in var.lower(): 
     downloadsPath = "C:\\Users\\bibha\\Downloads"
     print("opening downloads")
     speak("opening downloads")
    #  subprocess.call([downloadsPath])
     os.startfile(downloadsPath)
else:
    if var:
        openai.api_key = apiKey

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': var}
            ],
            temperature=0,
            stream=True  # this time, we set stream=True
        )

        count = 0
        content = ""
        for chunk in response:
            try:
                 print(chunk['choices'][0]["delta"]["content"])
                 content += chunk['choices'][0]["delta"]["content"]
                 count += 1 
                 if count > 10:
                      speak(content)
                      count = 0
                      content = ""
            except:
             speak(content)
             print("END....")


            
            