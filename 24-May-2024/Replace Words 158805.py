# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:

    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.is_end = True

    def get_prefix(self, word):
        cur = self.root
        res = ""
        for char in word:
            if cur.is_end:
                break
            if char not in cur.children:
                break
            res += char

            cur = cur.children[char]

        return res if cur.is_end else ""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence_list = sentence.split(' ')
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)

        ans = ""
        for successor in sentence_list:
            root_word = trie.get_prefix(successor)
            if root_word:
                ans += (root_word + " ")
            else:
                ans += (successor + " ")

        return ans[:-1]




        
        



