#реализация структуры данных FB-Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class FuzzyBoundedTrie:
    def __init__(self, max_distance):
        self.root = TrieNode()
        self.max_distance = max_distance

    def levenshtein_distance(self, word1, word2):
        n, m = len(word1), len(word2)
        if n > m:
            word1, word2 = word2, word1
            n, m = m, n

        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if word1[j - 1] != word2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    def search(self, word):
        results = []

        def dfs(node, prefix, remaining_dist):
            if node.word is not None and self.levenshtein_distance(node.word, word) <= remaining_dist:
                results.append(prefix + node.word)

            for char, child in node.children.items():
                dist = remaining_dist
                if node.word is not None and node.word[-1] != char:
                    dist -= 1
                if dist >= 0:
                    dfs(child, prefix + char, dist)

        dfs(self.root, "", self.max_distance)
        return results