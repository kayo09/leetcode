from typing import List
class Solution:
    def gcd(self, a: int, b: int):
        while b:
            a, b = b, a % b
        return a
    def lcm(self, a: int, b: int):
        return (a *b) // self.gcd(a,b)
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 0
        found = False
        while i < len(nums) - 1:
            if self.gcd(nums[i], nums[i+1]) > 1:
                nums[i] = self.lcm(nums[i], nums[i+1])
                nums.pop(i+1)
                found = True
            else:
                i += 1
            if not found:
                break
        return nums
solution = Solution()
print(solution.replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]))

