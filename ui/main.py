from loginUi import *
from video import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.LButton.clicked.connect(self.loginTomain)

        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.show()

    def loginTomain(self):
        account = self.ui.Laccont.text()
        password = self.ui.Lpassword.text()
        if account == "1" and password == "1":
            self.win = videoWindow()
            self.close()
        else:
            QMessageBox.warning(self, "错误", "用户名或密码错误")

class videoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_videoWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.ui.widget)

        self.ui.pushButton.clicked.connect(self.open_in_video)
        self.ui.pushButton_2.clicked.connect(self.playPause)

        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.ui.horizontalSlider.sliderMoved.connect(self.updatePosition)

        self.show()

    def open_in_video(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()

    # 播放视频
    def playPause(self):
        if self.player.state()==1:
            self.player.pause()
        else:
            self.player.play()

    # 视频总时长获取
    def getDuration(self, d):
        '''d是获取到的视频总时长（ms）'''
        self.ui.horizontalSlider.setRange(0, d)
        self.ui.horizontalSlider.setEnabled(True)
        self.displayTime(d)

    # 视频实时位置获取
    def getPosition(self, p):
        self.ui.horizontalSlider.setValue(p)
        self.displayTime(self.ui.horizontalSlider.maximum()-p)

    # 显示剩余时间
    def displayTime(self, ms):
        minutes = int(ms/60000)
        seconds = int((ms-minutes*60000)/1000)
        self.ui.label.setText('{}:{}'.format(minutes, seconds))

    # 用进度条更新视频位置
    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(self.ui.horizontalSlider.maximum()-v)

if __name__ ==  '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
