from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
import pymysql


class Login(QWidget):
    login_success_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.title = '登陆'
        self.width = 300
        self.height = 150
        self.initUI()

    def initUI(self):
        # 获取屏幕大小和位置
        screen_size = QDesktopWidget().screenGeometry()
        # 计算窗口的位置
        self.left = (screen_size.width() - self.width) // 2
        self.top = (screen_size.height() - self.height) // 2
        # 移动窗口到屏幕中心
        self.move(self.left, self.top)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('账号:')
        self.usernameLabel.move(20, 20)
        self.username = QLineEdit(self)
        self.username.move(100, 20)

        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText('密码:')
        self.passwordLabel.move(20, 50)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(100, 50)

        self.loginButton = QPushButton('登陆', self)
        self.loginButton.setStyleSheet('background-color: red;')
        self.loginButton.move(20, 90)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        username = self.username.text()
        password = self.password.text()

        cnx = pymysql.connect(user='root', password='123456',
                              host='localhost', database='tank')
        cursor = cnx.cursor()
        query = ("SELECT * FROM users WHERE username=%s AND password=%s")
        cursor.execute(query, (username, password))

        if cursor.fetchone() is not None:
            self.close()
            self.login_success_signal.emit(username)  # 发射登录成功信号
        else:
            QMessageBox.warning(self, '错误', '账号或密码错误', QMessageBox.Ok)
