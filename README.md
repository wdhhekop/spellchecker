# Спеллчекер.

***
Проверка орфографии: подсчёт расстояния Дамера-Левенштейна, вывод некорректно написанных слов 
с возможными исправлениями.

Примечания
----------
- Скрипт выводит 10 похожих слов из словаря на основе расстояния Дамера-Левенштейна с пороговым значением 2.
- Если для слова не найдено похожих слов, скрипт сообщит об этом.

Использование
-----------
В текстовом файле text.txt напишите текст, который необходимо проверить на орфографию.

Достаточно запустить main.
```commandline
python main.py
```

Комманда для построения словаря по корпусу текста:
```commandline
python utils.py
```
Утилита проверки орфографии:
```commandline
python spellchecker.py
```
