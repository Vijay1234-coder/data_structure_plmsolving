''' '''
'''     * 
      * * 
    * * * 
  * * * * 
* * * * * '''

n=6
for i in range(1,n+1):
    print(" ")
    for j in range(1,n+1):
        if j < (n+1)-i:
            print(" ",end = " ")
        else:
            print("*",end =" ")
