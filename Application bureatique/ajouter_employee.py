# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajouter_employee.ui'
#
# Created: Thu May 03 13:36:09 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_Forme(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(528, 587)
        Form.move(670,50)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.ajout_employee_prenom_le = QtGui.QLineEdit(Form)
        self.ajout_employee_prenom_le.setGeometry(QtCore.QRect(170, 200, 221, 41))
        self.ajout_employee_prenom_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.ajout_employee_prenom_le.setObjectName(_fromUtf8("ajout_employee_prenom_le"))
        self.ajout_employee_rfid_le = QtGui.QLineEdit(Form)
        self.ajout_employee_rfid_le.setGeometry(QtCore.QRect(170, 260, 221, 41))
        self.ajout_employee_rfid_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.ajout_employee_rfid_le.setObjectName(_fromUtf8("ajout_employee_rfid_le"))
        self.ajout_employee_mdp_le = QtGui.QLineEdit(Form)
        self.ajout_employee_mdp_le.setGeometry(QtCore.QRect(170, 320, 221, 41))
        self.ajout_employee_mdp_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.ajout_employee_mdp_le.setEchoMode(QtGui.QLineEdit.Password)
        self.ajout_employee_mdp_le.setObjectName(_fromUtf8("ajout_employee_mdp_le"))
        self.btn_ajout_employee_ajouter = QtGui.QPushButton(Form)
        self.btn_ajout_employee_ajouter.setGeometry(QtCore.QRect(190, 390, 171, 41))
        self.btn_ajout_employee_ajouter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ajout_employee_ajouter.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btn_ajout_employee_ajouter.setObjectName(_fromUtf8("btn_ajout_employee_ajouter"))
        ##############################################
        self.btn_ajout_employee_ajouter.clicked.connect(self.save2database)
        ##############################################        
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 260, 141, 51))
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
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 140, 51, 51))
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
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 200, 71, 51))
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
        self.label_4.setGeometry(QtCore.QRect(50, 320, 111, 51))
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
        self.ajout_employee_nom_le = QtGui.QLineEdit(Form)
        self.ajout_employee_nom_le.setGeometry(QtCore.QRect(170, 140, 221, 41))
        self.ajout_employee_nom_le.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    \n"
"  padding : 6px 12px;\n"
"  font-size : 14px ;\n"
"  color :333 ;\n"
"  background-color :#fff;\n"
"  border : #4px solid #000;\n"
"  border-radius:5px;\n"
"}"))
        self.ajout_employee_nom_le.setText(_fromUtf8(""))
        self.ajout_employee_nom_le.setObjectName(_fromUtf8("ajout_employee_nom_le"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 471, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: #00bfff;\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: #FFFFFF;\n"
"   font-size: 50px;\n"
"   font-family: Algerian;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.btn_ajout_employee_ajouter, self.ajout_employee_nom_le)
        Form.setTabOrder(self.ajout_employee_nom_le, self.ajout_employee_prenom_le)
        Form.setTabOrder(self.ajout_employee_prenom_le, self.ajout_employee_rfid_le)
        Form.setTabOrder(self.ajout_employee_rfid_le, self.ajout_employee_mdp_le)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", " Ajouter employé", None))
        self.ajout_employee_prenom_le.setPlaceholderText(_translate("Form", "entrez le prénom", None))
        self.ajout_employee_rfid_le.setPlaceholderText(_translate("Form", "entrez le № de carte RFID ", None))
        self.ajout_employee_mdp_le.setPlaceholderText(_translate("Form", "entrez le mot de passe", None))
        self.btn_ajout_employee_ajouter.setText(_translate("Form", "Ajouter", None))
        self.label.setText(_translate("Form", "№ de carte RFID :", None))
        self.label_5.setText(_translate("Form", "Nom :", None))
        self.label_3.setText(_translate("Form", "Prénom :", None))
        self.label_4.setText(_translate("Form", "Mot de passe :", None))
        self.ajout_employee_nom_le.setPlaceholderText(_translate("Form", "entrez le nom", None))
        self.label_6.setText(_translate("Form", " Ajouter employé", None))

#################################################################################
    def save2database(self):
        
    
        _nom = str(self.ajout_employee_nom_le.text())
        _prenom = str(self.ajout_employee_prenom_le.text())
        _RFID = str(self.ajout_employee_rfid_le.text())
        _mot_de_passe = str(self.ajout_employee_mdp_le.text() )
        
        subprocess.Popen(["python","file_ajouter_employee.py",_nom,_prenom,_RFID,_mot_de_passe])
        
        self.ajout_employee_nom_le.setText("")
        self.ajout_employee_prenom_le.setText("")
        self.ajout_employee_rfid_le.setText("")
        self.ajout_employee_mdp_le.setText("")
#################################################################################        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Forme = QtGui.QWidget()
    ui = Ui_Forme()
    ui.setupUi(Forme)
    Forme.show()
    sys.exit(app.exec_())

