import json
from Levenshtein import distance


# функция, которая проверяет орфографию в тексте по словарю
def check_spelling(text):
    if not text:
        return
    with open('dictionary.json', 'r', encoding='utf-8') as file:
        correct_words = set(json.load(file))
    try:
        with open('corpus.json', 'r', encoding='utf-8') as file:
            text_words = set(json.load(file))
    except json.JSONDecodeError:
        print("Не введено слово или текст для проверки")
        return

    printed_similar_words = set()  # Множество для хранения похожих слов
    count = 0  # Счетчик для отслеживания количества выведенных предложений
    errors_found = False  # Флаг для отслеживания наличия ошибок

    for word in text_words:
        if word not in correct_words:
            errors_found = True
            if '-' in word:
                parts = word.split('-')
                closest_words = []
                for part in parts:
                    closest_words.extend([correct_word for correct_word in correct_words if
                                          distance(part, correct_word) <= 2])
            else:
                closest_words = [correct_word for correct_word in correct_words if
                                 distance(word, correct_word) <= 2]

            if closest_words:
                print(f"Ошибка в слове '{word}'. Возможно, вы имели в виду:")
                for closest_word in closest_words:
                    if closest_word not in printed_similar_words:
                        print(f"- {closest_word}")
                        printed_similar_words.add(closest_word)
                        count += 1
                        if count == 10:
                            break
            else:
                print(f"Ошибка в слове '{word}'. Похожие слова не найдены.")

            if count == 10:
                break

    if not errors_found:
        print("Ошибок не найдено")
