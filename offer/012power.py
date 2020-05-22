class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0.0:
            return 0
        if exponent == 0:
            return 1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        if exponent < 0:
            return 1 / result
        return result

    def power_fast(self,base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        result = self.power_fast(base, abs(exponent) >> 1)
        result *= result
        if exponent & 1 == 1:
            result *= base
        if exponent < 0:
            return 1 / result

        return result




s = Solution()
# print(s.Power(0.0, -1))
print(s.power_fast(2, -3))
