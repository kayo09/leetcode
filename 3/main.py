class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=(i)

        print(dic)

    

solution=Solution()
s = "pwwkew"
solution.lengthOfLongestSubstring(s)
