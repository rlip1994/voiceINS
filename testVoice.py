# Import the required module for text 
# to speech conversion 
from gtts import gTTS 
from playsound import playsound
import json
import speech_recognition as sr
language = 'es' # Language in which you want to convert 

r = sr.Recognizer()
def saySomething():    
    with sr.Microphone()as source:
        print("SAY SOMTHING")
        audio = r.listen(source)
        print("TIME OVER, THANKS")

    try:
        mytext=r.recognize_google(audio, language=language)
        print(mytext)
    except:
        pass
    return mytext



def textToVoice(text,mp3Name):
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    # Saving the converted audio in a mp3 file named  
    gTTS(text=text, lang=language, slow=False).save(mp3Name)


def openJSON(filename):
    json_data = open (filename).read ()
    return json.loads(json_data)



playsound("welcome.mp3")
