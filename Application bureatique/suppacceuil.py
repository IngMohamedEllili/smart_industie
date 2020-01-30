# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bienvenue.ui'
#
# Created: Thu May 03 14:01:03 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from inscription import *
############################################################
import subprocess
##########################################################
import acceuil1
import alerte
import capteurs
import controle
#######################################################################
from config import*
import pyrebase


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(mail, password)

# Get a reference to the database service
db = firebase.database()
#########################################9


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

class Ui_widget(object):

 ##########################################################################   
    def OpenInscription(self):
        
        self.widget = QtGui.QWidget()
        self.ui = Ui_Formee()
        self.ui.setupUi(self.widget)
        widget.hide()
        self.widget.show()
##############################################################################
    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.resize(777, 587)
        widget.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}"))
        self.bienvenue_mdp_le = QtGui.QLineEdit(widget)
        self.bienvenue_mdp_le.setGeometry(QtCore.QRect(230, 280, 331, 41))
        self.bienvenue_mdp_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:15px;\n"
"}"))
        self.bienvenue_mdp_le.setEchoMode(QtGui.QLineEdit.Password)
        self.bienvenue_mdp_le.setObjectName(_fromUtf8("bienvenue_mdp_le"))
        self.label = QtGui.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(70, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: rgb(255, 255, 255);\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: rgb(255, 255, 255);\n"
"   font-size: 20px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_connexion = QtGui.QPushButton(widget)
        self.btn_connexion.setGeometry(QtCore.QRect(300, 350, 161, 41))
        self.btn_connexion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_connexion.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #4169E1 ;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 10;\n"
"  -moz-border-radius: 10;\n"
"  border-radius: 10px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family: Georgia;\n"
"  color: #ffffff;\n"
"  font-size: 18px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #4f5a64;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}\n"
"\n"
""))
        self.btn_connexion.setObjectName(_fromUtf8("btn_connexion"))
########################################################################
        self.btn_connexion.clicked.connect(self.login)
########################################################################
        self.label_2 = QtGui.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(80, 270, 131, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: rgb(255, 255, 255);\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: rgb(255, 255, 255);\n"
"   font-size: 20px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.bienvenue_email_le = QtGui.QLineEdit(widget)
        self.bienvenue_email_le.setGeometry(QtCore.QRect(230, 210, 331, 41))
        self.bienvenue_email_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:15px;\n"
"}"))
        self.bienvenue_email_le.setFrame(True)
        self.bienvenue_email_le.setObjectName(_fromUtf8("bienvenue_email_le"))
        self.btn_bienvenue_inscription = QtGui.QPushButton(widget)
        self.btn_bienvenue_inscription.setGeometry(QtCore.QRect(540, 500, 171, 41))
        self.btn_bienvenue_inscription.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_bienvenue_inscription.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #4169E1 ;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 5;\n"
"  -moz-border-radius: 5;\n"
"  border-radius: 5px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family: Georgia;\n"
"  color: #ffffff;\n"
"  font-size: 18px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #4f5a64;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}\n"
"\n"
""))
        self.btn_bienvenue_inscription.setObjectName(_fromUtf8("btn_bienvenue_inscription"))
########################################################################
        self.btn_bienvenue_inscription.clicked.connect(self.OpenInscription)
########################################################################
        self.label_3 = QtGui.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(470, 470, 291, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font-family: Georgia, serif;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(80, 50, 511, 151))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/bienvenue.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)
        widget.setTabOrder(self.btn_connexion, self.bienvenue_email_le)
        widget.setTabOrder(self.bienvenue_email_le, self.bienvenue_mdp_le)
        widget.setTabOrder(self.bienvenue_mdp_le, self.btn_bienvenue_inscription)

    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "SoLi", None))
        self.bienvenue_mdp_le.setPlaceholderText(_translate("widget", "entrez votre mot de passe", None))
        self.label.setText(_translate("widget", "Adresse e-mail :", None))
        self.btn_connexion.setText(_translate("widget", "Connexion", None))
        self.label_2.setText(_translate("widget", "Mot de passe :", None))
        self.bienvenue_email_le.setPlaceholderText(_translate("widget", "entrez votre adresse e-mail", None))
        self.btn_bienvenue_inscription.setText(_translate("widget", "Inscription", None))
        self.label_3.setText(_translate("widget", "Vous n\'avez pas un compte ?Connectez-vous", None))
##############################################################################

    def login(self):
        j = 0
        Email = self.bienvenue_email_le.text()
        Password = self.bienvenue_mdp_le.text ()
        import subprocess
        x = db.child("Inscription_Qt").get().val()
        print x
        for k1 , k2 in x.iteritems() :
            if (k2["Email"]  == Email) and ( k2["MDP"]  == Password ):
                
                subprocess.Popen(["python","acceuil1.py"], shell=False)
                widget.hide()
            else :
                print "incorrect"
                subprocess.Popen(["python","alerte.py"], shell=False)
##        if ( j == 0 ):
##            print "incorrect les 2 "
##            subprocess.Popen(["python","alerte.py"], shell=False)
##        
        self.bienvenue_email_le.setText('')
        self.bienvenue_mdp_le.setText('')
                

            

        



        
################################################################################

                                        
import photos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

