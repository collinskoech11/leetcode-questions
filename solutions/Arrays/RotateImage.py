class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        #revesre the whole matrix first
        matrix.reverse()
        for r in range (N):
          for c in range (r):
            #then transpose the matrix
            matrix[c][r],matrix[r][c] = matrix[r][c],matrix[c][r]
