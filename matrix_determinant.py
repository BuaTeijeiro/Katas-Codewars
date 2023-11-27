def get_minor(matrix, row= 0, column = 0):
    new_matrix = []
    for i in range(len(matrix)):
        if i != row:
            new_matrix.append(matrix[i][:column] + matrix[i][column + 1:])
    return new_matrix

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        suma = 0
        for index, number in enumerate(matrix[0]):
            sign = -2 * (index % 2) + 1
            minor = get_minor(matrix, column = index)
            suma += sign * number * determinant(minor)
        return suma