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

