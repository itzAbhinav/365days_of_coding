class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float('-inf')
        sum_val  = 0

        for i in range(len(nums)):
            sum_val += nums[i]      #addition of values

            max_val = max(max_val,sum_val) #maximum val of addition for subarray

            if sum_val < 0:          # if addition is -ve then makes zero
                sum_val = 0

        return max_val

s1 = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = s1.maxSubArray(nums)    
print(ans)