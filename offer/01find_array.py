# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    # 循环行，每行执行二分查找，复杂度nlog(n)
    def Find(self, target, array):
        if not array:
            return None
        row = len(array)
        col = len(array[0])
        for i in range(row):
            left, right = 0, col - 1

            while left <= right:
                mid = int((left + right) / 2)
                if array[i][mid] == target:
                    return True
                elif array[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

    # 从数组的右上角或者左下角开始遍历，
    # 从右上角遍历，如果右上角的数字>target，删去所在列；反之删掉所在行，逐步逼近左下角
    # 程序复杂度是o(row+col)
    def Find2(self, target, array):
        if not array:
            return None
        row = len(array)
        col = len(array[0])
        i, j = 0, col - 1  # 初始点坐标（第i行第j列）
        while i <= row - 1 and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


s = Solution()
matrix = [[1, 2, 3], [5, 6, 7]]
matrix1 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
ans = s.Find(7, matrix1)
ans2 = s.Find2(7, matrix1)
print(ans)
print(ans2)
