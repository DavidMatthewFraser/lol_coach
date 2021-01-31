import pyttsx3 as pp
import time as t
import random 

engine = pp.init()

name = 'David'

interval = 3
minutes = 60 * interval

lines = [
    'where is the enemy jungler',
    'are there any lanes to gank',
    'who is strong on their team and who is weak',
    'who should you target in team fights',
    'what objectives are up soon',
    'who has flash and who does not',
    'are you buying wards',
]

while True:
    t.sleep(minutes)
    engine.say("hey " + name + ", " + lines[random.randint(0, len(lines)-1)])
    engine.runAndWait()