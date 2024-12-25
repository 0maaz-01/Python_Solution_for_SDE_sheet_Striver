# **Pascal’s Triangle?**
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Array/Pascal's%20Triangle/Images/A.png)
![image at](https://github.com/0maaz-01/Python_Solution_for_SDE_sheet_Striver/blob/main/Array/Pascal's%20Triangle/Images/B.png)

### **What is Pascal’s Triangle?**
Pascal’s Triangle is a triangular array of integers where:
1. The first and last numbers of each row are `1`.
2. Each number in between is the sum of the two numbers directly above it in the previous row.

For example:
```
Row 0:      [1]
Row 1:     [1, 1]
Row 2:    [1, 2, 1]
Row 3:   [1, 3, 3, 1]
Row 4:  [1, 4, 6, 4, 1]
```

---

### **Code Explanation**

#### **1. Initialize the Result (`ans`)**
```python
ans = []
```
- `ans` will store all rows of Pascal’s Triangle as a list of lists.
- For example, after generating 3 rows, `ans` will be `[[1], [1, 1], [1, 2, 1]]`.

---

#### **2. Loop through the Rows**
```python
for i in range(numRows):
```
- The loop iterates from `0` to `numRows - 1`. Each iteration generates one row of the triangle.

---

#### **3. Base Cases for Row 0 and Row 1**
```python
if i == 0:
    ans.append([1])
elif i == 1:
    ans.append([1, 1])
```
- **Row 0**: The first row is `[1]`.
- **Row 1**: The second row is `[1, 1]`.
- These are added directly to `ans`.

---

#### **4. Generate Rows Beyond the Second Row**
```python
else:
    left, right = 0, 1
    current = []
```
- For rows beyond the first two, we calculate the values based on the previous row.
- **Pointers**:
  - `left` and `right` point to adjacent indices in the previous row to calculate the sum.
- **`current`**:
  - This list will store the values of the current row being generated.

---

#### **5. Populate the Current Row**
```python
for r in range(i + 1):
    if r == 0 or r == i:
        current.append(1)
    else:
        current.append(ans[i-1][left] + ans[i-1][right])
        left += 1
        right += 1
```
- **Outer Elements**:
  - If the index `r` is `0` (first element) or `i` (last element), append `1`.
- **Middle Elements**:
  - For other indices, calculate the sum of the two numbers above in the previous row:
    ```python
    current.append(ans[i-1][left] + ans[i-1][right])
    ```
  - Move `left` and `right` pointers forward to process the next pair of numbers.

---

#### **6. Add the Current Row to the Result**
```python
ans.append(current)
```
- After completing the current row, add it to `ans`.

---

#### **7. Return the Result**
```python
return ans
```
- After generating all rows, return the complete Pascal’s Triangle.

---

### **Example Walkthrough**

#### Input: `numRows = 4`

**Initialization**:
```python
ans = []
```

**Iteration 1 (`i = 0`)**:
```python
ans = [[1]]
```

**Iteration 2 (`i = 1`)**:
```python
ans = [[1], [1, 1]]
```

**Iteration 3 (`i = 2`)**:
- Start with `left = 0`, `right = 1`, and `current = []`.
- Process each index in row 2 (`range(3)`):
  - `r = 0`: Append `1`.
  - `r = 1`: Append `ans[1][0] + ans[1][1] = 1 + 1 = 2`.
  - `r = 2`: Append `1`.
```python
ans = [[1], [1, 1], [1, 2, 1]]
```

**Iteration 4 (`i = 3`)**:
- Start with `left = 0`, `right = 1`, and `current = []`.
- Process each index in row 3 (`range(4)`):
  - `r = 0`: Append `1`.
  - `r = 1`: Append `ans[2][0] + ans[2][1] = 1 + 2 = 3`.
  - `r = 2`: Append `ans[2][1] + ans[2][2] = 2 + 1 = 3`.
  - `r = 3`: Append `1`.
```python
ans = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
```

**Output**:
```python
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
```

---

### **Time Complexity**
- Each row has i + 1 elements, and generating a single row involves O(i) operations.
- The total cost is:
  O(1) + O(2) + O(3) + ...... + O(n) = O(n(n+1)/2) = O(n^2)
  

### **Space Complexity**
- The space used is proportional to the size of the result: O(n^2).
