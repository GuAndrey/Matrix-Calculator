import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from input_matrix import *
from operate import *
from result import *
from calculat.calculater import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWin(QWidget):

    def __init__(self):
        super().__init__()
        self.matrixs = Calculater()
        self.initUI()
        self.initRule()
        

    def initUI(self):
        #Инициализация окна приложения 
        self.main = QWidget(self)
        self.main.setStyleSheet(u"background-color: rgb(255, 255, 255);\n border-color: rgb(104, 101, 255);")
        self.main.setGeometry(QRect(5,5,912,620))
        font = QFont()
        self.mouseEvent = False
        
        #Определение путей для изображений
        imageDir = os.path.dirname(os.path.realpath(__file__)).replace('interface', 'image') +  os.path.sep 
        self.exit_path = imageDir + 'exit.png'
        self.turn_path = imageDir + 'turn.png'
        print(self.exit_path)

        #Инициализация вверхней линии
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.upline = QWidget(self.main)
        self.upline.setGeometry(QRect(0, 0, 912, 25))
        self.upline.setStyleSheet(u"background-color: rgb(104, 101, 255);")
        self.name = QLabel('Matrix', self.upline)
        font.setFamily(u"Franklin Gothic Demi")
        font.setPointSize(12)
        self.name.setGeometry(QRect(17, 0, 500, 25))
        self.name.setFont(font)
        self.name.setStyleSheet("QLabel { color: #FFFFFF;}")

        #Кнопка выхода
        exitbtn = QPushButton(self.upline)
        exitbtn.setGeometry(QRect(912-25, 0, 25, 25))
        exitbtn.setIcon(QIcon(self.exit_path))
        exitbtn.setStyleSheet("icon-size: 25px;")
        exitbtn.clicked.connect(self.close)

        #Кнопка сворачивания
        turnbtn = QPushButton(self.upline)
        turnbtn.setGeometry(QRect(912-50, 0, 25, 25))
        turnbtn.setIcon(QIcon(self.turn_path))
        turnbtn.setStyleSheet("icon-size: 25px;")
        turnbtn.clicked.connect(self.showMinimized)

        #Тень
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0) 
        self.main.setGraphicsEffect(shadowEffect)   

        #Размер окна с тенью
        self.setMinimumSize(QSize(922, 630))
        self.setMaximumSize(QSize(922, 630))
        self.setGeometry(300, 300, 922, 630)

        #Поле ввода
        self.matrix1 = Input(1, self)
        self.matrix1.setParent(self)
        self.matrix1.move(28,39)

        self.matrix2 = Input(2, self)
        self.matrix2.setParent(self)
        self.matrix2.move(529,39)

        #Кнопки действий над двумя функциями
        oper = Operate(self)
        oper.setParent(self)
        oper.move(405, 39)

        #Поле результата
        self.res = Result(self)
        self.res.setParent(self)
        self.res.move(28, 376)

        #Кнопка инструкции
        rule = QPushButton(self)
        rule.setGeometry(QRect(755,565, 154, 45))
        rule.setText("Инструкция")
        rule.setFont(font)
        rule.setStyleSheet('''QPushButton { color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        rule.clicked.connect(self.to_rule)

        self.show()
    
    def initRule(self):
        self.rule = QWidget(self)
        self.rule.setStyleSheet(u"background-color: rgb(255, 255, 255);\n border-color: rgb(104, 101, 255);")
        self.rule.setGeometry(QRect(5,30,912,595))
        font = QFont()

        #Верхний текст
        lblins = QLabel('Инструкция:')
        font.setFamily(u"Bahnschrift Light")
        font.setPointSize(24)
        lblins.setFont(font)
        lblins.setAlignment(Qt.AlignCenter)

        
        #Приветственный текст
        text = '''Данная программа представляет собой матричный калькулятор, в котором Вы можете складывать, умножать, вычитать матрицы с размером 2х2, 3х3, 4х4, 5х5.

            Также для перечисленных матриц Вы можете найти их обратные матрицы, транспонировать, умножить на скаляр или возвести в степень.

            Для выполнения той или иной операции необходимо ввести матрицы в поле ввода и нажать на кнопку с соответствующей операцией.

            Для увеличения или уменьшения ранга матриц необходимо нажать на плюс в кружке или минус в кружке соответственно.

            Если калькулятор не выполнил Ваше действие, значит, Вы запрашиваете некорректное действие. Проверти введенные данные ещё раз.
                '''.replace('''    ''', '')


        lbltext = QLabel(text)
        font.setPointSize(14)
        lbltext.setFont(font)
        lbltext.setWordWrap(True)
        lbltext.setStyleSheet("margin: 10px")

        #Размещение
        hbox = QHBoxLayout()  
        vbox = QVBoxLayout()

        vbox.addWidget(lblins)
        vbox.addWidget(lbltext)
        vbox.addStretch(1)

        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        self.rule.setLayout(hbox)

        #Кнопка назад
        font.setFamily(u"Franklin Gothic Demi")
        font.setPointSize(12)
        rule = QPushButton(self.rule)
        rule.setGeometry(QRect(750,535, 154, 45))
        rule.setText("Назад")
        rule.setFont(font)
        rule.setStyleSheet('''QPushButton { color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        rule.clicked.connect(self.to_back)

    def to_rule(self):
        self.rule.show()

    def to_back(self):
        self.rule.hide()

    prev_mous_mos = [0, 0]

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            pos = e.screenPos()
            x_m = pos.x()
            y_m = pos.y()
            x = self.pos().x()
            y = self.pos().y()
            if (x_m - x < 917 and x_m - x > 4) and \
                    (y_m - y < 30 and y_m -y > 4):
                    self.prev_mous_mos[0] = x_m
                    self.prev_mous_mos[1] = y_m
                    self.mouseEvent = True

    def mouseReleaseEvent(self, e):
        self.mouseEvent = False

    def mouseMoveEvent(self, e):
        if self.mouseEvent:
            pos = e.screenPos()
            x = self.pos().x()
            y = self.pos().y()
            x_m = pos.x()
            y_m = pos.y()
            dx = x_m - self.prev_mous_mos[0]
            dy = y_m - self.prev_mous_mos[1]
            self.move(x+dx,y+dy)
            self.prev_mous_mos[0] = x_m
            self.prev_mous_mos[1] = y_m




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWin()
    sys.exit(app.exec_()) 