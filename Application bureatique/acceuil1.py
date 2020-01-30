# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acceuil.ui'
#
# Created: Mon May 07 21:14:27 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ajouter_employee import *
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

class Ui_Form(object):
    global AE
    global Cam
    global Temp
    global Hum
    global Gaz
    global Pres
    global LAdmin
    global LEntre
    global LExt
    global LInt
    global Buzz
    global Ventilo
    global UpdateEtatLampe
########################################################################
    def OpenUpdateEtatLampe(self):
        
        global UpdateEtatLampe
        UpdateEtatLampe = subprocess.Popen(["python","updateEtatLampe.py"], shell=False)

    
##########################################################################   
    def OpenCamera(self):
        global AE
        global Cam
        global Temp
        global Hum
        global Gaz
        global Pres
        global LAdmin
        global LEntre
        global LExt
        global LInt
        global Buzz
        global Ventil
        Cam = subprocess.Popen(["python","Camera1.py"], shell=False)
        try :
            AE.kill()
        except :
            pass
        try :
            LAdmin.kill()
        except :
            pass
        try :
            LEntre.kill()
        except :
            pass
        try :
            LExt.kill()
        except :
            pass
        try :
            LInt.kill()
        except :
            pass
        try :
            Buzz.kill()
        except :
            pass
        try :
            Ventilo.kill()
        except :
            pass
        try :
            Temp.kill()
        except :
            pass
        try :
            Hum.kill()
        except :
            pass
        try :
            Gaz.kill()
        except :
            pass
        try :
            Pres.kill()
        except :
            pass

        
##############################################################################
##########################################################################   
    def OpenAjouterEmployee(self):
        global AE
        global Cam
        global Temp
        global Hum
        global Gaz
        global Pres
        global LAdmin
        global LEntre
        global LExt
        global LInt
        global Buzz
        global Ventil
        AE = subprocess.Popen(["python","ajouter_employee.py"], shell=False)
        try :
            Cam.kill()
        except :
            pass
        try :
            LAdmin.kill()
        except :
            pass
        try :
            LEntre.kill()
        except :
            pass
        try :
            LExt.kill()
        except :
            pass
        try :
            LInt.kill()
        except :
            pass
        try :
            Buzz.kill()
        except :
            pass
        try :
            Ventilo.kill()
        except :
            pass
        try :
            Temp.kill()
        except :
            pass
        try :
            Hum.kill()
        except :
            pass
        try :
            Gaz.kill()
        except :
            pass
        try :
            Pres.kill()
        except :
            pass

##############################################################################
##########################################################################   
    def OpenContole(self):
        global Temp
        global Hum
        global Gaz
        global Pres
        global LAdmin
        global LEntre
        global LExt
        global LInt
        global Buzz
        global Ventilo
        global AE
        global Cam
        
        
        LAdmin = subprocess.Popen(["python","lampe_administration1.py"], shell=False)
        LEntre = subprocess.Popen(["python","lampe_entree1.py"], shell=False)
        LExt = subprocess.Popen(["python","lampe_externe1.py"], shell=False)
        LInt = subprocess.Popen(["python","lampe_interne1.py"], shell=False)
        Buzz = subprocess.Popen(["python","buzzer1.py"], shell=False)
        Ventilo = subprocess.Popen(["python","ventilateur1.py"], shell=False)
        try :
            AE.kill()
        except :
            pass
        try :
            Cam.kill()
        except :
            pass
        
        try :
            Temp.kill()
        except :
            pass
        try :
            Hum.kill()
        except :
            pass
        try :
            Gaz.kill()
        except :
            pass
        try :
            Pres.kill()
        except :
            pass
