class Solution:
   
    def SetMatrixZero(self,matrix):
            row = len(matrix)
            col = len(matrix[0])
            row_arr = [0]*row             # row marker
            col_arr = [0]*col             # column marker
            for i in range(0,row):
                for j in range(0,col):       # Nested loop checks if matrix is equal to zero if yes then marks the row and col markers 1
                    if matrix[i][j] == 0:
                        row_arr[i] = 1
                        col_arr[j] = 1
          
            for i in range(0,row):
                for j in range(0,col):
                    if row_arr[i] == 1 or col_arr[j] == 1:   # Again reiterate the matrix if any row or col markers are 1 make the matrix elem 0
                        matrix[i][j] = 0
        


matrix = [[1,0,1],[1,4,5],[1,2,0]]
s1 = Solution()
s1.SetMatrixZero(matrix)

for row in matrix:
    print(row)
