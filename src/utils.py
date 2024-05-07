# утилита, которая строит словарь по корпусу текстов
# утилита реализует подсчёт расстояния Левенштейна, находит наиболее похожее слово в словаре, исправляет неправильные слова
import re
import json
from collections import Counter

stop_words = {"и", "в", "на", "с", "к", "как", "так", "это", "по", "но", "что", "он", "она", "они", "мы", "вы", "ты"}


def build_dictionary(text_files, min_word_freq=2):
    word_freq = Counter()
    for file_path in text_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                words = re.findall(r'\w+', text)
                words_filtered = [word for word in words if word not in stop_words]
                word_freq.update(words_filtered)
        except IOError as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
    return {word: freq for word, freq in word_freq.items() if freq >= min_word_freq}


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1
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
        closest_word = find_closest_word(word, dictionary)
        if word != closest_word:
            corrected_word = f"[{closest_word}]"
        else:
            corrected_word = word
        corrected_words.append(corrected_word)
    return ' '.join(corrected_words)


# вывод слов с ошибками
def find_misspelled_words(text, dictionary):
    words = text.split()
    misspelled_words = {}

    for word in words:
        if word not in dictionary:
            misspelled_words[word] = float('inf')
            for dict_word in dictionary:
                distance = levenshtein_distance(word, dict_word)
                if distance < misspelled_words[word]:
                    misspelled_words[word] = distance
    min_error_value = min(misspelled_words.values())
    incorrect_words = [word for word, value in misspelled_words.items() if value == min_error_value]
    incorrect_sentence = ' '.join(incorrect_words)

    print(f"Орфографически неверные слова: {incorrect_sentence}")


def save_dictionary(dictionary, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении файла {file_path}: {e}")


text_files = ["text.txt"]
with open('text.txt', 'r', encoding='utf-8') as file:
        text_to_check = file.read()
dictionary = build_dictionary(text_files)
save_dictionary(dictionary, "dictionary.json")
find_misspelled_words(text_to_check.lower(), dictionary)
