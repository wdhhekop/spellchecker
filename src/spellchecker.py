from src.utils import spell_check_text

dictionary = {"это", "пример", "текста", "который", "мы", "хотим", "проверить", "на", "орфографию"}

text = "Это пример тек ттста, который мы хотим провериироть на орфографию."

corrected_text = spell_check_text(text, dictionary)
print(corrected_text)
