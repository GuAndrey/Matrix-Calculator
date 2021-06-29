from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Input(QWidget):
    def __init__(self, number, window):
        super().__init__()
        self.number = number
        self.window = window
        self.elems = []
        self.initUI()

     
    def initUI(self):
        self.setFixedSize(377, 314)
        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold")
        font.setPointSize(14)

        #Кнопка очистить
        btn_clear = QPushButton(self)
        btn_clear.setGeometry(QRect(0,0, 123, 37))
        btn_clear.setText("ОЧИСТИТЬ")
        btn_clear.setFont(font)
        btn_clear.setStyleSheet('''QPushButton {  color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_clear.clicked.connect(self.clear)

        #Определитеть
        self.det = '0.0'
        font.setFamily(u"Bahnschrift Light")

        #Ввод матрицы
        input_box = QWidget(self)
        input_box.setGeometry(QRect(0, 40, 377, 178))
        input_box.setStyleSheet('background-color: rgb(104, 101, 255);')
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addStretch(1)
        for i in range(5):
            gbox = QHBoxLayout()
            gbox.addStretch(1)
            for j in range(5):
                inp = NewLineEdit(self.number, i, j, self.window)
                inp.setFixedSize(70,30)
                inp.setFont(font)
                inp.setPlaceholderText('0')
                inp.setStyleSheet(u"background-color: rgb(255, 255, 255); border: 0px;")
                inp.setValidator(QRegExpValidator(QRegExp("^([1-9-][0-9]*|0)(\\.)[0-9]{21}")))
                self.elems.append(inp)
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
        btn_inv = QPushButton(self)
        btn_inv.setGeometry(QRect(0,233, 154, 37))
        btn_inv.setText("Обратная матрица")
        btn_inv.setFont(font)
        btn_inv.setStyleSheet('''QPushButton {  color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_inv.clicked.connect(self.inv)

        #Кнопка транспонирования
        btn_inv = QPushButton(self)
        btn_inv.setGeometry(QRect(0,278, 154, 37))
        btn_inv.setText("Транспонировать")
        btn_inv.setFont(font)
        btn_inv.setStyleSheet('''QPushButton { color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        btn_inv.clicked.connect(self.trans)

        #Кнопка умножить на
        btn_mult = QPushButton(self)
        btn_mult.setGeometry(QRect(222,233, 154, 37))
        btn_mult.setText("Умножить на")
        btn_mult.setFont(font)
        btn_mult.setStyleSheet('''QPushButton { padding:10px; text-align: left; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        inp_mult = QLineEdit(btn_mult)
        inp_mult.setFixedSize(31,25)
        inp_mult.move(117,6)
        inp_mult.setPlaceholderText('0')
        inp_mult.setValidator(QRegExpValidator(QRegExp("^([1-9-][0-9]*|0)(\\.)[0-9]{10}")))
        inp_mult.setFont(font)
        inp_mult.setStyleSheet(u"background-color: rgb(255, 255, 255); border: 0px;")
        btn_mult.clicked.connect(lambda x: self.mult(inp_mult))

        #Кнопка возвести в степень
        btn_power = QPushButton(self)
        btn_power.setGeometry(QRect(222,278, 154, 37))
        btn_power.setText("В степень")
        btn_power.setFont(font)
        btn_power.setStyleSheet('''QPushButton { padding:10px; text-align: left; color: #FFFFFF; background-color: rgb(104, 101, 255); border: none;} 
            QPushButton:hover{
            background-color: rgb(104, 0, 255);
            effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)
            effect.setOffset(0, 0)
            effect.setBlurRadius(20)
            effect.setColor(QColor(57, 219, 255))
            QPushButton.setGraphicsEffect(effect)}''')
        inp_power = QLineEdit(btn_power)
        inp_power.setFixedSize(31,25)
        inp_power.move(117,6)
        inp_power.setFont(font)
        inp_power.setPlaceholderText('0')
        inp_power.setValidator(QRegExpValidator(QRegExp("^([1-9-][0-9]*|0)")))
        inp_power.setStyleSheet(u"background-color: rgb(255, 255, 255); border: 0px; ")
        btn_power.clicked.connect(lambda x: self.power(inp_power))

        text = "Определитель: "
        det = QLabel(text+self.det,self)
        font = QFont()
        font.setPointSize(12)
        font.setFamily(u"Bahnschrift Light")
        det.setFont(font)
        det.move(140, 10)

    def make_det(self):
        self.children()[-1].hide()
        text = "Определитель: "
        det = QLabel(text+self.det,self)
        font = QFont()
        font.setPointSize(12)
        font.setFamily(u"Bahnschrift Light")
        det.setFont(font)
        det.move(140, 10)
        det.show()


    def clear(self):
        self.det = '0.0'
        self.make_det()
        for i in range(self.window.matrixs.rang):
            for j in range(self.window.matrixs.rang):
                self.children()[1].children()[5*i+j+1].setText('')
                self.window.matrixs.clear(self.number)


    def inv(self):
        res = self.window.matrixs.invers(self.number)
        if res is None:
            return
        self.to_res(res)


    def trans(self):
        res = self.window.matrixs.trans(self.number)
        if res is None:
            return
        self.to_res(res)


    def power(self, lineEdit):
        x = lineEdit.text()
        if x == "" or x == '-':
            x = 0
        x = int(x)
        res = self.window.matrixs.power(self.number,x)
        if res is None:
            return
        self.to_res(res)


    def mult(self, lineEdit):
        x = lineEdit.text()
        if x == "" or x == '-':
            x = 0
        x = float(x)
        res = self.window.matrixs.mult_by(self.number,x)
        if res is None:
            return
        self.to_res(res)

    
    def to_res(self, res):
        for i in range(self.window.matrixs.rang):
            for j in range(self.window.matrixs.rang):
                self.window.res.children()[0].children()[5*i+j+1].setText(str(res[i][j]))  


class NewLineEdit(QLineEdit):
    def __init__(self, number, x, y, window):
        super().__init__()
        self.x = x
        self.y = y
        self.window = window
        self.number = number

    def focusOutEvent(self, e):
        super().focusOutEvent(e)
        text = self.text()
        if text == "" or text == '-':
            text = 0
        else:
            try:
                text = float(text)
            except ValueError:
                text = 0
        if self.number == 1:
            self.window.matrixs.matrix1[self.x, self.y] = text
            self.window.matrix1.det = str(self.window.matrixs.det()[0])
            self.window.matrix1.make_det()
        else:
            self.window.matrixs.matrix2[self.x, self.y] = text
            self.window.matrix2.det = str(self.window.matrixs.det()[1])
            self.window.matrix2.make_det()
