class Trie:
    def __init__(self):
        self.floor= [[]]
        self.words= {}

    def insert(self, word: str) -> None:
        self.words[word] = True
        for i in range(len(word)):
            if word[i] not in self.floor[i]:
                self.floor[i].append(word[i])
                self.floor.append([])      
    def search(self, word: str) -> bool:
        if word not in self.words: return False
        for i in range(len(word)):
            if word[i] not in self.floor[i]:
                return False
        return True
    def startsWith(self, prefix: str) -> bool:
        cut = len(prefix)
        for i in self.words:
            if i[:cut] == prefix: return True
        return False
                  


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
trie = Trie()
trie.insert("apple");
# print(trie.search("apple")); 
# print(trie.search("app"));
print(trie.startsWith("app"));
# trie.insert("app");
print(trie.search("app"));  