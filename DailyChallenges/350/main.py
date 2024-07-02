class Solution(object):
    def intersect(self, nums1, nums2):
        same=[]
        for elem in nums1:
            if elem in nums2: 
                same.append(elem)
                nums2.remove(elem)
        return (same)






solution=Solution()
nums1 = [1,2,2,1]
nums2 = [2]
result=solution.intersect(nums1,nums2)
print(result)
