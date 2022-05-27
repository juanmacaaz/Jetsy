import pyttsx3

engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty('rate', 150)

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty('volume', 1.0)

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

engine.say('Hello i am Jetsy, what can i do for you?')
engine.runAndWait()
