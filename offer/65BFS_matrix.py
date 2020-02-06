# -*- coding:UTF-8 -*-
class Solution:
    def has_path(self, matrix, rows, cols, path):
        self.rows = rows
        self.cols = cols
        if not matrix:
            return False
        if not path:
            return True
        #matrix输入是list形式，因此需要转换成矩阵形式
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.search(x,i,j,path):
                    return True
                    # return 11111
        return False

    def search(self,x,i,j,path):
        if x[i][j] == path[0]:
            #path只有一个字符的情况
            if not path[1:]:
                return True
            #没有建立visited列表，所以将当前遍历的字符变成空的防止重复访问
            x[i][j] = ''
            if i > 0 and self.search(x,i-1,j,path[1:]):
                return True
            elif i < self.rows-1 and self.search(x,i+1,j,path[1:]):
                return True
            elif j > 0 and self.search(x,i,j-1,path[1:]):
                return True
            elif j < self.cols-1 and self.search(x,i,j+1,path[1:]):
                return True
            x[i][j] = path[0]#上面情况都不符合，恢复当前位置的原值
            return False
        else:
            return False

s = Solution()
matrix = "ABCESFCSADEE"
path = "ABCB"
print(s.has_path(matrix,3,4,"ABCB"))
# print(ans)
