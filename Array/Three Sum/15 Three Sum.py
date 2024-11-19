from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We are sorting the array, so that we can apply the logic below.
        nums.sort()
        # The array that will store the answer.
        result = []

        for i in range(len(nums)):
    # To skip getting same shuffled pairs in our answer
    # [1,2,3] and [3,2,1] are examples of same shuffled pairs.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    # At the beginning, the left pointer is pointing towards element
    # present at i + 1 th index and right pointer is pointing towards
    # the element present at the len(nums)-1 index

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

            # If total is less than zero, then we need to move the left 
            # we won't decrease the value of right because
            # agr total < 0 h to left me uske next wali badi value ko daal do
                if total < 0:
                    left += 1
            # agr total > 0 h to right me uske previous wali  choti value ko daal do
                elif total > 0:
                    right -= 1
            # jab total = 0 h to uss pair ko result me append kr lo
                else:
                    result.append([nums[i], nums[left], nums[right]])
            # jab left right se chota h and left aur uske baad wali value equal h to
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1             # left ko 1 se increase kr do
            # jab left right se chota h and right aur uske pehle wali value equal h to
                    while left < right and nums[right] == nums[right - 1]:
            # right ko 1 se decrease kr do, jisse ki vo right ke pehle wale element ko point krne lag jaaye
                        right -= 1
            # yha pe append krne ke baad left aur right ki value change krne ki zarurat h kyuki agar hum change nahi karenge
            # to upar if/elif wali condition se wapas same pair append ho jaayega. agr left or right dono naye honge to
            # naye pair add honge
                    left += 1
                    right -= 1

        return result

