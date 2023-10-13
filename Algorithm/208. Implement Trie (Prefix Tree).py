'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''

class Trie:

    class TrieNode:
        def __init__(self):
            self.children=[None for _ in range(26)]
            self.isWord=False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not node.children[index]:
                node.children[index] = self.TrieNode()
            
            node = node.children[index]
        node.isWord=True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not node.children[index]: return False
            node = node.children[index]
        return node.isWord            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            index = ord(c) - ord("a")
            if not node.children[index]: return False
            node = node.children[index]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)