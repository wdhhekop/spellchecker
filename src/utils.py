import json


# Утилита построения словаря по корпусу текстов
# Вырезаем только слова
def clean_word(word):
    return ''.join(filter(str.isalpha, word))


# Построение словаря по тексту
def build_word_dict(text):
    word_dict = {}
    words = text.lower().split()
    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word:
            if cleaned_word in word_dict:
                word_dict[cleaned_word].add(word)
            else:
                word_dict[cleaned_word] = {word}
    # Преобразование множеств в списки
    for key in word_dict:
        word_dict[key] = list(word_dict[key])
    return word_dict


# Чтение текстового файла и построение словаря
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

word_dict = build_word_dict(text)

# Сохранение словаря в файл corpus.json
with open('corpus.json', 'w', encoding='utf-8') as json_file:
    json.dump(word_dict, json_file, ensure_ascii=False, indent=4)

print('Словарь успешно построен и сохранен в файле corpus.json.')
