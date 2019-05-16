from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys
import win32api
import speech_recognition as sr

r = sr.Recognizer()
class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
def PlayMusic():
    win32api.ShellExecute(0, 'open', 'music.mp3', '', '', 1)
def HelloWorld():
    win32api.ShellExecute(0, 'open', 'helloWorld.txt', '', '', 1)

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
mic = sr.Microphone()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    a=r.recognize_sphinx(audio)
    print("You said " + a)    # recognize speech using  Speech     Recognition
    if((a == "play music") | (a=="playing music") | (a=="the name music")):
        PlayMusic()
    if ((a == "hello world") | (a == "hello worlds")| (a == "as low world")):
        HelloWorld()

except LookupError:                            # speech is unintelligible
    print("Could not understand audio")

sys.exit(app.exec())

