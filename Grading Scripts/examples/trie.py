class TrieNode:
    def __init__(self):
        self.freq = 0
        self.children = {}

    def add(self, word):
        print(word)
        if len(word) == 0:
            self.freq += 1
        else:
            c = word[0]

            if c not in self.children:
                self.children[c] = TrieNode()

            self.children[c].add(word[1:])

    def find(self, word):
        if len(word) == 0:
            return self.freq
        else:
            c = word[0]

            if c not in self.children:
                return 0

            return self.children[c].find(word[1:])

trie = TrieNode()
trie.add("hello")
trie.add("bye")
print(trie.find("bye"))
