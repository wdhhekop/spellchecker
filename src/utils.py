#Утилита построения словаря по корпусу текстов
def clean_word(word):
    return ''.join(filter(str.isalpha, word))


with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#Построение словаря по тексту
word_dict = {}

words = text.lower().split()
for word in words:
    cleaned_word = clean_word(word)
    if cleaned_word:
        if cleaned_word in word_dict:
            word_dict[cleaned_word].add(word)
        else:
            word_dict[cleaned_word] = {word}

#Преобразование множеств в списки
for key in word_dict:
    word_dict[key] = list(word_dict[key])

#Сохранение словаря в файл dictionary.json
import json

with open('dictionary.json', 'w', encoding='utf-8') as json_file:
    json.dump(word_dict, json_file, ensure_ascii=False, indent=4)

print('Словарь успешно построен и сохранен в файле dictionary.json.')

