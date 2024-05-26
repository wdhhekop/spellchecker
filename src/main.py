# main
import json
from utils import build_word_dict
from spellchecker import check_spelling


def main():
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    word_dict = build_word_dict(text)

    with open('corpus.json', 'w', encoding='utf-8') as json_file:
        json.dump(word_dict, json_file, ensure_ascii=False, indent=4)

    check_spelling()


if __name__ == '__main__':
    main()
