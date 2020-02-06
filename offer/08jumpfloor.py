# -*- coding:utf-8 -*-
#这道题目的数学思路：f(1)=1,f(2)=2,f(n)=f(n-1)+f(n-2)
class Solution:
    def jumpFloor(self, number):
        # write code here
        s = [0,1,2]
        for i in range(3,number+1):
            s.append(s[i-1]+s[i-2])
        return s[number]

s = Solution()
ans = s.jumpFloor(11)
print(ans)
