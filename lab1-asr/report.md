# Report

​	Here is the report of lab1, it contains the modifications of GUI and the codes, as well as a feasible way to increase the accuracy of speech recognition.

### GUI

​	The GUI is made by Pyqt5 and Pyqt5-tools( qt-designer and PYUIC). I create a .ui file by qt-designer( asrInterface.ui), then use PYUIC to change .ui file to .py file.

​	.ui file is something just like XML. It has good portability and readability. Here is the code of asrInterface.ui.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1084</width>
    <height>734</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1084</width>
    <height>734</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1084</width>
    <height>734</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="widget" native="true">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>1091</width>
      <height>731</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>1091</width>
      <height>731</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>1091</width>
      <height>731</height>
     </size>
    </property>
    <property name="styleSheet">
     <string notr="true">background-image: url(:/newPrefix/C:/Users/user/Pictures/摄图网_500305545.jpg);</string>
    </property>
    <widget class="QTextBrowser" name="textBrowser">
     <property name="geometry">
      <rect>
       <x>410</x>
       <y>480</y>
       <width>256</width>
       <height>221</height>
      </rect>
     </property>
     <property name="contextMenuPolicy">
      <enum>Qt::NoContextMenu</enum>
     </property>
     <property name="acceptDrops">
      <bool>true</bool>
     </property>
     <property name="layoutDirection">
      <enum>Qt::LeftToRight</enum>
     </property>
     <property name="autoFillBackground">
      <bool>false</bool>
     </property>
     <property name="styleSheet">
      <string notr="true">image: url(:/background/play.gif);
background-image: url(:/background/play.gif);</string>
     </property>
    </widget>
    <widget class="QTextBrowser" name="textBrowser">
     <property name="geometry">
      <rect>
       <x>150</x>
       <y>80</y>
       <width>791</width>
       <height>231</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Cambria</family>
       <pointsize>18</pointsize>
      </font>
     </property>
     <property name="mouseTracking">
      <bool>false</bool>
     </property>
     <property name="tabletTracking">
      <bool>false</bool>
     </property>
     <property name="styleSheet">
      <string notr="true">background-image: url(:/background/C:/Users/user/Pictures/timg1.jpg);
background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));</string>
     </property>
     <property name="html">
      <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Cambria'; font-size:18pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'SimSun'; color:#0055ff;&quot;&gt;	&lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; color:#000000;&quot;&gt;1. You can say &amp;quot;&lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; font-weight:600; color:#ff0000;&quot;&gt;Play Music&lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; color:#0055ff;&quot;&gt;&amp;quot; &lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; color:#000000;&quot;&gt;to open the music I prepared for you!&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; color:#0055ff;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; color:#0055ff;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'SimSun'; color:#0055ff;&quot;&gt;	&lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; color:#000000;&quot;&gt;2. What's more, try to say &amp;quot;&lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; font-weight:600; color:#ff0000;&quot;&gt;Hello world&lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; color:#0055ff;&quot;&gt;&amp;quot; &lt;/span&gt;&lt;span style=&quot; font-family:'SimSun'; color:#000000;&quot;&gt;and check helloworld.txt!&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
     </property>
    </widget>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="image/image_used.qrc"/>
 </resources>
 <connections/>
</ui>
```

​	Then I use PYUIC to transform this file to a .py file(asrInterface.py). Here is the code.

``` python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 734)
        MainWindow.setMinimumSize(QtCore.QSize(1084, 734))
        MainWindow.setMaximumSize(QtCore.QSize(1084, 734))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1091, 731))
        self.widget.setMinimumSize(QtCore.QSize(1091, 731))
        self.widget.setMaximumSize(QtCore.QSize(1091, 731))
        self.widget.setStyleSheet("background-image: url(./image/摄图网_500305545.jpg);")
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(410, 480, 256, 221))
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser.setAcceptDrops(True)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-image:  url(./image/play.gif);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser1 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser1.setGeometry(QtCore.QRect(150, 80, 791, 231))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.textBrowser1.setFont(font)
        self.textBrowser1.setMouseTracking(False)
        self.textBrowser1.setTabletTracking(False)
        self.textBrowser1.setStyleSheet("background-image: url(./image/timg1.jpg);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.textBrowser1.setObjectName("textBrowser1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cambria\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; color:#0055ff;\">    </span><span style=\" font-family:\'SimSun\'; color:#000000;\">1. You can say &quot;</span><span style=\" font-family:\'SimSun\'; font-weight:600; color:#ff0000;\">Play Music</span><span style=\" font-family:\'SimSun\'; color:#0055ff;\">&quot; </span><span style=\" font-family:\'SimSun\'; color:#000000;\">to open the music I prepared for you!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; color:#0055ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; color:#0055ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; color:#0055ff;\">    </span><span style=\" font-family:\'SimSun\'; color:#000000;\">2. What\'s more, try to say &quot;</span><span style=\" font-family:\'SimSun\'; font-weight:600; color:#ff0000;\">Hello world</span><span style=\" font-family:\'SimSun\'; color:#0055ff;\">&quot; </span><span style=\" font-family:\'SimSun\'; color:#000000;\">and check helloworld.txt!</span></p></body></html>"))
```

​	Then we can use asr.py to call this interface. The code of calling is:

```python
from asrInterface import Ui_MainWindow
class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
app = QtWidgets.QApplication([])
application = myWindow()
application.show()
```

​	Now we can see our interface:

![1555828942794](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1555828942794.png)

### Speech recognition

​	The speech recognition is implemented by pocket-sphinx. It can recognize oral English, but you should speak accurately. So, for us, it’s accuracy is not very good. We can do something to improve the accuracy.

1. Speak more standard English. We can use some application to pronounce instead of us.
2. cut down the recognition dictionary. Reducing the number of recognizable words will help the program to understand you more easily, just let the program know what you want it to know.
3. Add fuzzy recognition. If you want to recognize “Play music”. You should also recognize “Playing music” to avoid recognition failure.
4. Retraining model. You can retrain the model to make it understand your pronounciation.

In my program, the code of speech recognition is like this:

```python
r = sr.Recognizer()
def PlayMusic():
    win32api.ShellExecute(0, 'open', 'music.mp3', '', '', 1)
def HelloWorld():
    win32api.ShellExecute(0, 'open', 'helloWorld.txt', '', '', 1)
mic = sr.Microphone()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    a = r.recognize_sphinx(audio)
    print("You said " + a)    # recognize speech using  Speech     Recognition
    if((a == "play music") | (a=="playing music") | (a=="the name music")):
        PlayMusic()
    if ((a == "hello world") | (a == "hello worlds")| (a == "as low world")):
        HelloWorld()

except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
```

