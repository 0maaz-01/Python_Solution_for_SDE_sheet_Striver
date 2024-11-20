# Remove Duplicates from Sorted Array
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Images/Remove_Duplicates_from_Sorted_Array_1.png)
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Images/Remove_Duplicates_from_Sorted_Array_2.png)
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Images/Remove_Duplicates_from_Sorted_Array_3.png)
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Images/Remove_Duplicates_from_Sorted_Array_4.png)

### Link to the problem –
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

---

## **Step-by-Step Explanation**

---

### **1. Import List Modules**

```python
from typing import List
```

- This imports the `List` type from Python's `typing` module.  
- On LeetCode, this is optional, but in external IDEs, you need this import. If you don't import this module you will run into an error.

---

### **2. Define the Function**

```python
class Solution:  
    def removeDuplicates(self, nums: List[int]) -> int:
```

- The function `removeDuplicates` is defined as a method in the `Solution` class.  
- It takes a single argument, `nums`, which is a sorted list of integers, and it returns the count of unique elements in the list.

---

### **3. Initialize the Left Pointer**

```python
l = 1
```

- The pointer `l` is initialized to `1`.  
- It represents the position where the next unique element will be placed.  
- The first element is always unique, so we start from the second position.

---

### **4. Iterate Through the Array**

```python
for r in range(1, len(nums)):
```

- A loop is used to iterate through the array with a pointer `r` starting at index `1`.  
- The pointer `r` (right pointer) checks all elements after the first to identify unique values.

---

### **5. Check for a Unique Value**

```python
if nums[r] != nums[r - 1]:
```

- This condition checks if the current element (`nums[r]`) is different from the previous element (`nums[r - 1]`).  
- If they are different, it means `nums[r]` is a unique element.

---

### **6. Place the Unique Value at the Left Pointer**

```python
nums[l] = nums[r]
l += 1
```

- When a unique value is found:
  - It is placed at the position pointed to by `l`.
  - The `l` pointer is incremented to prepare for the next unique value.
- This ensures all unique elements are grouped at the start of the array.

---

### **7. Return the Count of Unique Elements**

```python
return l
```

- After the loop finishes, `l` contains the count of unique elements in the array.  
- The array has been modified in-place, with the first `l` positions containing the unique elements.

---

## **Example Walkthrough**

### **Input**
```python
nums = [1, 1, 2, 2, 3]
```

---

### **Step-by-Step Execution**

| Step | `r` | `nums[r]` | `nums[r - 1]` | Condition (`nums[r] != nums[r-1]`)? | Action                       | `nums` After Action    | `l` |
|------|-----|-----------|---------------|------------------------------------|------------------------------|-------------------------|-----|
| 1    | 1   | 1         | 1             | No                                 | No change                   | `[1, 1, 2, 2, 3]`       | 1   |
| 2    | 2   | 2         | 1             | Yes                                | Place `nums[2]` at `nums[1]` | `[1, 2, 2, 2, 3]`       | 2   |
| 3    | 3   | 2         | 2             | No                                 | No change                   | `[1, 2, 2, 2, 3]`       | 2   |
| 4    | 4   | 3         | 2             | Yes                                | Place `nums[4]` at `nums[2]` | `[1, 2, 3, 2, 3]`       | 3   |

---

### **Final State**

- **Modified Array**: `[1, 2, 3, 2, 3]`
  - The first `l = 3` positions contain unique elements: `[1, 2, 3]`.  
  - Values after index `l-1` are irrelevant.
- **Return Value**: `l = 3` (number of unique elements).

---

### **Output**

- **Result**: `3`
- **Modified Array**: `[1, 2, 3]` (first `l` elements are the unique ones).
