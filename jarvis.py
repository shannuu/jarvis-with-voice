import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio, torf):
    if torf == 0:
        print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!", 0)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!", 0)   

    else:
        speak("Good Evening!", 0)  
    speak(f'hello, iam jarvis, your personal assistant, please tell me how may i help you', 0)

wishMe()
print(f'\nIf you are stuck type help')
while True:
    query = input("\nHukum do mere Aaka: ")

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...', 0)
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia", 0)
        speak(results, 0)

    elif 'search' in query:
        query = query.replace("search", "")
        extraUrl = 'https://google.com/search?q='
        url = extraUrl + query
        speak(f'searching {query}', 0)
        webbrowser.open(url)

    elif 'open' in query:
        query = query.replace("open", "")
        if 'link' in query: 
            link = input('Enter the link: ')
            speak(f'opening {link}', 0)
            webbrowser.open(link)
        elif 'youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("opening youtube....", 0)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        else:
            link = input('Option not found, Please enter the url: ')
            speak(link ,0)
            webbrowser.open(link)   

    elif 'play music' in query:
        music_dir = 'enter the path'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}", 0)


    elif 'speak' in query:
        speak("what should i speak: ", 0)
        speach = input()
        speak(speach, 1)
        
    elif 'exit' or 'bye' in query:
        speak('Press Control \+ C to exit')

    elif 'help' in query:
        print('\n\nCommands:')
        print("     open \'website name or custom url\'")
        print('     wikipedia \'Anything\'')
        print('     search \'Anything\'')
        print('     play music')
        print('     time')
        print('     speak')
        print('     Control + C')

    else:
        print(f'Error: No Command Named {query}')
