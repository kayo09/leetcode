'''
s--> string
t--> string
maxCost--> int


'''
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        start = 0
        max_length = 0
        current_cost = 0
        
        for end in range(len(s)):
            current_cost += abs(ord(s[end]) - ord(t[end]))
            
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length



solution=Solution()
s="abcd"
# t="bcdf"
# t="acde"
# t="cdef"
t="bcdf"
maxCost=3
results=solution.equalSubstring(s,t,maxCost)
print(results)