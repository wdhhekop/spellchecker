#реализация структуры данных FB-Trie
from src.levenshtein_distance import levenshtein_distance


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None


class FBTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def levenshtein_search(self, word, max_distance):
        results = []

        def levenshtein_traverse(node, current_word, distance):
            if node.is_end_of_word and abs(len(current_word) - len(word)) <= max_distance:
                distance += levenshtein_distance(current_word, word)
                if distance <= max_distance:
                    results.append((node.word, distance))

            for char, child_node in node.children.items():
                new_word = current_word + char
                new_distance = distance + 1
                if char != word[len(current_word)]:
                    new_distance += 1

                if new_distance <= max_distance or len(new_word) < len(word):
                    levenshtein_traverse(child_node, new_word, new_distance)

        levenshtein_traverse(self.root, "", 0)
        return results
