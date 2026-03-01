class Solution:
   
    def SetMatrixZero(self,matrix):
            row = len(matrix)
            col = len(matrix[0])
            row_arr = [0]*row
            col_arr = [0]*col
            for i in range(0,row):
                for j in range(0,col):
                    if matrix[i][j] == 0:
                        row_arr[i] = 1
                        col_arr[j] = 1
          
            for i in range(0,row):
                for j in range(0,col):
                    if row_arr[i] == 1 or col_arr[j] == 1:
                        matrix[i][j] = 0
        


matrix = [[1,0,1],[1,4,5],[1,2,0]]
s1 = Solution()
s1.SetMatrixZero(matrix)

for row in matrix:
    print(row)