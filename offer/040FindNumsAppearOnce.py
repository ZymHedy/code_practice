class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # 全组异或
        result = 0
        for i in array:
            result ^= i

        # 判最低位1
        indexBit = 0
        while result & 1 == 0:  # 用于判断是否到达最低位的1
            result >>= 1
            indexBit += 1

        a = 0
        b = 0
        # 根据最低位1的情况分组
        for i in array:
            if self.isBit1(i, indexBit):
                a ^= i
            else:
                b ^= i

        return [a, b]

    def isBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1


arr = [1, 2, 3, 2, 1,5]
s = Solution()
print(s.FindNumsAppearOnce(arr))
