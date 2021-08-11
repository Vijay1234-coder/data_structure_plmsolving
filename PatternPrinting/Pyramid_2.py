''''''
''' * 
   * * 
  * * * 
 * * * * 
* * * * *         '''

n = 9

for i in range(n):
    print(" ")
    for j in range(n-i-1):
        print(" ",end = "")
    for j in range(i+1):
        print("*" ,end =" ")