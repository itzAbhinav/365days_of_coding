
class Solution:
    def findNextPermute(self, nums):
        self.nums = nums
        index = -1
        for i in range(len(nums) - 2,-1,-1):  # Finding breaking point index
            if nums[i] < nums[i+1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return nums

        for i in range(len(nums) - 1, index, -1):
            if nums[index] < nums[i]:
                nums[index],nums[i] = nums[i], nums[index]  # Swap to next greatest number
                break
        nums[index + 1:] = reversed(nums[index + 1 : ])        # reversing the string after index + 1
        return nums

nums = [1,3,2]


s1 = Solution()
s1.findNextPermute(nums)
print(" ".join(map(str, nums)))

