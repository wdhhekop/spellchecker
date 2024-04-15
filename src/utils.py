#утилита реализует подсчёт расстояния Левенштейна, находит наиболее похожее слово в словаре, исправляет неправильные слова
import re


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'[0-9]+', '', text)
    return text


def find_closest_word(word, dictionary):
    min_distance = float('inf')
    closest_word = None
    for dict_word in dictionary:
        distance = levenshtein_distance(word, dict_word)
        if distance < min_distance:
            min_distance = distance
            closest_word = dict_word
    return closest_word


def spell_check_text(text, dictionary):
    preprocessed_text = preprocess_text(text)
    words = preprocessed_text.split()
    corrected_words = []
    for word in words:
        corrected_word = find_closest_word(word, dictionary)
        corrected_words.append(corrected_word)
    return ' '.join(corrected_words)

