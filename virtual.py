import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import tkinter as tk
from PIL import ImageTk,Image
from jokyjokes import chucknorris

def run():

    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[1].id')
    engine.setProperty('rate',190)

    def speak(text):
        engine.say(text)
        engine.runAndWait()

    def wishMe():
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            speak("Hello,Good Morning")
            print("Hello,Good Morning")
            
            
            
        elif hour>=12 and hour<18:
            speak("Hello,Good Afternoon")
            print("Hello,Good Afternoon")
            
            
            

        else:
            speak("Hello,Good Evening")
            print("Hello,Good Evening")

    def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            
            audio=r.listen(source)

            try:
                statement=r.recognize_google(audio,language='en-in')
                print(f"user said:{statement}\n")                

            except Exception as e:
                speak("Pardon me, please say that again")
                return "None"
            return statement


    print('Loading your AI personal assistant - Silverus')
    speak("Loading your AI personal assistant Silverus")
    wishMe()

    if __name__=='__main__':


        while True:
            speak("Tell me how can I help you now?")
            statement = takeCommand().lower()
            if statement==0:
                continue

            if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
                speak('your personal assistant Silverus is shutting down,Good bye')
                print('your personal assistant Silverus is shutting down,Good bye')
                root.destroy()
                break



            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)           
                speak(results)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            elif 'open netflix' in statement:
                webbrowser.open_new_tab("https://www.netflix.com")
                speak("Netflix is open now")
                time.sleep(5)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif 'joke' in statement:
                joke = chucknorris.random()
                speak(joke)
                print(joke)
                time.sleep(5)

            elif "weather" in statement:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in Degree celsius is " +
                            str(current_temperature - 273.00) +
                            "\n humidity in percentage is " +
                            str(current_humidiy) +
                            "\n description  " +
                            str(weather_description))
                    print(" Temperature in degree Celsius = " + str(current_temperature - 273.00) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))
                    
                else:
                    speak(" City Not Found ")



            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am Silverus version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                        'opening youtube,google chrome,gmail and stackoverflow ,predict time,search wikipedia,predict weather' 
                        'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by tamanna ")
                print("I was built by Tamanna ")
                
                
                


            elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")

            elif 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            elif 'search'  in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            elif "read" in statement:
                speak(entry.get())
                entry.delete(0,"end")
                
            elif 'ask' in statement:
                speak('I can answer to computational and geographical questions and what question do you want to ask now')
                question=takeCommand()
                app_id="R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)
                
                
                


            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])



root = tk.Tk()
root.title('Silverus')

root.geometry('600x600')
load = Image.open("bg.jpeg")

render = ImageTk.PhotoImage(load)

img = tk.Label(root,image=render)
img.place(x=0,y=0)




label=tk.Label(root,text="Hi, I am Silverus",bg='DarkGoldenrod1',fg='black')
label.place(x=2,y=0,height=40,width=600)
label.config(font=('Comic Sans Ms',25))


entry = tk.Entry(root,bg='DarkGoldenrod1', fg = "black")
entry.place(x=150,y=80,height=40,width=300)

myImage = ImageTk.PhotoImage(file='redbutton.jpeg')

myButton = tk.Button(root,image=myImage,borderwidth=0, command = run)
myButton.place(x=292,y=403,height=20,width=20)

root.mainloop()










time.sleep(3)