# -*- coding:utf-8 -*-
class Solution:
    # 只适合没有重复元素的数组
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 判断数组是否为空
        if not rotateArray:
            return 0

        left, right = 0, len(rotateArray) - 1
        # 判断是否是旋转数组
        if rotateArray[right] > rotateArray[left]:
            return rotateArray[0]

        # 旋转数组的情况下，进行判断
        while left <= right:
            mid = int((left + right) / 2)
            if rotateArray[mid] > rotateArray[0]:
                left = mid
            else:
                right = mid

            if left + 1 == right:
                return rotateArray[right]

    # 不动脑子的写法，直接寻找最小值
    def minNumberInRotateArray2(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        pre = -7e20
        for num in rotateArray:
            if num < pre:
                return num
            pre = num
        return rotateArray[0]


s = Solution()
rotate_array = [3, 4, 5, 1, 2]
array1 = [1, 3, 5]
ans = s.minNumberInRotateArray(array1)
print(ans)
