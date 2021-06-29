from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Result(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.initUI()

    def initUI(self):
        self.setFixedSize(878, 236)
        font = QFont()
        font.setFamily(u"Bahnschrift Light")
        font.setPointSize(14)            

        #Поле вывода
        input_box = QWidget(self)
        input_box.setGeometry(QRect(0, 0, 878, 178))
        input_box.setStyleSheet('background-color: rgb(104, 101, 255);')
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addStretch(1)
        for i in range(5):
            gbox = QHBoxLayout()
            gbox.addStretch(1)
            for j in range(5):
                inp = QLineEdit()
                inp.setMinimumSize(70,30)
                inp.setFont(font)
                inp.setReadOnly(True)
                inp.setStyleSheet(u"background-color: rgb(255, 255, 255); border: 0px;")
                gbox.addWidget(inp)
                gbox.addStretch(1)
            gbox.addStretch(1)
            vbox.addLayout(gbox)
        vbox.addStretch(1)
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        input_box.setLayout(hbox)

        #Кнопка обратной матрицы
        font.setPointSize(12)
        btn_left = QPushButton(self)
        btn_left.setGeometry(QRect(250,190, 154, 45))
        btn_left.setText("Записать в левую\n матрицу")
        btn_left.setFont(font)
        btn_left.setStyleSheet('''QPushButton { color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_left.clicked.connect(self.left)

        #Кнопка умножить на
        btn_right = QPushButton(self)
        btn_right.setGeometry(QRect(472,190, 154, 45))
        btn_right.setText("Записать в правую\n матрицу")
        btn_right.setFont(font)
        btn_right.setStyleSheet('''QPushButton { color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_right.clicked.connect(self.right)


    def left(self):
        for i in range(self.window.matrixs.rang):
            for j in range(self.window.matrixs.rang):
                try:
                    self.window.matrixs.matrix1[i][j] = float(self.window.res.children()[0].children()[5*i+j+1].text())
                except ValueError:
                    self.window.matrixs.matrix1[i][j] = 0.0
                self.window.matrix1.children()[1].children()[5*i+j+1].setText(str(self.window.matrixs.matrix1[i][j]))
                self.window.matrix1.det, self.window.matrix2.det = self.window.matrixs.det()
                self.window.matrix1.make_det()



    def right(self):
        for i in range(self.window.matrixs.rang):
            for j in range(self.window.matrixs.rang):
                try:
                    self.window.matrixs.matrix2[i][j] = float(self.window.res.children()[0].children()[5*i+j+1].text())
                except ValueError:
                    self.window.matrixs.matrix2[i][j] = 0.0
                self.window.matrix2.children()[1].children()[5*i+j+1].setText(str(self.window.matrixs.matrix2[i][j]))
                self.window.matrix1.det, self.window.matrix2.det = self.window.matrixs.det()
                self.window.matrix2.make_det()
                