##############################################################################
##########################################################################   
    def OpenCapteurs(self):
        global Temp
        global Hum
        global Gaz
        global Pres
        global LAdmin
        global LEntre
        global LExt
        global LInt
        global Buzz
        global Ventilo
        
        Temp = subprocess.Popen(["python","temperature1.py"], shell=False)
        Hum = subprocess.Popen(["python","humidite1.py"], shell=False)
        Gaz = subprocess.Popen(["python","gaz1.py"], shell=False)
        Pres = subprocess.Popen(["python","presence1.py"], shell=False)

        try :
            LAdmin.kill()
        except :
            pass
        try :
            LEntre.kill()
        except :
            pass
        try :
            LExt.kill()
        except :
            pass
        try :
            LInt.kill()
        except :
            pass
        try :
            Buzz.kill()
        except :
            pass
        try :
            Ventilo.kill()
        except :
            pass
        try :
            AE.kill()
        except :
            pass
        try :
            Cam.kill()
        except :
            pass
        try :
            AE.kill()
        except :
            pass
        try :
            Cam.kill()
        except :
            pass
        

##############################################################################


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(590, 624)
        Form.move(20,20)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
"\n"
"\n"
""))
        self.btn_capteurs = QtGui.QPushButton(Form)
        self.btn_capteurs.setGeometry(QtCore.QRect(10, 20, 569, 140))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chiller"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_capteurs.setFont(font)
        self.btn_capteurs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_capteurs.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #53c687 ;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 5;\n"
"  -moz-border-radius: 5;\n"
"  border-radius: 5px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family: Chiller;\n"
"  color: #121254;\n"
"  font-size: 60px;\n"
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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/worldwide.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_capteurs.setIcon(icon)
        self.btn_capteurs.setIconSize(QtCore.QSize(300, 300))
        self.btn_capteurs.setObjectName(_fromUtf8("btn_capteurs"))
########################################################################
        self.btn_capteurs.clicked.connect(self.OpenCapteurs)
########################################################################
        self.btn_controle = QtGui.QPushButton(Form)
        self.btn_controle.setGeometry(QtCore.QRect(10, 170, 569, 140))
        self.btn_controle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_controle.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #ffcc80 ;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 5;\n"
"  -moz-border-radius: 5;\n"
"  border-radius: 5px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family:  Chiller;\n"
"  color: #121254;\n"
"  font-size: 60px;\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/controle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_controle.setIcon(icon1)
        self.btn_controle.setIconSize(QtCore.QSize(300, 300))
        self.btn_controle.setObjectName(_fromUtf8("btn_controle"))
########################################################################
        self.btn_controle.clicked.connect(self.OpenContole)
########################################################################
        self.btn_camera = QtGui.QPushButton(Form)
        self.btn_camera.setGeometry(QtCore.QRect(10, 320, 569, 140))
        self.btn_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_camera.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background:     #A9A9A9;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 5;\n"
"  -moz-border-radius: 5;\n"
"  border-radius: 5px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family:Chiller;\n"
"  color: #121254;\n"
"  font-size: 60px;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/camera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_camera.setIcon(icon2)
        self.btn_camera.setIconSize(QtCore.QSize(300, 300))
        self.btn_camera.setObjectName(_fromUtf8("btn_camera"))
########################################################################
        self.btn_camera.clicked.connect(self.OpenCamera)
########################################################################
        self.btn_ajout_employee = QtGui.QPushButton(Form)
        self.btn_ajout_employee.setGeometry(QtCore.QRect(10, 470, 569, 140))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chiller"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_ajout_employee.setFont(font)
        self.btn_ajout_employee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ajout_employee.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #bc8f8f ;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 5;\n"
"  -moz-border-radius: 5;\n"
"  border-radius: 5px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family: Chiller;\n"
"  color: #121254;\n"
"  font-size: 50px;\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/group.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ajout_employee.setIcon(icon3)
        self.btn_ajout_employee.setIconSize(QtCore.QSize(500, 500))
        self.btn_ajout_employee.setObjectName(_fromUtf8("btn_ajout_employee"))
########################################################################
        self.btn_ajout_employee.clicked.connect(self.OpenAjouterEmployee)
########################################################################
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Accueil", None))
        self.btn_capteurs.setText(_translate("Form", "    Capteurs", None))
        self.btn_controle.setText(_translate("Form", "   Contrôle", None))
        self.btn_camera.setText(_translate("Form", " Surveillance", None))
        self.btn_ajout_employee.setText(_translate("Form", " Ajouter employé", None))


import photos_rc

if __name__ == "__main__":
    import sys
    import subprocess
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

