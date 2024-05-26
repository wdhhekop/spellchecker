import json
from src.damerau_levenshtein_distance import damerau_levenshtein_distance


def check_spelling():
    with open('dictionary.json', 'r', encoding='utf-8') as file:
        correct_words = set(json.load(file))

    with open('corpus.json', 'r', encoding='utf-8') as file:
        text_words = set(json.load(file))

    printed_similar_words = set()  # Множество для хранения похожих слов
    count = 0  # Счетчик для отслеживания количества выведенных предложений
    for word in text_words:
        if word not in correct_words:
            closest_words = [correct_word for correct_word in correct_words if
                             damerau_levenshtein_distance(word, correct_word.replace('-', '').upper()) <= 2]
            if closest_words:
                print(f"Ошибка в слове '{word}'. Возможно, вы имели в виду:")
                for closest_word in closest_words:
                    if closest_word not in printed_similar_words:
                        print(f"- {closest_word}")
                        printed_similar_words.add(closest_word)
                        count += 1
                        if count == 5:
                            break
            else:
                print(f"Ошибка в слове '{word}'. Похожие слова не найдены.")

            if count == 5:
                break
