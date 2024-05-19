def levenshtein_distance(word_1, word_2):
    n, m = len(word_1), len(word_2)
    if n > m:
        word_1, word_2 = word_2, word_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if word_1[j - 1] != word_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]