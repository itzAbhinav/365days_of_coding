class Solution:
    def find3sum_zero(self,nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            head = i + 1
            tail = len(nums) - 1
            temp = []
            while head <= tail:
                if (nums[i] + nums[head] + nums[tail]) == 0:
                    temp = [nums[i],nums[head],nums[tail]]
                    res.append(temp)
                head += 1
                tail -= 1
            res.sort()    
        return res

nums = [1, -2, 1, 0, 5]
s1 = Solution()
ans = s1.find3sum_zero(nums)
for i in ans:
    print(i,end="")
