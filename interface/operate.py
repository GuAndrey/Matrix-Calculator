import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Operate(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.initUI()

    def initUI(self):
        self.setFixedSize(124, 218)

        #Определение путей для изображений
        imageDir = os.path.dirname(os.path.realpath(__file__)).replace('interface', 'image') +  os.path.sep 
        self.plus_path = imageDir + 'plus.png'
        self.minus_path = imageDir + 'minus.png'
        self.minus2_path = imageDir + 'minus2.png'
        self.plus2_path = imageDir + 'plus2.png'
        self.mult_path = imageDir + 'mult.png'
        self.replace_path = imageDir + 'replace.png'

        #Увеличение ранга
        btn_expand = QPushButton()
        btn_expand.setFixedSize(37, 37)
        btn_expand.setIcon(QIcon(self.plus_path))
        btn_expand.setStyleSheet('''QPushButton { icon-size: 35px; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_expand.clicked.connect(self.expand)

        #Уменьшение ранга
        btn_cut = QPushButton()
        btn_cut.setFixedSize(37, 37)
        btn_cut.setIcon(QIcon(self.minus_path))
        btn_cut.setStyleSheet('''QPushButton { icon-size: 35px; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_cut.clicked.connect(self.cut)

        #Смена мест
        btn_replace = QPushButton()
        btn_replace.setFixedSize(37, 37)
        btn_replace.setIcon(QIcon(self.replace_path))
        btn_replace.setStyleSheet('''QPushButton { icon-size: 35px; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_replace.clicked.connect(self.replace)

        #Умножение
        btn_mult = QPushButton()
        btn_mult.setFixedSize(37, 37)
        btn_mult.setIcon(QIcon(self.mult_path))
        btn_mult.setStyleSheet('''QPushButton { icon-size: 35px; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_mult.clicked.connect(self.mult)

        #Сложение
        btn_add = QPushButton()
        btn_add.setFixedSize(37, 37)
        btn_add.setIcon(QIcon(self.plus2_path))
        btn_add.setStyleSheet('''QPushButton { icon-size: 35px; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_add.clicked.connect(self.add)

        #Вычитание
        btn_sub = QPushButton()
        btn_sub.setFixedSize(37, 37)
        btn_sub.setIcon(QIcon(self.minus2_path))
        btn_sub.setStyleSheet('''QPushButton { icon-size: 35px; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_sub.clicked.connect(self.sub)

        #Разметка
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox2 = QVBoxLayout()

        #Верхняю линия
        hbox.addWidget(btn_expand)
        hbox.addStretch(1)
        hbox.addWidget(btn_cut)

        #Вертикальтая линия
        vbox2.addWidget(btn_replace)
        vbox2.addWidget(btn_mult)
        vbox2.addWidget(btn_add)
        vbox2.addWidget(btn_sub)

        hbox2.addStretch(1)
        hbox2.addLayout(vbox2)
        hbox2.addStretch(1)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def expand(self):
        if -1 == self.window.matrixs.expand():
            return
        for i in range(1, 26):
            if self.window.matrixs.rang == 3:
                if i >= 14 or i in [4, 5, 9, 10]:
                    continue
            if self.window.matrixs.rang == 2:
                if i not in [1, 2, 6, 7]:
                    continue
            if self.window.matrixs.rang == 4:
                if i >= 20 or i in [5, 10, 15, 20]:
                    continue
            self.window.matrix1.children()[1].children()[i].show()
            self.window.matrix2.children()[1].children()[i].show()
            self.window.res.children()[0].children()[i].show()

        self.window.matrix1.det, self.window.matrix2.det = self.window.matrixs.det()
        self.window.matrix1.make_det()
        self.window.matrix2.make_det()

    def cut(self):
        if -1 == self.window.matrixs.cut():
            return
        for i in range(1, 26):
            if self.window.matrixs.rang == 3:
                if i < 14 and i not in [4, 5, 9, 10]:
                    continue
            if self.window.matrixs.rang == 2:
                if i in [1, 2, 6, 7]:
                    continue
            if self.window.matrixs.rang == 4:
                if i < 20 and i not in [5, 10, 15, 20]:
                    continue
            self.window.matrix1.children()[1].children()[i].setText('')
            self.window.matrix2.children()[1].children()[i].setText('')
            self.window.matrix1.children()[1].children()[i].hide()
            self.window.matrix2.children()[1].children()[i].hide()
            self.window.res.children()[0].children()[i].setText('')
            self.window.res.children()[0].children()[i].hide()

        self.window.matrix1.det, self.window.matrix2.det = self.window.matrixs.det()
        self.window.matrix1.make_det()
        self.window.matrix2.make_det()
        

    def add(self):
        res = self.window.matrixs.add()
        self.to_res(res)


    def sub(self):
        res = self.window.matrixs.sub()
        self.to_res(res)


    def mult(self):
        res = self.window.matrixs.mult()
        self.to_res(res)


    def to_res(self, res):
        for i in range(self.window.matrixs.rang):
            for j in range(self.window.matrixs.rang):
                self.window.res.children()[0].children()[5*i+j+1].setText(str(res[i][j]))


    def replace(self):
        self.window.matrixs.replace()
        for i in range(self.window.matrixs.rang):
            for j in range(self.window.matrixs.rang):
                self.window.matrix1.children()[1].children()[5*i+j+1].setText(str(self.window.matrixs.matrix1[i][j]))
                self.window.matrix2.children()[1].children()[5*i+j+1].setText(str(self.window.matrixs.matrix2[i][j]))
                self.window.matrix1.det, self.window.matrix2.det = self.window.matrixs.det()
                self.window.matrix1.make_det()
                self.window.matrix2.make_det()



