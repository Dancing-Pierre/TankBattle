# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDesktopWidget, QFrame
import os

from PIL import Image, ImageDraw, ImageFont

from Login import Login
from Register import Register
from PyQt5.QtCore import Qt
import Game


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('坦克大战')
        self.setFixedSize(688, 624)
        self.setStyleSheet('background-color: black;')

        self.login_up = Login()  # 创建的注册窗口
        self.register_up = Register()  # 创建的注册窗口

        # 创建一个标签并设置图像
        icon_label = QLabel(self)
        icon_pixmap = QPixmap('./assets/images/others/logo.jpg')
        icon_label.setPixmap(icon_pixmap)
        icon_label.setGeometry(85, 70, 521, 209)

        # 添加游戏简介标签
        intro_label = QLabel(self)
        intro_label.setText(
            '    坦克大战是一款经典的游戏，玩家可以控制坦克消灭敌\n人，获得胜利。当年出现在FC游戏机上的《坦克大战》，是\n一款非常经典的游戏，也是80、90后童年时代的回忆。这款\n游戏画面简洁、操作简单，玩家可以操控坦克穿越地形，消\n灭敌方坦克和防御塔。同时游戏中的障碍物和地形也会不时\n的升降移动，给游戏增添了一些难度和乐趣。虽然这款游戏\n制作很简单，但是它却深入人心，成为了众多玩家童年的回\n忆，更是一款不可多得的经典游戏。现在，您可以通过我们\n的程序，重温这款经典游戏的乐趣。')
        intro_label.setGeometry(85, 300, 521, 200)
        intro_label.setStyleSheet('font-size: 20px; color: white;')

        login_button = QPushButton('登陆', self)
        login_button.setGeometry(570, 20, 50, 30)
        login_button.setStyleSheet('background-color: red;')

        register_button = QPushButton('注册', self)
        register_button.setGeometry(630, 20, 50, 30)
        register_button.setStyleSheet('background-color: red;')

        # 实现功能，按钮点击之后执行的动作
        login_button.clicked.connect(self.login)
        register_button.clicked.connect(self.sign_up_window)

        # 连接 Login 窗口的 login_success_signal 信号和 login_success 槽函数
        self.login_up.login_success_signal.connect(self.login_success)

        self.center()
        self.show()

    def center(self):
        # 获取屏幕尺寸
        screen_size = QDesktopWidget().screenGeometry()
        # 获取窗口尺寸
        window_size = self.geometry()
        # 计算窗口左上角坐标
        x = (screen_size.width() - window_size.width()) // 2
        y = (screen_size.height() - window_size.height()) // 2
        # 设置窗口位置
        self.move(x, y)

    def sign_up_window(self):
        self.register_up.setWindowFlag(Qt.Dialog)
        self.register_up.show()

    def login(self):
        self.login_up.setWindowFlag(Qt.Dialog)
        self.login_up.show()

    def login_success(self, username):
        self.close()
        game = Game.TankGame()
        game.start_game(username)

    def create_image(self, text, font_name, font_size, text_color, output_path):
        font = ImageFont.truetype(font_name, font_size)
        text_width, text_height = font.getsize(text)
        image = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font, fill=text_color, outline=(0, 0, 0), width=3)
        image.save(output_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
