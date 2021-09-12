import sys


def median(a1,a2,n1,n2):
    #this algorithm based on :
    # length of a1 should be equal or less  than length of a2
    if n1>n2:
        a1,a2 = a2,a1

    start1 = 0
    end1 = n1-1
    while start1<=end1:
        i1= (start1+end1)//2
        i2 = (n1+n2+1)//2-i1
        min1 = a1[i1] if i1!=n1 else sys.maxsize
        min2 = a2[i2] if i2!=n2 else sys.maxsize

        max1 = a1[i1-1] if i1!=0 else -sys.maxsize
        max2 = a2[i2-1] if i2!=0 else -sys.maxsize

        if max1<=min2 and max2<=min1:
            if (n1+n2)%2==0:
                return (max(max1,max2)+min(min1,min2))/2
            else:
                return max(max1,max2)/1





        elif max2>min1:
            start1 = i1+1


        elif max1>min2:
            end1 = i1-1












a1 =[10,20,30,40,50]
n1 =len(a1)
a2 = [5,15,25,35,45,55,65,75,85]
n2 =len(a2)
x=median(a1,a2,n1,n2)
print(x)