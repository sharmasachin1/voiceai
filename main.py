import os
import eel
from engine.features import *
from engine.command import *

eel.init('www')
os.system('start chrome.exe --app="http://localhost:3000/index.html"')

eel.start('index.html', mode='chrome', host='localhost', block=True)
