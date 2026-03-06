class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1                     # Initializing all the values                                             
        count_zero = 0
        ans = []
        idx = -1
        for i in range(len(nums)):      # First loop to find product of number and count no of zeroes
            if nums[i] == 0:
                count_zero += 1
                idx = i
            else:
                product *= nums[i]

        if count_zero > 1 :                 # If zeros more than one return null list
            return [0]*(len(nums))

        for i in range(len(nums)):            # if no zeros just print all the values 
            if count_zero != 1: 
               ans.append(product//nums[i])
            else:
                if nums[i] == 0:                # if 1 zero then just print product for that number other elems to be sero
                    ans.append(product)
                else:
                    ans.append(0)
        return ans 

nums = [-1,1,0,-3,3]
s1 = Solution()
print(s1.productExceptSelf(nums))

