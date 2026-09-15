class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowDict = {}
        countEquals = 0
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple not in rowDict:
                rowDict[row_tuple] = 1
            else:
                rowDict[row_tuple] += 1

        for column in zip(*grid):
            if column in rowDict:
                countEquals += rowDict[column]
    
        return countEquals