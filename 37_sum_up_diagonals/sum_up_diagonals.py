def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    diag_top_bot = 0
    diag_bot_top = 0

    for x in range(0, len(matrix)):
        diag_top_bot += matrix[x][x]
        diag_bot_top += matrix[x][len(matrix) - (x+1)]

    return diag_bot_top + diag_top_bot