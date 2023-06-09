import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from logging import exception
import webbrowser as web
import os
import smtplib
import winsound
import random
import pyjokes
import winshell
import json
import requests
from pywhatkit import misc
import calendar
import geocoder
import wolframalpha
import sys
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import yaml
from fuzzywuzzy import fuzz
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 150)
recognizer = sr.Recognizer()

def speak(audio):
    engine.say(audio)
    output_text.insert(tk.END, audio + '\n', "custom_tag")
    output_text.update()
    output_text.see('end')
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Voice Assistant Please tell me how may I help you?")


def takeCommand(text=None):
    if text:
        query = text
        output_text.insert(tk.END, "You said: " + query + '\n', "custom_tag")
        output_text.update()
        return query
    else:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            output_text.insert(tk.END, "Listening..." + '\n', "custom_tag")
            output_text.update()
            winsound.Beep(250, 500)
            r.energy_threshold = 500
            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            output_text.insert(tk.END, "Recognizing..." + '\n', "custom_tag")
            output_text.update()
            query = r.recognize_google(audio, language='en-in')
            output_text.insert(tk.END, "You said: " + query + '\n', "custom_tag")
            output_text.update()
        except Exception as e:
            speak("Say that again, please")
            query = "None"
    return query

def Email(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('teranuman@gmail.com', 'aykkhmytlxdhmwlp')
        server.sendmail('teranuman@gmail.com', to, content)
        server.close()
    # done = True
    except Exception as e:
        print(e)


def sendEmail():
    try:
        speak("What should I say?")
        content = takeCommand()
        speak("Please enter the email address and press send key:")
        input_text.unbind("<Return>")
        clearinp.configure(state='normal')  # Enable the "Send" button
        clearinp.configure(command=lambda: get_email_address(content))  # Update the command to call get_email_address

    except Exception as e:
        print(e)
        speak("I am not able to send this email")

def get_email_address(content):
    email_address = get_input1().lower()
    speak("Sending mail to " + email_address)
    Email(email_address, content)
    speak("Email has been sent!")
    clear_inbx()
    input_text.bind("<Return>", on_enter_key_press)


def create_note():

    speak("What do you want to add to notes?")

    done_notes = False

    while not done_notes:
        try:

            note = takeCommand()
            note = note.lower()  # type: ignore

            speak("Choose filename!")
            filename = takeCommand()
            filename = filename.lower()  # type: ignore

            with open(filename, 'w') as f:
                f.write(note)
            done_notes = True
            speak(f"I succesfully created the note, with name: {filename}")
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did't understood")

def show_note():
            speak("What is name of the note file?")
            nf = str(takeCommand())
            file = open(nf, "r")
            if nf == "none":
                  return
            speak("Showing Notes")
            a = (file.read())
            speak(a)

def news_listen():
    try:
        url = "https://newsapi.org/v2/top-headlines?country=in&q=india&pagesize=5&page=1&apiKey=47781a57b9bd4166a40440c3fa1d957f"
        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        
        speak("I have top 5 news headlines for you, which are as follows:")
        j = 1
        for article in arts:
            speak(f"Headline number {str(j)}")
            speak(article['title'])
            j = j+1
        speak("Thanks for listening the news headlines.")
    
    except Exception as e:      
        print(str(e))

def how_are_you():
    howareyou = ["I am good", "I am doing good", "I am doing fine today", "I am fine", "Can't be better", "I am hanging in there", "Can't complain", "Pretty good"]
    a = random.randint(0, 7)
    response_1 = str(howareyou[a])
    speak(response_1)
    speak("How about you?")

def shutdown():
    speak("Good Bye... Your system is going to shut down in a bit")
    return os.system("shutdown /s /t 1")
 

def restart():
    speak("Your system is about to restart, hope to see you back!")
    return os.system("shutdown /r /t 1")
 

def logout():
    speak("You are about to log out")
    return os.system("shutdown -l")

def wiki(query):

        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)

            speak(results)
        except exception as e:
            print(e)

