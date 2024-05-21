#подсчёт расстояния Дамерау-Левенштейна
def damerau_levenshtein_distance(first_word, second_word):
    n = len(first_word) + 1
    m = len(second_word) + 1
    matrix_d = [[0 for _ in range(m)] for _ in range(n)]

    deletion_cost = 1
    insertion_cost = 1

    for i in range(n):
        matrix_d[i][0] = i

    for j in range(m):
        matrix_d[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            substitution_cost = 0 if first_word[i - 1] == second_word[j - 1] else 1

            matrix_d[i][j] = min(matrix_d[i - 1][j] + deletion_cost,
                                 matrix_d[i][j - 1] + insertion_cost,
                                 matrix_d[i - 1][j - 1] + substitution_cost)

            if i > 1 and j > 1 and first_word[i - 1] == second_word[j - 2] and first_word[i - 2] == second_word[j - 1]:
                matrix_d[i][j] = min(matrix_d[i][j], matrix_d[i - 2][j - 2] + substitution_cost)

    return matrix_d[n - 1][m - 1]