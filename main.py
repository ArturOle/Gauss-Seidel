from Gauss_Siedel import GaussSeidel

if __name__ == "__main__":
    matrix_a = [[16, 3], [7, -11]]
    vector_b = [[11], [13]]

    GaussSeidel.from_lists(matrix_a, vector_b, 4)



