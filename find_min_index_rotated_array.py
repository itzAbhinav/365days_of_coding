class Solution:
      def find_index(self,nums):
            head = 0
            tail = len(nums) - 1
            min_val = float('inf')
            idx = -1
            while head <= tail:
                  min_val = min(min_val,nums[head],nums[tail])
                  if min_val == nums[head]:
                        idx = head
                  elif min_val == nums[tail]:
                        idx = tail      
                  head+=1
                  tail-=1

            return idx

s1 = Solution()
nums = [11,13,15,17]
print(s1.find_index(nums))            
