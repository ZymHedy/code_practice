# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        res = set()


        for i in range(len(ss)):
            # 仔细理解此处的递归
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                res.add(ss[i] + j)

        return sorted(res)

s = Solution()
ss = 'abc'
ans = s.Permutation(ss)
print(ans)
