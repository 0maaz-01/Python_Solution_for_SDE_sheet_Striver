class Solution:
    def generate(self, numRows: int):
        ans = []

        for i in range(numRows):
            if i == 0:
                ans.append([1])
            elif i == 1:
                ans.append([1,1])
            else:
                left, right = 0, 1
                current = []
                for r in range(i+1):
                    if r == 0 or r == i:
                        current.append(1)
                    else:
                        current.append(ans[i-1][left] + ans[i-1][right])
                        left += 1
                        right += 1
                        
                ans.append(current)
        return ans


