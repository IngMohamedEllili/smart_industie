# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gaz1.ui'
#
# Created: Tue May 08 12:38:11 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#######################################################################
from config import*
import pyrebase


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(mail, password)

# Get a reference to the database service
db = firebase.database()





def stream_handler(message):

    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    #global EtatLampe1
    if  str(message["data"])== '0':
       # EtatLampe1= 'OFF'
        ui.Set_EtatGaz("Gaz non Detectee")
    elif str(message["data"])== '1':
        ui.Set_EtatGaz("Gaz Detectee")
        #EtatLampe1='ON'
    #ui.Set_EtatLampe1(EtatLampe1)

my_stream = db.child("Capteurs/Gaz").stream(stream_handler)


######################################################################################
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
        Form.move(1000,360)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 0, 91, 91))
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
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 130, 141, 131))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/gaz1.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_gaz = QtGui.QLabel(Form)
        self.label_gaz.setGeometry(QtCore.QRect(60, 70, 221, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_gaz.setFont(font)
        self.label_gaz.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: rgb(255, 255, 255);\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: rgb(255, 255, 255);\n"
"   font-size: 25px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_gaz.setObjectName(_fromUtf8("label_gaz"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Gaz", None))
        self.label_3.setText(_translate("Form", "gaz", None))
        self.label_gaz.setText(_translate("Form", "Gaz  non Détectée", None))
####################################################################
    def Set_EtatGaz(self,s):

        self.label_gaz.setText(s)
####################################################################
import photos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

