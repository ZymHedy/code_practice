# -*- coding:UTF-8 -*-
class Solution:
    def GetNumberOfK(self, data, K):
        if not data:
            return 0
        left, right = 0, len(data) - 1
        count = 0
        while left <= right:
            mid = int((left + right) / 2)
            if data[mid] == K:
                count += 1
                break
            elif data[mid] < K:
                left = mid + 1
            else:
                right = mid - 1

        left = mid - 1
        right = mid + 1
        while left >= 0 and data[left] == K:
            count += 1
            left -= 1
        while right <= len(data)-1 and data[right] == K:
            count += 1
            right += 1

        return count


s = Solution()
data = [5, 7, 7, 8, 8, 10]
data1 = [1, 2, 3, 3, 3, 3]
ans = s.GetNumberOfK(data1, 3)
print(ans)
