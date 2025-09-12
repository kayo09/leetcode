class Solution:
    def doesAliceWin(self, s:str) -> bool:
        turn = True
        vowels = "aeiou"
        vowels_idx = [i for i, char in enumerate(s) if char.lower() in vowels]
        print(vowels_idx)
        while(turn):
            turn, s = self.alice(vowels_idx, s)
        return 0
    def alice(self, idxL: list, s: str):
        if (len(idxL)/2 !=0):
            pass


solution = Solution()
solution.doesAliceWin("leetcoder")

