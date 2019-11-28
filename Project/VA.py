from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
from brain import *
import random
import re
import sys
from time import sleep
from urllib.request import *
from urllib.error import *
import requests
import json
controlcodes={'livingroom_hall_on':101,'livingroom_hall_off':106,'livingroom_auto':110,'bedroom_room_on':102,'bedroom_room_off':107,'bedroom_room_auto':111,'diningroom_dininghall_on':103,'diningroom_dininghall_off':108,'diningroom_dininghall_auto':112,'fan_on':104,'fan_off':109,'door_open':119,'door_close':120}
statuscodes={'livingroom_auto':'1','bedroom_room_auto':'2','diningroom_dininghall_on':'3','fan_on':'4'}
def send_data_thingspeak(Code):
    fieldid='1'
    writekey='U6DEUI2SRWRL9WHW'
    code=str(Code)
    baseURL = 'http://api.thingspeak.com/update?api_key='+writekey+'&field'+fieldid+'='
    f = urlopen(baseURL+code)	
    print("Sending ",code," to thingspeak")
    retCode = int.from_bytes(f.read(), "big")
    f.close()
    if retCode!=48:
        print("Data sent to cloud succesfully.")
        return 1
    else:
        print("Data could not be sent to cloud.")
        return 0

def read_data_thingspeak(field):
    channelid='917359'
    fieldid=str(field)
    URL='https://api.thingspeak.com/channels/'+channelid+'/fields/'+fieldid+'.json?api_key='
    readkey='CU4W1P240POXKOQP'
    HEADER='&results=1'
    NEW_URL=URL+readkey+HEADER
    print("Contacting URL : ",NEW_URL)
    get_data=requests.get(NEW_URL).json()
    # print(get_data)
    # channel_id=get_data['channel']['id']
    fields=get_data['feeds']
    # print(fields)
    # t=[]
    for x in fields:
        return int(x['field'+fieldid])
# sleep(5)

def speak(word):
    engine.say(word)
    engine.runAndWait()

# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Your bot is listening, try to speak.")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("Could not recognize audio.")

# creating a function
def enter_function(event):
    btn.invoke()

def repeatL():
    while True:
        takeQuery()

def ask_from_bot():
    query = textF.get()
    print(query)
    answer_from_bot,tag=chat(query)
    msgs.insert(END, "you : " + ' '+query)
    #print(type(answer_from_bot))
    print(tag)
    if tag in controlcodes:
    	code=controlcodes[tag]
    	print(code)
    	send_data_thingspeak(code)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id) 
main = Tk()
main.geometry("500x650")
main.title("My Chat bot")
#img = PhotoImage(file="bot1.png")
#photoL = Label(main, image=img)
#photoL.pack(pady=5)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
#msgs1 = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
#msgs1.pack(side=RIGHT, fill=BOTH, pady=10)
frame.pack()
# creating text field
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

# going to bind main window with enter key...
main.bind('<Return>', enter_function)
t = threading.Thread(target=repeatL)
t.start()
main.mainloop()
