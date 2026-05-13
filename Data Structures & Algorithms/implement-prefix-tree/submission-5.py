class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixTree()
            cur = cur.children[c]
        cur.is_end = True # finished with all char in word

    def search(self, word: str) -> bool:
        cur = self
        # im attempting to check for every is_end until we get either True at the end or false
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True        
        