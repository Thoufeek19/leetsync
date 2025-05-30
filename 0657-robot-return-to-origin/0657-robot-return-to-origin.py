class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('L')!=moves.count('R'):
            return False
        if moves.count('U')!=moves.count('D'):
            return False
        else:
            return True
        