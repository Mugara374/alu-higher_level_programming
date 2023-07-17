#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        result_row = []
        for i in row:
            result_row.append(i**2)
        result_matrix.append(result_row)
    return result_matrix
