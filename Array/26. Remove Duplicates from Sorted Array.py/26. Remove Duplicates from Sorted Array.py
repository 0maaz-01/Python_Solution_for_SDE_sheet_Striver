from typing import List
class Solution0:       # Most Optimal
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 1
        for r in range(1, len(nums)):
            if (nums[r] != nums[r - 1]):
                nums[l] = nums[r]
                l += 1

        return l


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1

        while index < len(nums):
            while index < len(nums) and nums[index] == nums[index - 1]:
                nums.pop(index)

            index += 1

        return len(nums)


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1

        while index < len(nums):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
                index -= 1

            index += 1

        return len(nums)


s = Solution()
print(s.removeDuplicates())