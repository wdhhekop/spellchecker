import unittest
from src.spellchecker import check_spelling


class TestSpellChecker(unittest.TestCase):
    def test_known_word(self):
        # Тест проверяет корректность проверки известного слова.
        self.assertEqual(check_spelling("привет"), None)

    def test_hyphenated_word(self):
        # Тест проверяет корректность проверки слов с дефисом.
        self.assertEqual(check_spelling("само-уважение"), None)

    def test_empty_input(self):
        # Тест проверяет обработку пустого ввода.
        self.assertEqual(check_spelling(""), None)


if __name__ == '__main__':
    unittest.main()
