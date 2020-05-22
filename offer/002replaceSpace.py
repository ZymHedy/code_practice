class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return s
        s_replace = ''
        for i in range(len(s)):
            if s[i] == ' ':
                s_replace += '%20'
            else:
                s_replace += s[i]
        return s_replace


s = Solution()
x = 'we are happy'
y = ' '
print(s.replaceSpace(y))
