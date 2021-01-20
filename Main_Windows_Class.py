
from main_window_interface import *
from PyQt5.QtWidgets import QApplication ,QMessageBox ,QWidget
from PyQt5.QtGui import QImage ,QPixmap
from PyQt5.QtCore import QTimer,QTime,QDateTime
from PyQt5.QtSql import QSqlDatabase,QSqlQueryModel,QSqlQuery
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from Person_Windows_Class import *

import face_recognition
import cv2
import qimage2ndarray

height = 480
width = 640
channel = 3
step = channel * width

class MainWindow(QtWidgets.QMainWindow,Ui_MainForm):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.MODEL = "hog"              
        # create a timer for clock
        self.timerClock = QTimer() 
        self.timerClock.timeout.connect(self.showTime) 
        self.timerClock.start(1000)
        # create exit button
        self.BtnExit.clicked.connect(self.close_app)
        # Open personfrm 
        self.BtnPersons.clicked.connect(self.OpenPersonfrm)
        # load video 
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.ShowVideos)
        # set control_bt callback clicked  function
        self.control_bt.clicked.connect(self.controlTimer)
               
        self.hog.clicked.connect(self.onClickedhog)
        self.cnn.clicked.connect(self.onClickedcnn)
        self.LblDate.setText(QDateTime.currentDateTime().toString('yyyy-MM-dd'))
        self.LblDate.setGeometry(620, 0, 150, 31)

    def onClickedcnn(self):
        self.MODEL= 'cnn'
     
    def onClickedhog(self):
        self.MODEL = 'hog'


# open person from
    def OpenPersonfrm(self):
        personWindow = PersonWindow(self)
        personWindow.LblImage.pixmap=self.image_label.pixmap
        personWindow.show()


 #show clock top right
    def showTime(self): 
        current_time = QTime.currentTime() 
        label_time = current_time.toString('hh:mm:ss') 
        self.LblTime.setText(label_time)


    def close_app(self):
        sys.exit(app.exec_())
        

        # start/stop timer
    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            self.control_bt.setText("توقف")
        else:
            self.timer.stop()
            self.cap.release()
            self.control_bt.setText("شروع")


        # show video
    def ShowVideos(self):
        ret, frame = self.cap.read()
       # call facedetection
        if self.ChBoxFaceDetect.isChecked():
            self.FaceDetected(frame)
        # resize frame image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.image_label.setPixmap(QPixmap.fromImage(image)) 
          
    
    def IsDuplicateFrame(self,frame,locations):
        Frame_encodes= face_recognition.face_encodings(frame,locations)        
        
        # Faces Detected
    def FaceDetected(self,frame):
        locations = face_recognition.face_locations(frame, model=self.MODEL)
        for (y1, x2, y2, x1) in locations:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)    