class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(curr, i):
            if i == len(word):
                return curr.is_end
            
            char = word[i]

            if char == ".":
                for child in curr.children.values():
                    if dfs(child, i+1):
                        return True
                return False

            if char not in curr.children:
                return False
            
            return dfs(curr.children[char], i+1)

        return dfs(self, 0)
