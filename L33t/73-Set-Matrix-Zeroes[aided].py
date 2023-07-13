class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zerorows, zerocols = [], []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zerorows.append(r)
                    zerocols.append(c)
        
        for r in zerorows:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        
        for c in zerocols:
            for i in range(len(matrix)):
                matrix[i][c] = 0