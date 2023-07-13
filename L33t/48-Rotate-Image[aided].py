class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # [::-1] flips the matrix upside down
        # zip() transposes the entire matrix 

        matrix[:] = zip(*matrix[::-1])
