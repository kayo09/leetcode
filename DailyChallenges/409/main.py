class Solution(object):
    def longestPalindrome(self, s):

        count =0 
        arr=set()
        for c in s:
            if c in arr:
                arr.remove(c)
                count+=2

            else:
                arr.add(c)
        if arr:
                count+=1
        print(count)




solution=Solution()
s="abccccdd"
solution.longestPalindrome(s)

