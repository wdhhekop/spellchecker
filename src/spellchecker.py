import json

from src.utils import dictionary


def save_dictionary(dictionary, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)


save_dictionary(dictionary, "dictionary.json")
