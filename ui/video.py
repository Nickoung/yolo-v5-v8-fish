# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zhy02\Desktop\urp\ui\video.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_videoWindow(object):
    def setupUi(self, videoWindow):
        videoWindow.setObjectName("videoWindow")
        videoWindow.resize(1078, 420)
        self.centralwidget = QtWidgets.QWidget(videoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 340, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 310, 981, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.widget = QVideoWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 521, 291))
        self.widget.setObjectName("widget")
        self.widget_2 = QVideoWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(540, 10, 521, 291))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 340, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1000, 310, 61, 16))
        self.label.setObjectName("label")
        videoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(videoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 23))
        self.menubar.setObjectName("menubar")
        videoWindow.setMenuBar(self.menubar)

        self.retranslateUi(videoWindow)
        QtCore.QMetaObject.connectSlotsByName(videoWindow)

    def retranslateUi(self, videoWindow):
        _translate = QtCore.QCoreApplication.translate
        videoWindow.setWindowTitle(_translate("videoWindow", "MainWindow"))
        self.pushButton.setText(_translate("videoWindow", "导入视频"))
        self.pushButton_2.setText(_translate("videoWindow", "播放/暂停"))
        self.pushButton_4.setText(_translate("videoWindow", "识别"))
        self.label.setText(_translate("videoWindow", "——/——"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    videoWindow = QtWidgets.QMainWindow()
    ui = Ui_videoWindow()
    ui.setupUi(videoWindow)
    videoWindow.show()
    sys.exit(app.exec_())