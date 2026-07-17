"""
Matrix Calculator Backend
Created by Deb

Core matrix operations used by Flask.
"""


# -------------------------------------------------
# Helper Functions
# -------------------------------------------------

def same_size(A, B):
    return len(A) == len(B) and len(A[0]) == len(B[0])


def is_square(matrix):
    return len(matrix) == len(matrix[0])


# -------------------------------------------------
# Matrix Addition
# -------------------------------------------------

def add(A, B):

    if not same_size(A, B):
        return None, "Addition not possible. Matrix dimensions must match."

    result = []

    rows = len(A)
    cols = len(A[0])

    for i in range(rows):

        row = []

        for j in range(cols):

            row.append(A[i][j] + B[i][j])

        result.append(row)

    return result, None


# -------------------------------------------------
# Matrix Subtraction
# -------------------------------------------------

def subtract(A, B):

    if not same_size(A, B):
        return None, "Subtraction not possible. Matrix dimensions must match."

    result = []

    rows = len(A)
    cols = len(A[0])

    for i in range(rows):

        row = []

        for j in range(cols):

            row.append(A[i][j] - B[i][j])

        result.append(row)

    return result, None


# -------------------------------------------------
# Matrix Multiplication
# -------------------------------------------------

def multiply(A, B):

    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        return None, "Columns of Matrix A must equal rows of Matrix B."

    result = []

    for i in range(rowsA):

        row = []

        for j in range(colsB):

            total = 0

            for k in range(colsA):

                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result, None
# -------------------------------------------------
# Determinant
# -------------------------------------------------

def determinant(matrix):

    if not is_square(matrix):
        return None

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    for c in range(n):

        minor = []

        for row in matrix[1:]:

            minor.append(
                row[:c] + row[c + 1:]
            )

        sign = (-1) ** c

        det += sign * matrix[0][c] * determinant(minor)

    return det
# -------------------------------------------------
# Matrix Inverse
# -------------------------------------------------

def inverse(matrix):

    if not is_square(matrix):
        return None, "Matrix must be square."

    n = len(matrix)

    det = determinant(matrix)

    if det == 0:
        return None, "Inverse does not exist because the determinant is zero."

    if n == 1:
        return [[1 / det]], None

    cofactors = []

    for i in range(n):

        cofactor_row = []

        for j in range(n):

            minor = []

            for row in (matrix[:i] + matrix[i + 1:]):
                minor.append(row[:j] + row[j + 1:])

            cofactor = ((-1) ** (i + j)) * determinant(minor)

            cofactor_row.append(cofactor)

        cofactors.append(cofactor_row)

    adjugate = []

    for i in range(n):

        row = []

        for j in range(n):

            row.append(cofactors[j][i])

        adjugate.append(row)

    inverse_matrix = []

    for i in range(n):

        row = []

        for j in range(n):

            row.append(adjugate[i][j] / det)

        inverse_matrix.append(row)

    return inverse_matrix, None