def search(query):
        query = query.replace("search", "")
        try:
            web.open(f"https://www.google.com/search?q={query}&rlz=1C1UEAD_enIN1028IN1028&oq=hi&aqs=chrome..69i57j0i67i131i433j46i67i199i465j0i67l2j69i61l3.1343j0j7&sourceid=chrome&ie=UTF-8")
        except exception as e:
            print(e)

def printcalender():
    speak("Say the year you want calendar for: ")
    year = int(takeCommand())
    try:
        output_text.insert(tk.END, calendar.calendar(year) + '\n', "custom_tag")
    except exception as e:
        print(e)

def playYT(query):
            query = query.replace('play ', '')
            speak('playing ' + query)
            misc.playonyt(query)
            print(query)

def playMusic():
    try:
            music_dir = 'D:\Coding Exercises\Voice Assistant\Music'
            songs = os.listdir(music_dir)
            b =  random.randint(0, 4)
            output_text.insert(tk.END, f"Playing '" + str(songs[b]) +"'" '\n', "custom_tag")
            os.startfile(os.path.join(music_dir, songs[b]))
    except Exception as e:
        print(e)

def openWebsite(query):
        try:
            name = query.replace("open ", "")
            NameA = str(name)
            if 'youtube' in NameA:
                web.open("https://www.youtube.com/")
            elif 'instagram' in NameA:
                web.open("https://www.instagram.com/")
            else:
                string = "https://www." + NameA + ".com"
                string_2 = string.replace(" ", "")
                web.open(string_2)
        except exception as e:
            print(e)

def searchlocation(query):
    try:
            query = query.replace("where is", "")
            location = query
            speak(f"User asked to Locate {location}")
            web.open("https://www.google.com/maps/place/" + location + "")
    except exception as e:
        print(e)

def mylocation():
    try:
        g = geocoder.ip('')
        loc = g.address
        return loc
    except exception as e:
        print(e)

def weather(city):
    if city == "None":
        speak("You have not given any city, please try over again!")
        return
    try:
        api_key = "04e0c2957c596ded6723c4b68c2c246d"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
        
            current_temperature_k = y["temp"]
            current_temperature_c = current_temperature_k - 273.15
            current_temperature_c = float("{:.2f}".format(current_temperature_c))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]

            z = x["weather"]
            weather_description = z[0]["description"]
            speak(f"The Weather details for the city {city} is as follows:")
            speak(f"Temperature is {current_temperature_k} kelvin or {current_temperature_c}    celsius.")
            speak(f"Atmospheric pressure is {current_pressure} hPa unit.")
            speak(f"Humidity in percentage is {current_humidity}.")
            speak(f"It will be {weather_description}")  
 
        else:
            output_text.insert(tk.END, " City Not Found " + '\n', "custom_tag")
    except exception as e:
        print(e)

               
def close_app(app):
    app = app.replace("close ", "")
    import subprocess
    try:
        subprocess.call([f"taskkill","/F","/IM",f"{app}.exe"])
        speak(f"Successfully closed the {app}")
    except exception as e:
        print(e)

def question(question):
    try:
        app_id = 'WW6W3T-3LGT7WLPGA'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
    except:
        wiki(question)
        return
    
