class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value=None):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = value

    def words(self):
        def collect_words(node, prefix, words):
            if node.is_end:
                words.append(prefix)
            for char, child in node.children.items():
                collect_words(child, prefix + char, words)
        result = []
        collect_words(self.root, "", result)
        return result