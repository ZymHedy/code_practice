# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串

    # 暴力法（用于帮助理解思路）
    # 虽然暴力法思路容易理解，但是当字符串过长，递归过深的时候复杂度极大，超出可运行时间
    # 动态规划则不会出现这个问题，效率还是更高
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        elif s and not pattern:
            return False
        elif not s and pattern:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        else:
            # s和pattern均不为空
            # 区分pattern的下一个元素是否为*
            if len(pattern) > 1 and pattern[1] == '*':
                # s与pattern的第一个元素不同，相当于*前一个字符无法匹配，则pattern后羿两位
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                else:
                    # s[0]==pattern[0]分为三种情况
                    # 1、*前的字符出现0次：s不变，直接忽略pattern的x*前两位，让字符串从后面几位开始匹配
                    # 2、*前的字符出现1次：s后移一位，pattern后移2位，eg:a与a*匹配
                    # 3、*前的字符出现n次：s后移一位，pattern不变
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)

            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False

    # 动态规划，找最优子结构，找状态转移方程，理论上来说复杂度更低
    def isMatch(self, s, p):
        if not p:
            return not s
        # s空，p只有一个字符，一定是不匹配的
        if not s and len(p) == 1:
            return False

        # 两种情况需要判断
        # 1、s空p是长度大于1的非空字符串
        # 2、s，p均为非空

        # 找状态转移方程，要根据具体情况判定，if else
        # 初始化状态转移矩阵dp[i][j]:s的前i个字符与p的前j个字符相匹配
        # 为了状态转移访问之前的状态，行列都多1
        row = len(s) + 1
        col = len(p) + 1
        dp = [[False for j in range(col)] for i in range(row)]
        dp[0][0] = True  # 预备状态
        # 为70行的那种情况做初始化用的，逻辑的可解释性很差
        for c in range(2, col):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        # 依据题目逻辑判断状态转移矩阵
        # i,j从0开始，r,c从1开始
        for r in range(1, row):
            i = r - 1
            for c in range(1, col):
                j = c - 1
                # 这种思路下我们只考虑s,p的当前元素和前一个元素
                if p[j] == s[i] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    # 区分，p[j-1]与s[i]是否匹配
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[r][c] = dp[r][c - 2]
                    else:
                        # 分为三种情况
                        # 1、*匹配0次s[i]
                        # 2、*匹配1次s[i]，不需要考虑这种情况了，p[j] == s[i]在第一个if分支已经考虑过了
                        # 3、*匹配n次s[i]
                        dp[r][c] = dp[r][c - 2] or dp[r - 1][c]
                else:
                    dp[r][c] = False

        return dp[row - 1][col - 1]

        # 仿照遍历法的思路不可行，主要因为字符串和矩阵的上界下界问题
        #         # 如果按照下一个元素是否是*这种方式，到达字符串上界的时候一定会溢出
        #         # 字符串下界的溢出已经通过矩阵从1开始遍历，且pattern的首个元素不等于*
        #         # 区分p的下一个元素是否是*
        #         if p[j + 1] == '*':
        #             # 区分p中*的前一个字符是否与s的当前字符匹配
        #             # 因为pattern不会出现第一个字符是*的情况，所以p[j-1]不会越界
        #             if p[j - 1] != s[i] and p[j-1] != '.':
        #                 dp[r][c] = dp[r][c-2]
        #                 pass
        #             else:
        #                 pass
        #         else:
        #             if p[j] == s[i] or p[j] == '.':
        #                 dp[r][c] = dp[r - 1][c - 1]


so = Solution()
s = 'aaaaaaaaaaaaab'
pattern = 'a*a*a*a*a*a*a*a*a*a*c'
# ans = so.match(s, pattern)
ans1 = so.isMatch(s,pattern)
# print(ans)
print(ans1)
