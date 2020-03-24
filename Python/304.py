class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            curSum = 0
            for num in matrix[i]:
                curSum += num
                self.sums[i].append(curSum)
            
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1, row2 + 1):
            result += self.sums[i][col2 + 1] - self.sums[i][col1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)