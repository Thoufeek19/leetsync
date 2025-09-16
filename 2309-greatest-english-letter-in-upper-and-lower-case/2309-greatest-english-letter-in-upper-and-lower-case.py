class Solution:
    def greatestLetter(self, s: str) -> str:
        letters=set(s)
        for i in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if i in letters and i.lower() in letters:
                return i.upper()
        return ""
        