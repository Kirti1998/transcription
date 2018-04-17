# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os
import speech_recognition as sr
import os.path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.openFileNameDialog)
        self.horizontalLayout.addWidget(self.browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.extract_text = QtWidgets.QPushButton(self.centralwidget)
        self.extract_text.setObjectName("extract_text")
        self.verticalLayout.addWidget(self.extract_text)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.play_video = QtWidgets.QPushButton(self.centralwidget)
        self.play_video.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.play_video)
        self.video_with_caption = QtWidgets.QPushButton(self.centralwidget)
        self.video_with_caption.setObjectName("video_with_caption")
        self.horizontalLayout_2.addWidget(self.video_with_caption)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Video"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.extract_text.setText(_translate("MainWindow", "Extract text"))
        self.play_video.setText(_translate("MainWindow", "Play Video"))
        self.video_with_caption.setText(_translate("MainWindow", "Play Video with Caption"))

    def vediotoaudio(self, filename):
        # textfile_path = 'C:/Users/Preeti/PycharmProjects/transcription/videos.txt'
        # Read the text file
        #with open(filenames) as f:
            #content = f.readlines()
        # you may also want to remove whitespace characters like

        # at the end of each line
        #files_list = [x.strip() for x in content]
        # Extract audio from video.
        # It already save the video file using the named defined by output_name.
        #for file_num, file_path_input in enumerate(filenames, start=1):
            # Get the file name withoutextension
        file_name = os.path.basename(filename)
        if 'mouthcropped' not in file_name:
            raw_file_name = os.path.basename(file_name).split('.')[0]
            file_dir = os.path.dirname(filename)
            file_path_output = file_dir + '/' + raw_file_name + '.wav'
            print('processing file: %s' % filename)
            subprocess.call(
                ['ffmpeg', '-i', filename, '-codec:a', 'pcm_s16le', '-ac', '1', file_path_output])
            print('file %s saved' % file_path_output)
            self.audiototext(file_path_output)


    def audiototext(self, path):
        r = sr.Recognizer()
        if os.path.exists(path):
            print("File found")
        else:
            print("Error")
        with sr.AudioFile(path) as source:
            audio = r.record(source)

        print("Converting To Text...")
        txt = r.recognize_sphinx(audio)

        try:
            file = open('abc.txt', 'w')
            file.write(txt)
            file.close()
            print('saved')
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open File", "",
                                                  "Video Files (*.mp4 *.avi)", options=options)
        if fileName:
            self.lineEdit.setText(fileName)
            self.vediotoaudio(fileName)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

