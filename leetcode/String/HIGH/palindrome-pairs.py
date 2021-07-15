# https://leetcode.com/problems/palindrome-pairs/

class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.palindrome_word_ids = []
        self.children = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]
    
    #단어 삽입
    def insert(self, index, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for i, char in enumerate (reversed(word)):
            if self.is_palindrome(world[0:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
        
    #단어 존재 여부 판별
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
    
    #문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
    
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie = Trie()
        
        for word in words:
            trie.insert(word.reverse)
        
        result = []
        # 체크하고 남은거 return 받아서 펠린드롬인지 확인!! 
        # index 기억해서 보내기, i == j는 없애기..! 
        
        
        