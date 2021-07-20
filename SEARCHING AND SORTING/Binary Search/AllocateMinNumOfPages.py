'''BEST QUESTION OF BINARY SEARCH '''
'''Allocate minimum number of pages
Difficulty Level : Hard
Last Updated : 12 May, 2021
Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages.
 Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum. 
Example : 
 

Input : pages[] = {12, 34, 67, 90}
        m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed 
in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 
      2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      2 with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 
      1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113. '''


def is_valid(arr,n,k,mid):
    student_count = 1
    sum1 = 0
    for i in range(n):
        sum1 +=arr[i]
        if sum1 > mid:
            student_count +=1
            sum1 =arr[i]

            if student_count >k :
                return -1
    return True



def findPages(arr,k,n):
    start = max(arr)
    end = sum(arr)
    result=-1
    if k > n:
        return -1
    while(start<=end):
        mid = start+(end-start)//2
        if(is_valid(arr,n,k,mid)==True):
            result = mid
            end=mid-1
        else:
            start =mid+1
    return result






arr = [10,20,30,40]
k = 2  # 2 students are here
n = len(arr)
print(findPages(arr,k,n))

