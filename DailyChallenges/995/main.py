class Solution(object):
    def minKBitFlips(self, nums, k):
        #XOR
        '''
        nums=[0,1,0]
        k=1
        how many ways can nums be divided into
        subarrays of length k, what are the subarrays?

        '''
        bit_flip=0
        subarray=[]
        for i in range(len(nums)):
            for _ in range(k):
                if nums[i]==1:
                    bit_flip-=1
                subarray.append(nums[i])
                nums[i]^=1


                if len(subarray)==k:
                    bit_flip+=1
                    subarray=[]
                else: break
        if bit_flip==0:
            return -1
        print(bit_flip)
        return bit_flip

        #output: number of k-bit flips (Condition: no 0 in nums. i.e nums has every element as 1), else -1


solution=Solution()
nums = [0,0,0,1,0,1,1,0]
k=3
results=solution.minKBitFlips(nums,k)
print(results)
