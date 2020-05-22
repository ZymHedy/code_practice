class Solution:
    def NumberOf1(self, n):
        # write code here
        nbin = bin(n & 0xffffffff)
        return nbin.count('1')


from ctypes import *


class Solution2:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while c_int(n).value != 0:
            count += 1
            n = n & (n - 1)
        return count


s = Solution()
s2 = Solution2()
number = s.NumberOf1(3)
number2 = s2.NumberOf1(3)
print(number)
print(number2)
