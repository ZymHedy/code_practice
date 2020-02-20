# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        f = []
        for i in range(len(array)):
            if i == 0 or f[i - 1] < 0:
                f.append(array[i])
            else:
                f.append(f[i - 1] + array[i])

        return max(f)


s = Solution()
data = [6, -3, -2, 7, -15, 1, 2, 2]
ans = s.FindGreatestSumOfSubArray(data)
print(ans)
