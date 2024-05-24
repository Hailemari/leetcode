# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:

    def __init__(self):
        self.is_end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.is_end = True        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root

            for j in range(i, len(word)):
                char = word[j]
                if char == ".":
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True

                    return False


                else:
                    if char not in cur.children:
                        return False

                    cur = cur.children[char]
            
            return cur.is_end



        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