def load_conversations(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
        return data['conversations']
    
folder_path = 'Voice Assistant/conversations'

filenames = [
    os.path.join(folder_path, 'ai.yml'),
    os.path.join(folder_path, 'botprofile.yml'),
    os.path.join(folder_path, 'computers.yml'),
    os.path.join(folder_path, 'emotion.yml'),
    os.path.join(folder_path, 'food.yml'),
    os.path.join(folder_path, 'gossip.yml'),
    os.path.join(folder_path, 'greetings.yml'),
    os.path.join(folder_path, 'health.yml'),
    os.path.join(folder_path, 'history.yml'),
    os.path.join(folder_path, 'humor.yml'),
    os.path.join(folder_path, 'literature.yml'),
    os.path.join(folder_path, 'money.yml'),
    os.path.join(folder_path, 'movies.yml'),
    os.path.join(folder_path, 'politics.yml'),
    os.path.join(folder_path, 'psychology.yml'),
    os.path.join(folder_path, 'science.yml'),
    os.path.join(folder_path, 'sports.yml'),
    os.path.join(folder_path, 'trivia.yml'),
    os.path.join(folder_path, 'basic.yml'),
    os.path.join(folder_path, 'oneword.yml'),

]

conversations = []

for filename in filenames:
    conv = load_conversations(filename)
    conversations.extend(conv)



def get_response(query, threshold=60):
    best_matches = []
    best_score = 0

    for i, conv in enumerate(conversations):
        for j, utterance in enumerate(conv):
            score = fuzz.token_sort_ratio(query, utterance)
            if score > best_score:
                best_matches = [(i, j)]
                best_score = score
            elif score == best_score:
                best_matches.append((i, j))

    filtered_matches = [(i, j) for i, j in best_matches if best_score >= threshold]

    if filtered_matches:
        random_match = random.choice(filtered_matches)
        matching_conversation = conversations[random_match[0]]
        response_index = random_match[1] + 1
        if response_index < len(matching_conversation):
            response = matching_conversation[response_index]
            return response

    return None


def get_random_joke_from_humor_yml():
    joke_conversations = [conv[1] for conv in conversations if 'tell me a joke' in conv[0]]
    if joke_conversations:
        return random.choice(joke_conversations)
    return None


def on_speak_click():
        
        query = takeCommand().lower()

        response = get_response(query)
    
        if 'how are you' in query or 'how you doing' in query or 'what is going on' in query:
           how_are_you()
    
        elif 'fine' in query or 'good' in query or 'great' in query or 'wonderful' in query or 'awesome' in query:
            speak("I am happy listening that")
    
        elif 'thank you' in query or 'thanks' in query:
            speak("It's my pleasure!")

        elif 'you are ' in query:
            speak("It's okay! I will take it as a compliment.")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            try:
                root.destroy()
            except:
                sys.exit()

        elif "show note" in query:
            show_note()
        
        elif 'create note' in query:
            create_note()

        elif 'joke' in query:
            joke_source = random.choice(['pyjokes', 'Voice Assistant/conversations/humor.yml'])
            if joke_source == 'pyjokes':
                joke = pyjokes.get_joke()
            else:
                joke = get_random_joke_from_humor_yml()
    
            speak(joke)

        elif 'search' in query:
            search(query)


        elif 'close' in query:
            close_app(query)

        elif 'play music' in query or 'play songs' in query or 'play another song' in query:
           playMusic()


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        elif 'date' in query:
            today = datetime.date.today().strftime("%d %b, %Y")
            speak(f"Today date is {today}")

        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            try:
                os.startfile(codePath)

            except Exception as e:
                print(e)
        
        elif 'open notepad' in query:
            import subprocess
            subprocess.call(['notepad.exe', 'file.txt'])


        elif 'open word' in query:
           path= "C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)

        elif 'open powerpoint' in query or 'open power point' in query:
           path= "C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)

        elif 'open excel' in query:
           path= "C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)
        
        elif 'open chrome' in query:
           path= "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)

        # all open apps statements should be before the below statement

        elif 'open' in query:
            openWebsite(query)

        elif 'mail' in query:
            sendEmail()

        elif "who are you" in query or 'what is your name' in query or 'about you' in query or 'what can you do' in query or 'help me' in query:
            speak("I am your Voice Assistant")
            speak("I am able to do several tasks for you like, play music, crack some jokes, doing google searches for you, managing your computer functions and that's all on your voice command.")

        elif 'shutdown' in query or 'turn off' in query :
                shutdown()

        elif 'restart' in query:
                restart()

        elif 'log out' in query:
                logout()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin emptied")

        elif "where is" in query:
            searchlocation(query)

        elif 'news' in query:
           news_listen()

        elif 'play' in query:
            playYT(query)

        elif 'calendar' in query:
            printcalender()

        elif 'my location' in query:
            location = mylocation()
            speak(f"Based on your IP adress, your geolocation is:{location}")

        elif 'weather' in query or 'temperature' in query:
            city = mylocation()
            speak(f"You want to know weather of your current location {city}? or any other city?")
            cityinp = takeCommand()
            if 'current location' in cityinp or 'current city' in cityinp or 'my city' in cityinp:
                weather(city)
            elif 'None' in cityinp:
                speak("Say the name of the city again!")
                cityinp = takeCommand()
                weather(cityinp)
                
            else:
                weather(cityinp)

        elif 'what is my name' in query:
            with open('username.txt', 'r') as f:
                data = f.read()
            speak(f"Your are {data}")

        elif 'tell me about' in query:
            query = query.replace("tell me about ", "")
            question(query)
        
        elif 'what do you mean by' in query:
            query = query.replace("what do you mean by ", "")
            question(query)

        elif 'how many' in query:
            query = query.replace("", "")
            question(query)

        elif 'how much' in query:
            query = query.replace("", "")
            question(query)

        elif response is not None:
            speak(response)

        elif 'who is' in query:
            query = query.replace("who is ", "")
            question(query)

        elif 'what is' in query:
            query = query.replace("what is ", "")
            question(query)

        
        elif 'my name is ' in query:
            query = query.replace("my name is", "")
            with open('username.txt', 'w') as f:
                f.write(query)
            speak(f"I will remember, Your name is{query}")    
    
        elif 'ok' in query:
            speak("OK!")
        
        elif 'yes' in query or 'yeah' in query:
            speak("Oh I see!")
        
        elif 'no' in query or 'nah' in query:
            speak("Oh okayy!")

        else:

            speak("Sorry but I'm still trying to learn about this")
      

def on_send_click():
        
        input_data = get_input1().lower()
        query = takeCommand(input_data)

        response = get_response(query)

        if 'how are you' in query or 'how you doing' in query or 'what is going on' in query:
           how_are_you()
           
    
        elif 'fine' in query or 'good' in query or 'great' in query or 'wonderful' in query or 'awesome' in query:
            speak("I am happy listening that")
    
        elif 'thank you' in query or 'thanks' in query:
            speak("It's my pleasure!")

        elif 'you are ' in query:
            speak("It's okay! I will take it as a compliment.")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            try:
                root.destroy()
            except:
                sys.exit()

        elif "show note" in query:
            show_note()
        
        elif 'create note' in query:
            create_note()
 
        elif 'joke' in query:
            joke_source = random.choice(['pyjokes', 'Voice Assistant/conversations/humor.yml'])
            if joke_source == 'pyjokes':
                joke = pyjokes.get_joke()
            else:
                joke = get_random_joke_from_humor_yml()
    
            speak(joke)


        elif 'search' in query:
            search(query)


        elif 'close' in query:
            close_app(query)

        elif 'play music' in query or 'play songs' in query or 'play another song' in query:
           playMusic()


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        elif 'date' in query:
            today = datetime.date.today().strftime("%d %b, %Y")
            speak(f"Today date is {today}")

        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            try:
                os.startfile(codePath)

            except Exception as e:
                print(e)
        
        elif 'open notepad' in query:
            import subprocess
            subprocess.call(['notepad.exe', 'file.txt'])


        elif 'open word' in query:
           path= "C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)

        elif 'open powerpoint' in query or 'open power point' in query:
           path= "C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)

        elif 'open excel' in query:
           path= "C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)
        
        elif 'open chrome' in query:
           path= "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
           try:
                os.startfile(path)

           except exception as e:
            print(e)

        # all open apps statements should be before the below statement

        elif 'open' in query:
            openWebsite(query)

        elif 'mail' in query:
            sendEmail()

        elif "who are you" in query or 'what is your name' in query or 'about you' in query or 'what can you do' in query or 'help me' in query:
            speak("I am your Voice Assistant")
            speak("I am able to do several tasks for you like, play music, crack some jokes, doing google searches for you, managing your computer functions and that's all on your voice command.")

        elif 'shutdown' in query or 'turn off' in query :
                shutdown()

        elif 'restart' in query:
                restart()

        elif 'log out' in query:
                logout()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin emptied")

        elif "where is" in query:
            searchlocation(query)

        elif 'news' in query:
           news_listen()

        elif 'play' in query:
            playYT(query)

        elif 'calendar' in query:
            printcalender()

        elif 'my location' in query:
            location = mylocation()
            speak(f"Based on your IP adress, your geolocation is:{location}")

        elif 'weather' in query or 'temperature' in query:
            city = mylocation()
            speak(f"You want to know weather of your current location {city}? or any other city?")
            cityinp = takeCommand()
            if 'current location' in cityinp or 'current city' in cityinp or 'my city' in cityinp:
                weather(city)
            elif 'None' in cityinp:
                speak("Say the name of the city again!")
                cityinp = takeCommand()
                weather(cityinp)
                
            else:
                weather(cityinp)

        elif 'what is my name' in query:
            with open('username.txt', 'r') as f:
                data = f.read()
            speak(f"You are {data}")

        elif 'tell me about' in query:
            query = query.replace("tell me about ", "")
            question(query)


        elif 'what do you mean by' in query:
            query = query.replace("what do you mean by ", "")
            question(query)

        elif 'how many' in query:
            query = query.replace("", "")
            question(query)

        elif 'how much' in query:
            query = query.replace("", "")
            question(query)

        elif response is not None:
            speak(response)

        elif 'who is' in query:
            query = query.replace("who is ", "")
            question(query)

        elif 'what is' in query:
            query = query.replace("what is ", "")
            question(query)

        elif 'my name is ' in query:
            query = query.replace("my name is", "")
            with open('username.txt', 'w') as f:
                f.write(query)
            speak(f"I will remember, Your name is{query}")

        elif 'yes' in query or 'yeah' in query:
            speak("Oh I see!")
        
        elif 'no' in query or 'nah' in query:
            speak("Oh okayy!")    
    
        elif 'ok' in query:
            speak("OK!")

        else:
            speak("Sorry but I'm still trying to learn about this")

root = tk.Tk()

# set title
root.title("Voice Assistant")
# set default size
root.geometry("500x500")
# set the icon of the GUI
icon_path = "D:/Coding Exercises/Voice Assistant/app_icon.ico"
root.iconbitmap(icon_path)

# Input box


input_text = tk.Text(root, height=10, width=50, insertbackground='white', bg="black", fg="white", font=("Arial", 15, "bold"))
input_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
input_text.configure(bg='black')

def on_enter_key_press(event):
    on_send_click()

input_text.bind("<Return>", on_enter_key_press)

def clear_inbx():
    input_text.delete("1.0", "end")


input_text.tag_config("custom_tag", foreground='#FFFFFF', font=("Arial", 15, "bold"))

def get_input1():
    input_data = input_text.get("1.0", "end-1c").strip()
    input_text.delete("1.0", "end")
    input_text.tag_config("custom_tag", foreground="white")
    return input_data


#send button

bold_font = Font(family="Helvetica", size=12, weight="bold")

clearinp = tk.Button(root, text="Send", command=on_send_click, font=bold_font, background='#40414f', foreground='white')
clearinp.pack(padx=5, pady=5)
clearinp.configure(cursor='hand2', width=4, height= 2)

# speak button
img = Image.open("D:\Coding Exercises\Voice Assistant\mic.png")
img = img.resize((40, 40), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(img)
buttonSpeak = tk.Button(root, image=icon, command=on_speak_click, background='#40414f', foreground='#40414f')
buttonSpeak.pack(padx=5,pady=5)
buttonSpeak.configure(cursor='hand2')


#Output text box and scrollbar

output_frame = tk.Frame(root)
output_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
output_frame.configure(bg='#444654')

output_text = tk.Text(output_frame)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,  padx=10, pady=10)

scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.place(relx=2, rely=0, relheight=1, anchor=tk.NE)
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_text.yview)

output_text.config(yscrollcommand=scrollbar.set)
output_text.configure(insertontime=0)
output_text.configure(cursor='arrow', bg='black')
output_text.tag_config("custom_tag", foreground='#FFFFFF', font=("Arial", 16, "bold"))

root.after(500, wishMe)
root.configure(bg='#444654')  
root.mainloop()