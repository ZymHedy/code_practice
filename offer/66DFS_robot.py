# -*- coding:UTF-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        self.rows = rows
        self.cols = cols
        self.threshold = threshold
        self.visited = set()
        self.wall = set()
        self.sum = 0
        self.DFS(0, 0)
        return self.sum

    def sum_bit(self,i,j):
        #map函数：把list中的元素都变成int类型
        return sum(map(int,list(str(i))))+sum(map(int,list(str(j)))) <= self.threshold

    def border(self,i,j):
        flag_i = False
        flag_j = False
        if i >= 0 and i <= self.rows-1:
            flag_i = True
        if j >= 0 and j <= self.cols-1:
            flag_j = True
        return flag_i and flag_j

    def DFS(self,i,j):
        #！！！！self.wall！！！！非常重要，否则会错误记录（符合sum条件但是不相邻的点）
        if ((i,j) in self.wall): return None #记录不符合sum条件的点，如果碰到这样的点直接递归结束
        if ((i,j) in self.visited): return None #避免记录过的点
        if not self.border(i,j): return None #避免超出矩阵范围

        self.visited.add((i,j))
        if self.sum_bit(i,j):
            self.sum += 1
            self.DFS(i + 1, j)
            self.DFS(i - 1, j)
            self.DFS(i, j + 1)
            self.DFS(i, j - 1)
        else:
            self.wall.add((i,j))




s = Solution()
ans = s.movingCount(10,1,100)
print(ans)