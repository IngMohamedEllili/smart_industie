# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'presence1.ui'
#
# Created: Tue May 08 12:37:55 2018
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
        ui.Set_EtatPIR("Mouvement non Detectee")
    elif str(message["data"])== '1':
        ui.Set_EtatPIR("Mouvement Detectee")
        #EtatLampe1='ON'
    #ui.Set_EtatLampe1(EtatLampe1)

my_stream = db.child("Capteurs/PIR").stream(stream_handler)


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
        Form.move(1000,20)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 0, 201, 91))
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
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 141, 151))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/pir1.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_presence = QtGui.QLabel(Form)
        self.label_presence.setGeometry(QtCore.QRect(20, 80, 291, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_presence.setFont(font)
        self.label_presence.setStyleSheet(_fromUtf8("QLabel{\n"
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
        self.label_presence.setObjectName(_fromUtf8("label_presence"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Mouvement", None))
        self.label_3.setText(_translate("Form", "Presence", None))
        self.label_presence.setText(_translate("Form", "Mouvement non Détectée", None))
####################################################################
    def Set_EtatPIR(self,s):

        self.label_presence.setText(s)
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

