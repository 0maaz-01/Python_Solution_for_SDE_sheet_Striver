# Three Sum – LeetCode Question Number 15
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Images/3_Sum_1.png)
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Images/3_Sum_2.png)

### Link to the problem –
https://leetcode.com/problems/3sum/description/

---

## **Step-by-Step Explanation**
1. **Import List Modules**
   
   ```python
   from typing import List
   ```
   - This imports the `List` type from Python's `typing`, making it clear that the input `nums` is a list of integers, and the output is a list of lists of integers.
     You don't need to import it on LeetCode, but if you are running on another IDE than you should import this module to run the code.
---

2. **Define the Function**
   
   ```python
   class Solution:
       def threeSum(self, nums: List[int]) -> List[List[int]]:
   ```
   - `threeSum` is a method within the `Solution` class. It takes an array of integers `nums` and returns a list of unique triplets that sum to zero.

---

3. **Sort the Array**
   
   ```python
   nums.sort()
   ```
   - The array is sorted to simplify handling duplicates and enable the use of the two-pointer approach that we will use to solve this question. Sorting ensures that equal elements are adjacent, which is critical for avoiding duplicate triplets.

---
4. **Initialize the Result Array**
   
   ```python
   result = []
   ```
   - This list will store all the unique triplets that meet the criteria.

---

5. **Iterate Through the Array**
   
   ```python
   for i in range(len(nums)):
   ```
   - The loop iterates through the array. Each element at index `i` is treated as the fixed number in a triplet. 

---
6. **Skip Duplicates**
   
   ```python
   if i > 0 and nums[i] == nums[i - 1]:
       continue
   ```
   - This ensures that the same number is not reused as the fixed number in multiple iterations, avoiding duplicate triplets.
   - Example :
     Suppose the input array is:
     
     nums = [-1, -1, 0, 1, 2]

After sorting, the array becomes:
     nums = [-1, -1, 0, 1, 2]

     
Now, let's walk through the iteration:

Step 1: i = 0

Fixed element: nums[i] = -1.

The algorithm looks for two numbers that sum to 1 (since -1 + (nums[left] + nums[right]) = 0).

Assume a valid triplet is found: [-1, -1, 2].

Step 2: i = 1

Fixed element: nums[i] = -1 (same as nums[0]).

Without the condition 

```python
if i > 0 and nums[i] == nums[i - 1]:
  continue
```

the algorithm would again find the same triplet [-1, -1, 2].

With the condition:

Since nums[i] == nums[i - 1], the algorithm skips this iteration and does not repeat the same work.

The duplicate triplet is avoided.


---

7. **Set Up Two Pointers**
   
   ```python
   left, right = i + 1, len(nums) - 1
   ```
   - After fixing `nums[i]`, use two pointers:
     - `left` starts at `i + 1` (immediate next element).
     - `right` starts at the end of the array.
   - This setup allows us to efficiently find pairs that, along with `nums[i]`, sum to zero.

---

8. **While Loop for Two Pointers**
   
   ```python
   while left < right:
       total = nums[i] + nums[left] + nums[right]
   ```
   - The loop continues as long as `left` is less than `right`. The `total` variable stores the sum of the current triplet (`nums[i] + nums[left] + nums[right]`).

---

9. **Three Cases Based on `total`**
    
   - **Case 1: Total is Less than Zero**
     ```python
     if total < 0:
         left += 1
     ```
     - If the sum is too small, move `left` to the right to increase the sum (because the array is sorted).

   - **Case 2: Total is Greater than Zero**
     ```python
     elif total > 0:
         right -= 1
     ```
     - If the sum is too large, move `right` to the left to decrease the sum.

   - **Case 3: Total is Exactly Zero**
     ```python
     else:
         result.append([nums[i], nums[left], nums[right]])
     ```
     - If the sum is zero, the current triplet is added to the `result` list.

---

10. **Skip Duplicates for `left` and `right`**
    
    - After finding a valid triplet, skip duplicate values for `left` and `right` to avoid duplicate triplets.
      ```python
      while left < right and nums[left] == nums[left + 1]:
          left += 1
      while left < right and nums[right] == nums[right - 1]:
          right -= 1
      ```
    - These loops move `left` and `right` pointers until they point to new, unique values.

---

11. **Move Pointers**
    
    ```python
    left += 1
    right -= 1
    ```
    - After handling duplicates, shift both pointers to explore other potential triplets.

---

12. **Return the Result**
    
    ```python
    return result
    ```
    - After all iterations are complete, the method returns the list of unique triplets.

---



