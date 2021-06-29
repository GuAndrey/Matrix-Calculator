import numpy as np

class Calculater():

    def __init__(self):
        self.matrix1 = np.zeros((5,5))
        self.matrix2 = np.zeros((5,5))
        self.rang = 5


    def expand(self):
        '''
        Функция увеличивает ранг матриц на 1
        '''
        if self.rang == 5:
            return -1
        self.rang+=1
        new = np.zeros((self.rang,self.rang))
        new[:self.rang-1,:self.rang-1] = self.matrix1
        self.matrix1 = new.copy()
        new[:self.rang-1,:self.rang-1] = self.matrix2
        self.matrix2 = new.copy()


    def cut(self):
        '''
        Функция уменьшает ранг матриц на 1
        '''
        if self.rang == 2:
            return -1
        self.rang-=1
        self.matrix1 = self.matrix1[:self.rang,:self.rang]
        self.matrix2 = self.matrix2[:self.rang,:self.rang]


    def det(self):
        '''
        Функция возвращает картеж с определителями матриц
        '''
        a = np.linalg.det(self.matrix1)
        b = np.linalg.det(self.matrix2)
        a = round(a, 2)
        b = round(b, 2)
        return (str(a), str(b))

    
    def invers(self, matrix):
        '''
        Функция принимает на вход номер матрицы
        Возвращает обратную матрицу
        При недопустимости операции возвращает None
        '''
        try:
            if matrix == 1:
                inv = np.linalg.inv(self.matrix1)
            else:
                inv = np.linalg.inv(self.matrix2)
        except np.linalg.LinAlgError:
            print("Действие не возможно")
            return
        return inv
        

    def trans(self, matrix):
        '''
        Функция принимает на вход номер матрицы
        Возвращает транспонированную матрицу 
        '''
        if matrix == 1:
            trans = np.transpose(self.matrix1)
        else:
            trans = np.transpose(self.matrix2)
        return trans


    def power(self, matrix, p):
        '''
        Функция принимает на вход номер матрицы и степень
        Возвращает возведенную в степень матрицу
        При недопустимости операции возвращает None
        '''
        try:
            if matrix == 1:
                return np.linalg.matrix_power(self.matrix1, p)
            else:
                return np.linalg.matrix_power(self.matrix2, p)
        except np.linalg.LinAlgError:
            print("Действие не возможно")
            return


    def mult_by(self, matrix, x):
        '''
        Функция принимает на вход номер матрицы и скаляр
        Возвращает умноженную на скаляр степень
        При недопустимости операции возвращает None
        '''
        if matrix == 1:
            return self.matrix1 * x
        else:
            return self.matrix2 * x


    def add(self):
        '''
        Функция складывает матрицы
        '''
        return self.matrix1 + self.matrix2

    
    def sub(self):
        '''
        Функция вычитает матрицы
        '''
        return self.matrix1 - self.matrix2


    def mult(self):
        '''
        Функция умножает матрицы
        '''
        return np.dot(self.matrix1, self.matrix2)


    def replace(self):
        '''
        функция меняет матрицы местами
        '''
        self.matrix1, self.matrix2 = self.matrix2, self.matrix1

    def clear(self, matrix):
        '''
        Функция очищает выбранную матрицу
        '''
        if matrix == 1:
            self.matrix1 = np.zeros((self.rang, self.rang))
        else:
            self.matrix2 = np.zeros((self.rang, self.rang))

    def print(self):
        print(self.matrix1)
        print()
        print(self.matrix2)
        print()


