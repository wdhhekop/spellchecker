#Поиск ошибок в словаре
from src.utils import word_dict
from FBTrie import FBTrie

correct_words = set()
with open('russian.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.strip()
        correct_words.add(word)


def find_closest_word(word, correct_words, fb_trie):
    closest_word = None
    min_distance = float('inf')

    results = fb_trie.levenshtein_search(word, 2)  # Ищем слова с расстоянием Левенштейна не больше 2

    for result_word, distance in results:
        if result_word in correct_words and distance < min_distance:
            closest_word = result_word
            min_distance = distance

    return closest_word


fb_trie = FBTrie()
for word in correct_words:
    fb_trie.insert(word)

#Проверка орфографии и поиск наиболее похожего слова
for key in word_dict:
    if key not in correct_words:
        closest_word = find_closest_word(key, correct_words, fb_trie)
        print(f"Ошибка в слове '{key}'.")
        if closest_word:
            print(f"Возможно, вы имели в виду '{closest_word}'")
        else:
            print("Похожее слово не найдено.")