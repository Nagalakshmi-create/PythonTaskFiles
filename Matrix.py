import numpy as np


class Matrix:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def addition(self):
        result = np.add(self.matrix1, self.matrix2)
        print(result)
    
    def subtraction(self):
        result = np.subtract(self.matrix1, self.matrix2)
        print(result)
    
    def multiplication(self):
        result = np.dot(self.matrix1, self.matrix2)
        print(result)

    def transposes(self):
        print(self.matrix1.transpose())
        print(self.matrix2.transpose())


class Childs(Matrix):
    def __init__(self, matrix1, matrix2):
        super().__init__(matrix1, matrix2)

    def addition(self):
        result = [([(matrix1[i][j] + matrix2[i][j]) for j in range(len(matrix1[0]))]) for i in range(len(matrix1))]
        print("Addition of two matrices is: \n"+str(result))

    def subtraction(self):
        result = [([(matrix1[i][j] - matrix2[i][j]) for j in range(len(matrix1[0]))]) for i in range(len(matrix1))]
        print("Subtraction of two matrices is: \n"+str(result))

    def multiplication(self):
        result= [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
        print("Multiplication of two matrices is: \n"+str(result))

    def transposes(self):
        result1 = [([matrix1[j][i] for j in range(len(matrix1))]) for i in range(len(matrix1[0]))]
        print("Transpose of first matrix is: \n"+str(result1))

        result2 = [([matrix2[j][i] for j in range(len(matrix2))]) for i in range(len(matrix2[0]))]
        print("Transpose of second matrix is: \n"+str(result2))


matrix1 = np.array([[4, 5], [2,1]])
matrix2 = np.array([[8, 4], [3,2]])


#obj = Matrix(matrix1, matrix2)
#obj.addition()
#obj.substraction()
#obj.multiplication()
#obj.transposes()


obj1 = Childs(matrix1, matrix2)
obj1.addition()
obj1.subtraction()
obj1.multiplication()
obj1.transposes()