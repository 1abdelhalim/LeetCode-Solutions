class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word 
    return root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = build_trie(words)
        result = []
        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            char = board[i][j]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  

            board[i][j] = "#" 
            for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(ni, nj, next_node)
            board[i][j] = char 

            if not next_node.children:
                del node.children[char]

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return result