# Основной модуль с логикой проверки орфографии
import re


def preprocess_text(text):
    """
    Функция для предварительной обработки текста.
    Удаляет знаки пунктуации, цифры и приводит текст к нижнему регистру.
    """
    text = text.lower()  # Приведение к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text)  # Удаление пунктуации
    text = re.sub(r'[0-9]+', '', text)  # Удаление цифр
    text = re.sub(r'_', '', text)  # Удаление подчеркиваний
    return text


def tokenize(text):
    """
    Функция для разбиения текста на слова (токены).
    """
    tokens = text.split()
    return tokens


def build_vocabulary(tokens):
    """
    Функция для построения словаря из списка токенов.
    Возвращает множество уникальных слов.
    """
    vocabulary = set(tokens)
    return vocabulary


# Пример списка стоп-слов на русском языке
stop_words = ['и', 'в', 'на', 'с', 'как', 'а', 'что', 'это', 'так', 'или', 'но', 'он', 'она', 'они', 'мы', 'ты', 'я',
              'ее', 'их', 'вы']

# Тестовый корпус текстов на русском языке
corpus = ""

# Предобработка текста
preprocessed_text = preprocess_text(corpus)

# Токенизация
tokens = tokenize(preprocessed_text)

# Удаление стоп-слов
tokens = [token for token in tokens if token not in stop_words]

# Построение словаря
vocabulary = build_vocabulary(tokens)

print(vocabulary)
