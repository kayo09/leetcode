class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        return sum(1 for word in text.split() if not set(word) & broken_set)

solution = Solution()
print(solution.canBeTypedWords("leet code", "lt"))

