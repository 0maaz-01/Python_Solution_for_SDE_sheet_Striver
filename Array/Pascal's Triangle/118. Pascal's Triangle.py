class Solution:
    def generate(self, numRows: int):
        ans = []
    # i = 0 and i = 1 ke liye fixed h pehle se hi,
    # baki ke liye calculate kr lenge
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            elif i == 1:
                ans.append([1,1])
            else:
                left, right = 0, 1
                current = []
                for r in range(i+1):
                    # har list me pehla aur last 1 h to
                    # use fix kr diya yaha pe
                    if r == 0 or r == i:
                        current.append(1)
                    else:
                        # baki ke liye uppar (pichli wali list) ke jo
                        # previous elements h use add kr rahe h
                        current.append(ans[i-1][left] + ans[i-1][right])
                        left += 1
                        right += 1
                ans.append(current)
        return ans


s = Solution()
print(s.generate(4))
