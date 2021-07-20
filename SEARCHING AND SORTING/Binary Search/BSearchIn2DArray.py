'''Binary Search in 2D Array'''
''' Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it.
    Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. 
    The designed algorithm should have linear time complexity. 

 Example: 

 Input: mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output: Found at (2, 1)
Explanation: Element at (2,1) is 29

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : Element not found
Explanation: Element 100 is not found . '''

''' in Bruit Force Approach will take O(N**2): because we will traverse the whole array using two loops'''
''' best solution using Binary Search on array: Complexty is O(M+N) because here in worst case we have to travel 
   whole row length and column length'''


def sortedMatrixSearch(arr, n, m, target):
    i = 0                             # set starting position of from where we satart search at top right corner of array
    j = m-1                           # arr[0][m-1]
    while(i>=0 and i<n and j>=0 and j<m): # here if whole array searched and it will false if target not found because it wil index out of bound will show
        if arr[i][j] == target:
            return i,j
        elif(target < arr[i][j]): # it means target is less than current element so we have to move left  : target will present lesft side or column
            j-=1
        elif(target > arr[i][j]): # target is greater than the current element so we have to search down because we get greater element at down side
            i+=1
    return -1   # if target not found we return -1





if __name__ == "__main__":
    n = 4
    m = 5
    target = 100
    arr = [[ 0, 6, 8, 9   , 11],
           [20, 22, 28, 29, 31],
           [36, 38, 50, 61, 63],
           [64, 66, 100,122,128]]
    print(sortedMatrixSearch(arr, n, m, target))