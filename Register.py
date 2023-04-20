import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
import pymysql

import Game


class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '注册'
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

        self.registerButton = QPushButton('注册', self)
        self.registerButton.setStyleSheet('background-color: red;')
        self.registerButton.move(180, 90)
        self.registerButton.clicked.connect(self.register)

    def register(self):
        cnx = pymysql.connect(user='root', password='123456',
                              host='localhost', database='tank')
        cursor = cnx.cursor()
        username = self.username.text()
        password = self.password.text()
        if username:
            query = ("SELECT * FROM users WHERE username=%s")
            cursor.execute(query, (username))
            if cursor.fetchone() is not None:
                self.username.clear()
                self.password.clear()
                QMessageBox.warning(self, '失败', '用户名已经存在', QMessageBox.Ok)
            else:
                if password:
                    query = ("INSERT INTO users (username, password) VALUES (%s, %s)")
                    cursor.execute(query, (username, password))
                    cnx.commit()
                    self.username.clear()
                    self.password.clear()
                    QMessageBox.information(self, '成功', '注册成功！\n请返回登陆。', QMessageBox.Ok)
                    self.close()
                else:
                    self.username.clear()
                    self.password.clear()
                    QMessageBox.warning(self, '失败', '密码为空', QMessageBox.Ok)
        else:
            self.username.clear()
            self.password.clear()
            QMessageBox.warning(self, '失败', '用户名为空', QMessageBox.Ok)
