class TrieNode:
    def __init__(self):
        self.children = {}      # map from char → TrieNode
        self.words = []         # store original words that end at this node
        self.is_end = False     # marks end of a key


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert sorted key and store the original word
    def insert(self, sorted_word, original_word):
        node = self.root
        for ch in sorted_word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.words.append(original_word)

    # DFS to collect all grouped words
    def collect_groups(self):
        result = []

        def dfs(node):
            if node.is_end:
                result.append(node.words[:])  # copy list to avoid reference issues
            for child in node.children.values():
                dfs(child)

        dfs(self.root)
        return result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trie = Trie()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            trie.insert(sorted_word, word)
        return trie.collect_groups()