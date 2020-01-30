# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'humidite1.ui'
#
# Created: Tue May 08 12:38:30 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
########################################################
from config import*
import pyrebase
global ui
global Hum



firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(mail, password)

# Get a reference to the database service
db = firebase.database()





def stream_handler(message):
    global ui
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    global Hum
    Hum = (message["data"])
    ui.Set_Hum()

my_stream = db.child("Capteurs/Humidite").stream(stream_handler)


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
        Form.move(636,360)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 191, 71))
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
        self.lcd_number_humidite = QtGui.QLCDNumber(Form)
        self.lcd_number_humidite.setGeometry(QtCore.QRect(50, 100, 161, 111))
        self.lcd_number_humidite.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"   \n"
"  \n"
"   \n"
"   \n"
"  \n"
"   color: #FFFFFF;\n"
"    border-color: rgb(0, 0, 0);\n"
"   \n"
"}"))
        self.lcd_number_humidite.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_number_humidite.setLineWidth(1)
        self.lcd_number_humidite.setObjectName(_fromUtf8("lcd_number_humidite"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 80, 131, 161))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/hum5.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 90, 81, 131))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/percentage3.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Humidite", None))
        self.label_3.setText(_translate("Form", "Humidité", None))
#################################################################"""        

    def Set_Hum(self):
        global Hum
        self.lcd_number_humidite.display(Hum)
        
        
#########################################################################" 

import photos_rc

if __name__ == "__main__":
    import sys
    global ui
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

