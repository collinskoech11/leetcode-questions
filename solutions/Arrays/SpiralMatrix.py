class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return [] #return an empty list if there is no matrix
        output = []
        #initialise rows and columns
        start_row = 0
        end_row = len(matrix)
        start_column = 0
        end_column = len(matrix[0])
        
        while start_row < end_row or start_column < end_column:
            #right
            if start_row < end_row:
                output.extend([matrix[start_row][i] for i in range(start_column,end_column)])
                start_row +=1
            #down
            if start_column < end_column:
                output.extend([matrix[i][end_column-1] for i in range(start_row,end_row)])
                end_column -=1
            #left
            if start_row < end_row:
                output.extend([matrix[end_row-1][i] for i in range(end_column -1,start_column -1, -1)])
                end_row -=1
            #up
            if start_column < end_column:
                output.extend([matrix[i][start_column] for i in range(end_row -1,start_row -1, -1)])
                start_column +=1 
                
        return output
