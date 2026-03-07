class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        max_prefix = float('-inf')
        max_suffix = float('-inf')
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            if prefix == 0:               
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]       # checks product from prefix(left -> right)
            max_prefix = max(max_prefix,prefix)        # gets max of prefix output 
            suffix *= nums[len(nums) - i - 1] # checks product from suffix(right -> left)
            max_suffix = max(max_suffix,suffix)         # gets max of suffix output
            max_prod = max(max_prod,max_prefix,max_suffix) # gets max output from both suffix and prefix

        return max_prod    

s1 = Solution()
nums = [2,3,-2,4]
res = s1.maxProduct(nums)
print(res)