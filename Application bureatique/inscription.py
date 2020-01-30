# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inscription.ui'
#
# Created: Sat May 05 22:16:51 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from bienvenue import *
############################################################
import subprocess
############################################################

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

class Ui_Formee(object):
    global Inscri
    global Bien
    global Formee

 ##########################################################################   
    def OpenBienvenue(self):


        Bien = subprocess.Popen(["python","bienvenue.py"], shell=False)
        Formee.hide()

        
        
        
##############################################################################

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(528, 587)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 250, 141, 51))
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
"   font-size: 17px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.inscription_nom_le = QtGui.QLineEdit(Form)
        self.inscription_nom_le.setGeometry(QtCore.QRect(150, 130, 221, 41))
        self.inscription_nom_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.inscription_nom_le.setObjectName(_fromUtf8("inscription_nom_le"))
        self.inscription_prenom_le = QtGui.QLineEdit(Form)
        self.inscription_prenom_le.setGeometry(QtCore.QRect(150, 190, 221, 41))
        self.inscription_prenom_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.inscription_prenom_le.setObjectName(_fromUtf8("inscription_prenom_le"))
        self.inscription_email_le = QtGui.QLineEdit(Form)
        self.inscription_email_le.setGeometry(QtCore.QRect(150, 250, 221, 41))
        self.inscription_email_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.inscription_email_le.setObjectName(_fromUtf8("inscription_email_le"))
        self.inscription_mdp_le = QtGui.QLineEdit(Form)
        self.inscription_mdp_le.setGeometry(QtCore.QRect(150, 310, 221, 41))
        self.inscription_mdp_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.inscription_mdp_le.setEchoMode(QtGui.QLineEdit.Password)
        self.inscription_mdp_le.setObjectName(_fromUtf8("inscription_mdp_le"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 71, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: rgb(255, 255, 255);\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: rgb(255, 255, 255);\n"
"   font-size: 17px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 310, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: rgb(255, 255, 255);\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: rgb(255, 255, 255);\n"
"   font-size: 17px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_inscription = QtGui.QPushButton(Form)
        self.btn_inscription.setGeometry(QtCore.QRect(170, 380, 171, 41))
        self.btn_inscription.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_inscription.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btn_inscription.setObjectName(_fromUtf8("btn_inscription"))
        ##############################################
        self.btn_inscription.clicked.connect(self.SaveDatabase)
        ############################################## 
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 130, 51, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: rgb(255, 255, 255);\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: rgb(255, 255, 255);\n"
"   font-size: 17px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 381, 101))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/inscription.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(280, 460, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font-family: Georgia, serif;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.btn_retour = QtGui.QPushButton(Form)
        self.btn_retour.setGeometry(QtCore.QRect(330, 530, 151, 41))
        self.btn_retour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_retour.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_retour.setIcon(icon)
        self.btn_retour.setIconSize(QtCore.QSize(50, 50))
        self.btn_retour.setObjectName(_fromUtf8("btn_retour"))
########################################################################
        self.btn_retour.clicked.connect(self.OpenBienvenue)
########################################################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.btn_inscription, self.inscription_nom_le)
        Form.setTabOrder(self.inscription_nom_le, self.inscription_prenom_le)
        Form.setTabOrder(self.inscription_prenom_le, self.inscription_email_le)
        Form.setTabOrder(self.inscription_email_le, self.inscription_mdp_le)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Inscription", None))
        self.label.setText(_translate("Form", "Adresse e-mail :", None))
        self.inscription_nom_le.setPlaceholderText(_translate("Form", "entrez votre nom", None))
        self.inscription_prenom_le.setPlaceholderText(_translate("Form", "entrez votre prénom", None))
        self.inscription_email_le.setPlaceholderText(_translate("Form", "entrez votre adresse e-mail", None))
        self.inscription_mdp_le.setPlaceholderText(_translate("Form", "entrez votre mot de passe", None))
        self.label_3.setText(_translate("Form", "Prénom:", None))
        self.label_4.setText(_translate("Form", "Mot de passe :", None))
        self.btn_inscription.setText(_translate("Form", "Inscription", None))
        self.label_5.setText(_translate("Form", "Nom :", None))
        self.label_6.setText(_translate("Form", "En appuyant sur Inscription, vous devez \n"
"retournez à la page précédente\n"
"pour se connecter .", None))
        self.btn_retour.setText(_translate("Form", " Retour", None))
#################################################################################
    def SaveDatabase(self):
        
    
        _nom = str(self.inscription_nom_le.text())
        _prenom = str(self.inscription_prenom_le.text())
        _adresse_email = str(self.inscription_email_le.text())
        _mot_de_passe = str(self.inscription_mdp_le.text() )
        
        subprocess.Popen(["python","file_inscription.py",_nom,_prenom,_adresse_email,_mot_de_passe])
        
        self.inscription_nom_le.setText("")
        self.inscription_prenom_le.setText("")
        self.inscription_email_le.setText("")
        self.inscription_mdp_le.setText("")
#################################################################################        

import photos_rc

if __name__ == "__main__":
    import sys
    import subprocess
    app = QtGui.QApplication(sys.argv)
    Formee = QtGui.QWidget()
    ui = Ui_Formee()
    ui.setupUi(Formee)
    Formee.show()
    sys.exit(app.exec_())

