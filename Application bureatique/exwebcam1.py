# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webcam.ui'
#
# Created: Sat May 12 20:00:51 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import cv2


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
########################################################################    
    def start_webcam(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./self.fps)

##        self.capture=cv2.VideoCapture(0)
##        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,421)
##        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,601)
##
##        self.timer=QTimer()
##        self.timer.timeout.connect(self.update_frame)
##        self.timer.start(5)
    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        # My webcam yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)
    def setFPS(self, fps):
        self.fps = fps
    def update_frame(self):
        ret,self.image=self.capture.read()
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image,1)
        
        
        
    def stop_webcam(self):
        self.timer.stop()

    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if (len(img.shape))==3 :
            if img.shape[2]==4 :
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888

        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outImage=outImage.rgbSwapped()

        if window==1 :
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)
                
            
        
###########################################################################"        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(635, 517)
        Form.move(670,90)
        self.image=None
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.startButton = QtGui.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(10, 20, 301, 41))
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
##############################################################################################
        self.startButton.clicked.connect(self.start_webcam)
##############################################################################################
        self.stopButton = QtGui.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(320, 20, 301, 41))
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
##############################################################################################
        self.stopButton.clicked.connect(self.stop_webcam)
##############################################################################################
        self.imgLabel = QtGui.QLabel(Form)
        self.imgLabel.setGeometry(QtCore.QRect(20, 80, 601, 421))
        self.imgLabel.setFrameShape(QtGui.QFrame.Box)
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "webcam", None))
        self.startButton.setText(_translate("Form", "Démarrer la webcam", None))
        self.stopButton.setText(_translate("Form", "Arrêter la webcam", None))
        self.imgLabel.setText(_translate("Form", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

