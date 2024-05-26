#тесты на проверку утилиты подсчёта расстояния Дамера - Левенштейна
import unittest
from src.damerau_levenshtein_distance import damerau_levenshtein_distance


class TestSpellChecker(unittest.TestCase):
    # расстояние между двумя пустыми строками равно 0
    def test_empty_strings(self):
        self.assertEqual(damerau_levenshtein_distance("", ""), 0)

    # тест на расстояние между строками разной длины
    def test_strings_of_different_lengths(self):
        self.assertEqual(damerau_levenshtein_distance("кошка", "кот"), 3)
        self.assertEqual(damerau_levenshtein_distance("дом", "домик"), 2)

    #подсчёт расстояния между строками с разными символами
    def test_strings_with_different_characters(self):
        self.assertEqual(damerau_levenshtein_distance("собака", "кот"), 5)
        self.assertEqual(damerau_levenshtein_distance("дом", "дождь"), 3)

    #проверка строкк, отличающихся только регистром
    def test_strings_with_different_case(self):
        self.assertEqual(damerau_levenshtein_distance("Кот", "кот"), 1)
        self.assertEqual(damerau_levenshtein_distance("ДОМ", "дом"), 3)


if __name__ == '__main__':
    unittest.main()
