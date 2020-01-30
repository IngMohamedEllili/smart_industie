# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temperature1.ui'
#
# Created: Tue May 08 12:37:15 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
########################################################
from config import*
import pyrebase

global Temp



firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(mail, password)

# Get a reference to the database service
db = firebase.database()





def stream_handler(message):

    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    global Temp
    Temp = (message["data"])
    ui.Set_temp()

my_stream = db.child("Capteurs/Temperature").stream(stream_handler)


#####################################


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(329, 280)
        Form.move (636,20)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 281, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: #00bfff;\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: #FFFFFF;\n"
"   font-size: 39px;\n"
"   font-family: Algerian;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lcd_number_temperatue = QtGui.QLCDNumber(Form)
        self.lcd_number_temperatue.setGeometry(QtCore.QRect(30, 100, 161, 111))
        self.lcd_number_temperatue.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"   \n"
"  \n"
"   \n"
"   \n"
"  \n"
"   color: #FFFFFF;\n"
"    border-color: rgb(0, 0, 0);\n"
"   \n"
"}"))
        self.lcd_number_temperatue.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_number_temperatue.setLineWidth(1)
        self.lcd_number_temperatue.setObjectName(_fromUtf8("lcd_number_temperatue"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 90, 101, 131))
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: #00bfff;\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: #4dd2ff;\n"
"   font-size: 80px;\n"
"   font-family: Algerian;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-10, 100, 111, 131))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/temperature.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Temperature", None))
        self.label_3.setText(_translate("Form", "Température", None))
        self.label.setText(_translate("Form", " °C ", None))
#################################################################"""        

    def Set_temp(self):
        global Temp
        self.lcd_number_temperatue.display(Temp)
        
        
#########################################################################" 

import photos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

