import numpy as np


class GaussSeidel:
    def __init__(self, matrix_a: np.array, vector_b: np.array, num_of_iter: int) -> np.array:
        self.A = matrix_a
        self.b = vector_b
        self.number_of_iterations = num_of_iter
        self.lower_triangular = self.__lower_triangular_matrix()
        self.upper_triangular = self.__upper_triangular_matrix()
        self.describe()
        self.x = self.solve()
        print("Result: \n{}".format(self.x))

    @classmethod
    def from_lists(cls, matrix_a: list, vector_b: list, num_of_iter: int):
        """
        :summary the factory method to handle lists on the input:
        :param matrix_a:
        :param vector_b:
        :param num_of_iter:
        :return:
        """
        matrix_a = np.array(matrix_a)
        vector_b = np.array(vector_b)
        return cls(matrix_a, vector_b, num_of_iter)

    def describe(self):
        print("The matrix: \n{}".format(self.A))
        print("The lower triangular matrix:\n{}".format(self.lower_triangular))
        print("The upper triangular matrix:\n{}".format(self.upper_triangular))

    def __lower_triangular_matrix(self):
        return np.tril(self.A)

    def __upper_triangular_matrix(self):
        upper = np.triu(self.A)
        for i in range(len(upper)):
            upper[i][i] = 0
        return upper

    def solve(self):
        inversed_lower_triangular = np.linalg.inv(self.lower_triangular)
        T = np.matmul(-inversed_lower_triangular, self.upper_triangular)
        C = np.matmul(inversed_lower_triangular, self.b)
        x = np.ones((1, len(self.A)))
        for _ in range(self.number_of_iterations):
            x = x*T + C
            x = x[:, len(self.A)-1]
        return x









