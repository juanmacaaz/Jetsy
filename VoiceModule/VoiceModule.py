import pyttsx3
import time
import importlib




def voice_module(global_data):
    while 1:
        if global_data['voice'] != None:
            importlib.reload(pyttsx3)
            engine = pyttsx3.init()
            """ RATE"""
            rate = engine.getProperty('rate')  # getting details of current speaking rate
            engine.setProperty('rate', 150)

            """VOLUME"""
            volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
            engine.setProperty('volume', 1.0)

            """VOICE"""
            voices = engine.getProperty('voices')  # getting details of current voice
            # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
            print('Ha entrado')
            engine.say(global_data['voice'])
            engine.runAndWait()
            global_data['voice'] = None
            print('Ha llegado')
        time.sleep(0.66)
