import math as m

class Solution:

    def __init__(self,N,r,c):   #constructor 
         self.N = N
         self.r = r
         self.c = c

    def nCr(self,r,c):
           return m.factorial(r) // (m.factorial(c) * m.factorial(r-c))   # nCr combination used to find the next upcoming elements
      
        
    def printPascal(self, N):
         for i in range(N):
                for j in range(i+1):
                   print(self.nCr(i,j),end=" ")               # pascal trianle printed usinf nCr combination 
                print()
    
    def printNthrow(self, N):
         for i in range(N):                                     # To print the Nth row we iterate throuht whole Nth row usinf nCr combination
              print(self.nCr(N-1,i),end=" ")

    def printElement(self, r, c):
         print(f"Element at posititon (n,r) : {self.nCr(r-1,c-1)}")         # To find the specific elem in pascal trianle we use nCr(row - 1, col - 1)


if __name__ == "__main__":
    N = 5
    r = 5
    c = 3
    s1 = Solution(N,r,c)
    s1.printPascal(N)        
    print()
    s1.printNthrow(N)
    print()
    s1.printElement(r,c)


