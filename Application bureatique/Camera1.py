# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherCameraExemple.ui'
#
# Created: Sat May 12 22:47:18 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
############################################################
import subprocess

global var
var =5
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
    global ProcCam
  
##########################################################################   
    def OpenCamera(self):
        
        
        global ProcCam
        
        
        ProcCam = subprocess.Popen(["python","Camera2.py"])
        
       
        
        


        
        
#############################################################################
##########################################################################   
    def CloseCamera(self):

        global ProcCam
        #print ProcCam.pid
        try :
            ProcCam.kill()
        except :
            pass
        


        
        
##############################################################################
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(467, 123)
        Form.move(700,35)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.startButton = QtGui.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(10, 10, 441, 41))
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.startButton.setObjectName(_fromUtf8("startButton"))
########################################################################
        self.startButton.clicked.connect(self.OpenCamera)
########################################################################
        self.stopButton = QtGui.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(10, 70, 441, 41))
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
########################################################################
        self.stopButton.clicked.connect(self.CloseCamera)
########################################################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Webcam", None))
        self.startButton.setText(_translate("Form", "Démarrer la webcam", None))
        self.stopButton.setText(_translate("Form", "Arrêter la webcam", None))


if __name__ == "__main__":
    import sys
    import subprocess
    



    
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

